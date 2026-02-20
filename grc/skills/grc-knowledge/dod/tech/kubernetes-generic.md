# Kubernetes (Non-Platform One) — DoD ATO Playbook

Non-P1 Kubernetes means you own the full K8s hardening stack. There's no platform ATO to inherit from — just the underlying IaaS (AWS/Azure/on-prem) plus everything you build on it. This is significantly more work than P1 but gives you full control. Common for programs that can't or won't use P1, or for programs running on-prem K8s.

---

## Scope of This Playbook

This covers Kubernetes deployments that:
- Are NOT on Platform One / Cloud One
- May be on: AWS EKS (standalone), Azure AKS (standalone), on-prem (kubeadm/RKE2/k3s), DISA MilCloud VMs
- Require the team to own the K8s STIG compliance (no platform ATO covering it)

If you're on Platform One, use `platform-one.md` instead — most of this is already handled.

---

## Required STIGs and Benchmarks

**DISA STIGs for Kubernetes:**
- **Kubernetes STIG V1R11+** (currently V2R2): `public.cyber.mil/stigs` → search "Kubernetes"
- **Container Platform SRG** (Security Requirements Guide): Covers container platforms generally
- **Docker Enterprise STIG** (if using Docker Enterprise) or **Container Runtime** guidance

**Node OS STIGs:**
| OS | STIG |
|----|------|
| RHEL 8 / RHCOS | RHEL 8 STIG (V1R14+) |
| RHEL 9 | RHEL 9 STIG |
| Ubuntu 20.04 | Canonical Ubuntu 20.04 STIG |
| Windows Node | Windows Server STIG |

**CIS Kubernetes Benchmark v1.8** (supplement to DISA STIG):
- Master node security configuration
- Worker node security configuration
- API server settings
- etcd security
- Network policies
- RBAC configuration

---

## K8s STIG Key Requirements (High Impact)

The DISA Kubernetes STIG has ~100+ checks. These are the CAT I and most important CAT II items:

**API Server hardening:**
```yaml
# kube-apiserver manifest flags (kubeadm: /etc/kubernetes/manifests/kube-apiserver.yaml)
spec:
  containers:
  - command:
    - kube-apiserver
    - --anonymous-auth=false                          # V-242381 CAT I: No anonymous access
    - --audit-log-path=/var/log/kubernetes/audit.log  # V-242402 CAT II: Audit logging
    - --audit-log-maxage=30                           # V-242403: Retention
    - --audit-log-maxbackup=10
    - --audit-log-maxsize=100
    - --audit-policy-file=/etc/kubernetes/audit-policy.yaml
    - --authorization-mode=Node,RBAC                  # V-242388: Not AlwaysAllow
    - --client-ca-file=/etc/kubernetes/pki/ca.crt
    - --disable-admission-plugins=AlwaysAdmit         # V-242386: No AlwaysAdmit
    - --enable-admission-plugins=NodeRestriction,PodSecurity
    - --encryption-provider-config=/etc/kubernetes/encryption-config.yaml  # V-242397: etcd encryption
    - --kubelet-certificate-authority=/etc/kubernetes/pki/ca.crt
    - --kubelet-client-certificate=/etc/kubernetes/pki/apiserver-kubelet-client.crt
    - --kubelet-client-key=/etc/kubernetes/pki/apiserver-kubelet-client.key
    - --profiling=false                               # V-242389: Disable profiling
    - --request-timeout=300s
    - --service-account-issuer=https://kubernetes.default.svc
    - --service-account-key-file=/etc/kubernetes/pki/sa.pub
    - --service-account-signing-key-file=/etc/kubernetes/pki/sa.key
    - --tls-cipher-suites=TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
    - --tls-min-version=VersionTLS12
```

**etcd encryption at rest (V-242397 — CAT I):**
```yaml
# /etc/kubernetes/encryption-config.yaml
apiVersion: apiserver.config.k8s.io/v1
kind: EncryptionConfiguration
resources:
  - resources:
    - secrets
    providers:
    - aescbc:
        keys:
        - name: key1
          secret: [base64-encoded-32-byte-key]  # Use FIPS-approved AES-256
    - identity: {}  # Fallback for reading unencrypted data
```

**Audit policy (V-242402):**
```yaml
# /etc/kubernetes/audit-policy.yaml
apiVersion: audit.k8s.io/v1
kind: Policy
rules:
  # Log secrets access (detect credential theft)
  - level: Metadata
    resources:
    - group: ""
      resources: ["secrets"]
  # Log exec, attach, portforward (detect lateral movement)
  - level: RequestResponse
    verbs: ["create"]
    resources:
    - group: ""
      resources: ["pods/exec", "pods/attach", "pods/portforward"]
  # Log node auth changes
  - level: RequestResponse
    resources:
    - group: "rbac.authorization.k8s.io"
      resources: ["clusterroles", "clusterrolebindings", "roles", "rolebindings"]
  # Log changes to workloads
  - level: RequestResponse
    verbs: ["create", "update", "patch", "delete"]
    resources:
    - group: ""
      resources: ["pods", "services", "configmaps"]
    - group: "apps"
      resources: ["deployments", "daemonsets", "statefulsets"]
  # Minimal logging for everything else
  - level: Metadata
```

**Pod Security Standards (V-245541 and Container Platform SRG):**
```yaml
# Namespace-level Pod Security admission (K8s v1.25+)
# This replaces Pod Security Policies (deprecated)
apiVersion: v1
kind: Namespace
metadata:
  name: [your-app-namespace]
  labels:
    pod-security.kubernetes.io/enforce: restricted   # Strictest level
    pod-security.kubernetes.io/enforce-version: latest
    pod-security.kubernetes.io/audit: restricted
    pod-security.kubernetes.io/warn: restricted
```

For `restricted` profile, pods must:
- Run as non-root (`runAsNonRoot: true`)
- Have read-only root filesystem (`readOnlyRootFilesystem: true`)
- Drop all capabilities (`capabilities: drop: ["ALL"]`)
- Not run privileged (`privileged: false`)
- Set `allowPrivilegeEscalation: false`
- Specify seccomp profile (`seccompProfile.type: RuntimeDefault`)

**RBAC — Least Privilege (AC-6):**
```yaml
# Example: Application service account with minimal permissions
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: app-service-role
  namespace: [your-namespace]
rules:
  - apiGroups: [""]
    resources: ["configmaps"]
    verbs: ["get", "list"]   # Only what the app needs; no create/update/delete
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: app-service-binding
  namespace: [your-namespace]
subjects:
  - kind: ServiceAccount
    name: [app-service-account]
roleRef:
  kind: Role
  name: app-service-role
  apiGroup: rbac.authorization.k8s.io
```

**Disable auto-mount of service account tokens:**
```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: [app-service-account]
  namespace: [your-namespace]
automountServiceAccountToken: false  # Only enable for SAs that need K8s API access
```

---

## Container Security Stack (Non-P1)

Without Twistlock/Prisma from P1, you need to build the security stack yourself:

**Image scanning:**
```bash
# Trivy (open source, widely used in DoD non-P1 environments)
# CI/CD integration — scan before push to registry
trivy image --exit-code 1 --severity CRITICAL,HIGH [image-ref]

# In-cluster scanning via Trivy Operator
kubectl apply -f https://raw.githubusercontent.com/aquasecurity/trivy-operator/v[VERSION]/deploy/static/trivy-operator.yaml
# Generates VulnerabilityReport and ConfigAuditReport custom resources

# Grype (Anchore)
grype [image-ref] --fail-on critical
```

**Image signing (required for DoD — integrity of images):**
```bash
# Cosign (CNCF project, used in P1 and elsewhere)
# Sign on push:
cosign sign --key cosign.key registry.example.com/[image]:[tag]

# Verify on pull (via Kyverno policy):
```
```yaml
# Kyverno ClusterPolicy for image signature verification
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: verify-image-signatures
spec:
  validationFailureAction: Enforce
  rules:
    - name: verify-cosign-signature
      match:
        resources:
          kinds: ["Pod"]
      verifyImages:
        - imageReferences: ["registry.example.com/*"]
          attestors:
            - entries:
                - keys:
                    publicKeys: |-
                      -----BEGIN PUBLIC KEY-----
                      [your-cosign-public-key]
                      -----END PUBLIC KEY-----
```

**mTLS without Istio (options):**

*Linkerd (lighter weight than Istio):*
```bash
linkerd install --crds | kubectl apply -f -
linkerd install | kubectl apply -f -
# Annotate namespace for automatic mTLS injection:
kubectl annotate namespace [your-ns] linkerd.io/inject=enabled
```

*Cilium (with Hubble for observability):*
```bash
helm install cilium cilium/cilium --version [version] \
  --namespace kube-system \
  --set kubeProxyReplacement=strict \
  --set authentication.mutual.spiffe.enabled=true  # mTLS via SPIFFE/SPIRE
```

*cert-manager for PKI (if no service mesh):*
```bash
# cert-manager + SPIFFE for mTLS between services
helm install cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --set installCRDs=true \
  --set featureGates="ExperimentalGatewayAPISupport=true"
# Issue short-lived certificates for each service (automatic rotation)
```

**Runtime security:**
```yaml
# Falco DaemonSet for runtime anomaly detection (SI-4)
# Detects: shell spawned in container, file writes to sensitive directories,
#          privilege escalation, unexpected network connections

helm install falco falcosecurity/falco \
  --namespace falco \
  --create-namespace \
  --set falco.grpc.enabled=true \
  --set falco.grpcOutput.enabled=true

# Key Falco rules to enable:
# - shell in container (exec of sh/bash)
# - write below etc in container
# - read sensitive file trusted after startup
# - container run as root
```

**Network policies (SC-7 at K8s layer):**
```yaml
# Default deny all — apply to every namespace
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: [your-namespace]
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress
---
# Explicit allow — only what's needed
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-app-to-db
  namespace: [your-namespace]
spec:
  podSelector:
    matchLabels:
      role: database
  ingress:
  - from:
    - podSelector:
        matchLabels:
          role: app
    ports:
    - protocol: TCP
      port: 5432
```

---

## Authentication for Non-P1 K8s (No Keycloak Pre-built)

You need to implement CAC/PIV authentication. Options:

**Option 1: Keycloak (self-managed)**
Deploy Keycloak in your cluster:
```bash
helm install keycloak bitnami/keycloak \
  --namespace identity \
  --set auth.adminUser=admin \
  --set postgresql.enabled=true
# Configure DoD PKI as Identity Provider (SAML 2.0 or OIDC)
# Import DoD Root CA certificates to Keycloak trust store
# Create realm for your app
# Configure X.509 Certificate Authentication in realm
```

**Option 2: Dex + Gangway (Kubernetes native OIDC)**
```yaml
# Dex for OIDC federation
# Configure kube-apiserver with:
- --oidc-issuer-url=https://dex.your-cluster.example.com
- --oidc-client-id=kubernetes
- --oidc-username-claim=email
- --oidc-groups-claim=groups
- --oidc-ca-file=/etc/kubernetes/dex-ca.crt
```

**Option 3: External ADFS integration (if AD environment nearby)**
```
Users authenticate to ADFS → ADFS issues SAML assertion →
Keycloak/Dex acts as SAML-to-OIDC bridge → K8s OIDC auth
```

For all options: certificates must chain to DoD Root CA (not self-signed for production).

---

## ATO Day-by-Day for Non-P1 K8s

### Day 1: Cluster Hardening, Scans, Registration

**0800-1000: Apply K8s STIG (API server, etcd, kubelet)**
Apply all kube-apiserver flags from above. Apply kubelet hardening:
```yaml
# kubelet-config.yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
authentication:
  anonymous:
    enabled: false       # V-242381 equivalent for kubelet
  webhook:
    enabled: true
authorization:
  mode: Webhook
protectKernelDefaults: true    # V-245543
readOnlyPort: 0                # V-242399 CAT I: disable read-only port
```

**1000-1200: Apply Node OS STIG**
Run SCAP/SCC against node OS (RHEL/Ubuntu); apply remediation as described in `disa-hosting.md`.

**1200-1400: Deploy Security Stack**
- Deploy Falco (runtime detection)
- Deploy Trivy Operator (image scanning)
- Deploy Kyverno (policy enforcement: image signing, pod security)
- Apply Network Policies (default deny all)
- Deploy SIEM log forwarder (Fluent Bit → Elasticsearch/Splunk)

**1400-1600: Configure Audit Logging**
```bash
# Verify audit logging is working
kubectl get pod -n kube-system -l component=kube-apiserver
kubectl logs [apiserver-pod] | grep "audit"

# Ensure audit log is being collected by Fluent Bit or equivalent
# Audit log path: /var/log/kubernetes/audit.log (per kube-apiserver config above)
```

**1600-1700: FIPS 199 + eMASS Registration + Boundary Diagram**

### Day 2: SSP Writing, Scan Processing

**0800-0900: Review Trivy Operator + Falco Findings**
```bash
# Check Trivy VulnerabilityReports
kubectl get vulnerabilityreports -A
kubectl describe vulnerabilityreport [name] -n [namespace]

# Check ConfigAuditReports
kubectl get configauditreports -A

# Review Falco alerts (via Falco logs or Falco Sidekick)
kubectl logs -n falco -l app=falco --tail=100
```

**0900-1700: SSP Narratives**

Non-P1 K8s priority order:

1. **SC-7 (Boundary Protection)**:
   "Network boundary protection is implemented at the Kubernetes cluster level through Kubernetes NetworkPolicy objects in the default-deny-all configuration applied to all application namespaces. Explicit allow policies permit only documented service-to-service communication paths (see data flow diagram). The Kubernetes API server is not publicly accessible; access is restricted to [authorized admin CIDR ranges] via Kubernetes RBAC. Node-level network protection is provided by [Calico/Cilium/Flannel] CNI with host-firewall rules. Cluster ingress is via [Nginx/HAProxy/ALB] Ingress Controller with TLS termination enforced."

2. **SC-8/SC-8(1) (Transmission Protection)**:
   If using Linkerd: "Service-to-service communication is encrypted via Linkerd service mesh with automatic mutual TLS (mTLS) injection for all annotated namespaces. All inter-service traffic is MTLS-encrypted with SPIFFE/SPIRE-issued certificates rotated every 24 hours. External traffic terminates TLS at the Ingress Controller (TLS 1.3, FIPS-compliant ciphers). No plaintext service communication is permitted; verified by Linkerd network policy audit."

   If using cert-manager only: "All services use TLS 1.3 for communication. Certificates are issued by cert-manager backed by [internal CA / HashiCorp Vault PKI]. Certificate rotation is automated every [30/90] days. Service-to-service mTLS is enforced by [Istio/Linkerd/Cilium mTLS policy]. Evidence: cert-manager certificate renewal logs."

3. **IA-2 (Authentication)**:
   "User authentication to [System Name] is provided by [Keycloak/Dex] integrated with DoD PKI for CAC/PIV authentication. All interactive user sessions require certificate-based authentication using a certificate issued by DoD PKI and validated against DoD Root CA [3/4/5]. Username/password authentication is disabled. Kubernetes API server authentication uses OIDC tokens issued by [Keycloak/Dex]. Service-to-service authentication uses mTLS with SPIFFE-issued SVIDs (no static credentials for inter-service auth)."

4. **CM-6 (Configuration Settings)**:
   "Kubernetes cluster configuration is hardened per DISA Kubernetes STIG V[X.X]. API server flags are documented in the attached kube-apiserver manifest. SCAP assessment against the Kubernetes STIG SCAP content (from DISA) shows [X]% compliance; CAT I: [N]; CAT II: [N]. Pod Security Standards at 'restricted' level are enforced via PodSecurity admission controller for all application namespaces. Node OS hardening: [RHEL 8 STIG V1R14] applied; SCC compliance [X]%. Kyverno ClusterPolicies enforce: image signature verification, no privileged containers, non-root user enforcement, read-only root filesystem. Policy violations block pod creation (enforce mode)."

5. **AU-2/AU-6 (Audit Logging)**:
   "Kubernetes API audit logging is enabled with audit policy targeting security-sensitive operations (secrets access, exec/attach, RBAC changes, workload mutations). Audit logs are written to /var/log/kubernetes/audit.log on control plane nodes and collected by Fluent Bit, forwarded to [Elasticsearch/Splunk] with 90-day retention. Node-level logs (auditd, kubelet logs, container runtime logs) are similarly collected. Falco generates real-time security alerts for anomalous runtime behavior (shell in container, unexpected file writes, privilege escalation) forwarded to [Slack/PagerDuty/SIEM]. ISSO reviews SIEM security dashboards [daily/weekly]."

6. **SI-3/SI-4 (Malware Protection and Monitoring)**:
   "Container image scanning is performed by Trivy Operator deployed in-cluster, which continuously scans all running container images and generates VulnerabilityReports as Kubernetes custom resources. Critical/High CVEs trigger alerts via [Prometheus AlertManager / Falco Sidekick]. Falco provides runtime threat detection: anomalous process execution, unexpected network connections, container escape attempts. Falco rules are updated from upstream (weekly or per security advisory). Evidence: Trivy VulnerabilityReport exports; Falco event logs."

### Day 3: Final Scans, Package, Submit

Standard Day 3 process:
- Final Trivy + ACAS (node-level) scan export
- SCC results for node OS
- K8s STIG SCAP results (if applicable SCAP content exists for K8s)
- eMASS package assembly
- AO briefing

---

## Non-P1 K8s ATO Failure Modes

**Failure 1: etcd not encrypted at rest**
- Symptom: Kubernetes STIG V-242397 (CAT I) fails; etcd stores Secrets in plaintext
- Impact: SC-28 Critical finding; all Kubernetes Secrets (tokens, API keys, passwords) are unencrypted
- Fix: Deploy encryption-config.yaml (example above); run `kubectl get secrets -A -o yaml` through the API after enabling — they should show as encrypted in etcd

**Failure 2: Anonymous API server access enabled**
- Symptom: `kubectl --anonymous-auth=true` or default setting not explicitly disabled; V-242381 CAT I
- Impact: Unauthenticated API access possible; AC-3, IA-2 Critical findings
- Fix: `--anonymous-auth=false` in kube-apiserver flags; verify with `curl -k https://[api-server]:6443/api/v1/namespaces` returns 403 Unauthorized, not data

**Failure 3: Privileged containers running in production**
- Symptom: pods with `privileged: true` or `allowPrivilegeEscalation: true`
- Impact: Container escape risk; SI-3, AC-6 findings; blocks ATO for new deployments
- Fix: Enforce PodSecurity `restricted` standard; if app requires elevated privileges, document and accept risk with specific Kyverno exception

**Failure 4: No image signing / any-registry pull allowed**
- Symptom: Pods pulling images from docker.io, ghcr.io, or unsigned registries
- Impact: SA-10, SI-7 findings; supply chain integrity concern
- Fix: Deploy Kyverno/Sigstore policy controller requiring all images to be signed; restrict pull to approved registry via Kyverno ClusterPolicy

**Failure 5: Cluster-admin ServiceAccounts**
- Symptom: Application pods running with service account that has cluster-admin ClusterRoleBinding
- Impact: AC-6 (least privilege) Critical finding; compromise of one pod = full cluster access
- Fix: Audit with `kubectl get clusterrolebindings -o json | jq '.items[] | select(.roleRef.name=="cluster-admin")'`; remove all non-essential cluster-admin bindings

**Failure 6: No default deny NetworkPolicy**
- Symptom: Pods can communicate freely within cluster (no NetworkPolicy applied)
- Impact: SC-7 finding; lateral movement in event of compromise
- Fix: Apply default-deny-all NetworkPolicy to all namespaces; then add explicit allow policies

**Failure 7: Audit logs not shipped off-node**
- Symptom: Audit logs stored only on control plane node local disk; not in SIEM
- Impact: AU-9 (audit protection) and AU-6 (review) findings; local logs can be tampered with or lost
- Fix: Configure Fluent Bit to read /var/log/kubernetes/audit.log and forward to SIEM; verify log ingestion in SIEM

**Failure 8: Kubelet read-only port open (V-242399 — CAT I)**
- Symptom: kubelet running with `--read-only-port=10255` (default in some older configs)
- Impact: Unauthenticated access to pod/node metadata
- Fix: `readOnlyPort: 0` in kubelet config; verify with `curl http://[node-ip]:10255` returns connection refused

---

## K8s Security Scanning Quick Reference

| Tool | What It Scans | When to Run | Output for ATO |
|------|-------------|------------|---------------|
| `kube-bench` (CIS Kubernetes Benchmark) | K8s component configuration | Daily in CI; before ATO | JSON/HTML compliance report |
| SCAP/SCC + DISA K8s STIG content | DISA STIG checks | Weekly; before ATO | XCCDF ARF for eMASS |
| Trivy Operator | Container images + K8s objects | Continuous | VulnerabilityReport CR; export for POA&M |
| Falco | Runtime anomalies | Continuous | SIEM alerts |
| `kubectl-who-can` | RBAC audit | Before ATO; quarterly | Privileges report for AC-6 evidence |
| ACAS (node-level) | Node OS vulnerabilities | Monthly | Nessus results for eMASS |
| SCC | Node OS STIG | Monthly | XCCDF ARF for eMASS |

```bash
# kube-bench (CIS Benchmark assessment — fast, runs as a Job)
kubectl apply -f https://raw.githubusercontent.com/aquasecurity/kube-bench/main/job.yaml
kubectl logs job/kube-bench

# kubectl-who-can (RBAC audit)
kubectl-who-can get secrets -n [namespace]  # Who can read secrets?
kubectl-who-can exec pods -n [namespace]    # Who can exec into pods?
kubectl-who-can create pods -n [namespace]  # Who can create pods?
```
