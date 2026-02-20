# Platform One (P1) / Cloud One / Big Bang / Iron Bank — ATO Playbook

Platform One is the fastest path to a DoD ATO for cloud-native applications. When used correctly, it reduces your residual control count by roughly half and gives you a pre-built security toolchain. When used incorrectly, it gives you false confidence and an AO rejection.

---

## What Platform One Is

**Platform One (P1)**: Managed by Air Force Life Cycle Management Center (AFLCMC/HNA) at Hanscom AFB.

**Three-layer architecture:**
```
Iron Bank                 ← Layer 3: Hardened container image registry (repo1.dso.mil)
Big Bang                  ← Layer 2: Hardened Kubernetes platform (CNCF-compliant, STIG-hardened)
Cloud One                 ← Layer 1: IaaS infrastructure on AWS GovCloud (DISA IL4/IL5 PA)
```

**Who holds what ATO:**
- Cloud One infrastructure ATO: DISA Provisional Authorization + AWS FedRAMP High
- Platform One ATO: P1 CTSO (under AFLCMC authorization chain)
- YOUR app: You get your own ATO; you leverage P1 as inherited infrastructure

**Supported ILs:** IL2, IL4, IL5 (IL5 on dedicated Cloud One capacity)

---

## Required Conditions for P1 Inheritance to Apply

If you skip any of these, you CANNOT claim P1 inheritance in your SSP. The AO will catch it.

**1. All container images must come from Iron Bank (repo1.dso.mil)**
- No Docker Hub, no GHCR, no ECR public — only Iron Bank approved images
- Iron Bank images are pre-scanned by Twistlock/Prisma; P1 CTSO maintains them
- Your Dockerfile base image: must start FROM an Iron Bank approved image (repo1.dso.mil/ironbank/...)
- How to verify: run `kubectl get pods -n [your-namespace] -o jsonpath='{.items[*].spec.containers[*].image}'` and confirm all are from repo1.dso.mil

**2. Istio service mesh must be deployed in STRICT mTLS mode**
- Big Bang deploys Istio by default; do not disable it
- PeerAuthentication resource must be set to `mtls.mode: STRICT` for your namespace (not PERMISSIVE)
- If you set any PeerAuthentication to PERMISSIVE, SC-8(1) inheritance is void
- How to verify: `kubectl get peerauthentication -A`; any PERMISSIVE mode is a finding

**3. Authenticate through P1 Keycloak (SSO)**
- Your app must federate authentication through P1's Keycloak instance for interactive user logins
- CAC/PIV enforcement happens in Keycloak — this is how IA-2(1)/(2) inheritance works
- Do not implement a separate authentication system bypassing Keycloak for human users
- Service-to-service authentication: use mTLS (Istio handles) or Vault-issued tokens

**4. Use Big Bang components — do not disable security components**
- Big Bang comes with Kyverno/Gatekeeper, Twistlock, Istio, Keycloak, logging stack
- Do not disable these for convenience — each one satisfies specific inherited controls
- If a Big Bang component is not yet configured for your app, document it as a gap, not absent
- Adding your own tools on TOP of Big Bang is fine; replacing Big Bang tools requires P1 CTSO approval

**5. Deploy through approved CI/CD pipeline (typically GitLab on P1)**
- P1 provides GitLab CI/CD; use it (or equivalent P1-approved pipeline)
- This satisfies SA-10 (developer configuration management) and CM-3 (configuration change control)
- Manual kubectl apply to production = violation of CM-3; will be a finding

**6. Register your system intake with P1 CTSO before deploying**
- P1 has a formal onboarding process: System Intake → P1 Jira
- P1 CTSO reviews your intake and assigns a namespace on Cloud One
- Without an approved intake, you are NOT authorized to operate on P1 — unauthorized system

---

## Platform One ATO Process (Step-by-Step)

### Pre-Day-1: Get Access

Before the sprint starts, you need:
- [ ] P1 Jira access (jira.il2.dso.mil or jira.il4.dso.mil — IL-appropriate)
- [ ] Iron Bank account (registry1.dso.mil — for pulling images)
- [ ] P1 CTSO contact point (team lead or P1 onboarding POC)
- [ ] eMASS tenant decision (Air Force eMASS for most; Army/Navy eMASS for their programs)
- [ ] Cloud One instance type: Shared (IL4) or Dedicated (IL5)

### Day 1 — Intake, Boundary, Scans

**0800-0900: Submit P1 System Intake**
- Complete P1 System Intake form in P1 Jira
- Required fields: System name, mission description, IL target, namespace request, ISSO info, data types
- P1 CTSO will review; initial response typically within 24-48 hours (check P1 Jira status)

**0900-1100: Build Authorization Boundary Diagram**
- Show your app's components: pods/containers, databases, external integrations, users
- Show the P1 boundary: your namespace is INSIDE P1; show the P1 boundary wrapping it
- Label: "Cloud One / AWS GovCloud provides infrastructure; P1 Big Bang provides platform; [Your App] operates within this boundary"
- This diagram structure is what the AO expects to see for a P1-hosted app

**1100-1300: FIPS 199 Categorization**
- Identify your data types and map to impact levels
- Document with mission owner sign-off (email approval is acceptable)
- Enter in eMASS under categorization tab

**1300-1400: Register System in eMASS**
- Register in appropriate eMASS tenant
- System type: Major IS or Minor IS (based on user count and mission criticality)
- Import P1/Cloud One control baseline (contacts P1 CTSO for current eMASS package ID to reference)

**1400-1600: Get and Populate CRM**
- Download P1 CRM from P1 Confluence (accessible via P1 Jira) or request from P1 CTSO
- CRM lists ~120-150 controls marked Inherited; ~50-80 marked Shared; remainder Residual
- Review CRM for Shared controls: these require YOUR narrative in the SSP documenting how you configured the shared capability

**1600-1700: Kick Off Twistlock / Prisma Scans**
- Twistlock is deployed by Big Bang; scan your running container images
- Navigate to Twistlock console (deployed in Big Bang namespace)
- Trigger full scan of all images in your registry and running in your namespace
- Let scans run overnight; review results Day 2 morning

### Day 2 — Write SSP, Process Scans

**0800-0900: Review Twistlock Scan Results**
- Open Twistlock dashboard; filter to Critical and High CVEs
- For each Critical/High: determine if Iron Bank has a patched version; update if so
- Open findings become POA&M entries with 30-day (Critical) or 30-day (High) remediation timelines
- Export scan results for eMASS upload (Twistlock exports to CSV/PDF)

**0900-1700: Write SSP Narratives (Tier 1 → Tier 2 → Tier 3)**

*Priority order for P1 apps:*

1. **SSP System Overview** (PL-2): 500-1000 word description of the system, its mission, its users, its data, its deployment on P1
2. **RA-2**: FIPS 199 categorization rationale (paste your Day 1 FIPS 199 work)
3. **SC-7**: Boundary protection — describe your namespace isolation, Istio NetworkPolicy, ingress gateway config; reference P1 inheritance for infrastructure boundary
4. **IA-2**: Authentication — describe Keycloak integration, CAC/PIV flow, MFA enforcement; reference P1 Keycloak inheritance
5. **AC-2**: Account management — YOUR user lifecycle (how accounts are requested, approved, created in Keycloak, reviewed quarterly, terminated)
6. **AU-6**: Audit review — YOUR log review process using P1 EFK/PLG; who reviews, how often, what triggers escalation
7. **CA-7**: ConMon — reference ConMon plan outline; Twistlock scans weekly, POA&M updates monthly
8. **CM-6**: Configuration settings — reference Big Bang STIG-hardened K8s defaults; your app-specific config hardening (no debug mode in prod, no default credentials, etc.)
9. **SI-2**: Flaw remediation — your patch process; Iron Bank image update timeline; OS patching schedule; POA&M for Twistlock findings
10. **IR-6**: Incident reporting — your escalation chain; how you report to P1 CTSO and up to component CERT
11. **CP-2**: Contingency plan — app-layer recovery; how you restore from broken deployment; your RTO/RPO; K8s self-healing acknowledgment
12. **All AT, PS, PL, RA remaining controls** — typically these are policy/procedure narratives; use org-standard language

**For all Shared controls (P1 CRM marks these):**
Pattern: "[P1 provides X capability via [Big Bang component]. [Your app] leverages this capability by [what you specifically configured]. Evidence: [configuration artifact]."

Example for SC-8: "Transmission confidentiality is provided through Istio service mesh deployed by Big Bang. All service-to-service communication within the [Your App] namespace uses mTLS with PeerAuthentication set to STRICT mode. Ingress to the namespace is via the P1 Istio ingress gateway with TLS 1.3 enforced. Evidence: PeerAuthentication manifest, Istio ingress gateway TLS configuration."

**For Inherited controls:**
Pattern: "Inherited from Platform One / Cloud One. See P1 CRM control [ID]."

**For Residual controls:**
Full narrative required. Write the Five W's: What does the control require? Who implements it? How is it implemented? When does it run / get reviewed? Where in the boundary does it apply?

### Day 3 — Complete Package, Submit

**0800-1000: Finalize POA&M**
- All Twistlock findings entered with realistic scheduled completion dates
- All Manual STIG check failures (if any) entered
- No blank "TBD" dates — use real dates
- POA&M reviewed by ISSM

**1000-1100: Assemble eMASS Package**
- All SSP narratives entered or uploaded in eMASS
- CRM uploaded and linked to inherited controls
- Scan results attached (Twistlock export, SCAP if any)
- POA&M current in eMASS
- System personnel (ISSO, ISSM, AO) assigned

**1100-1300: Write AO Briefing Deck**
Slide structure for P1 ATO brief (30 min):
1. System Overview (2 slides): What it does, who uses it, what data it handles
2. Authorization Boundary (1 slide): Your boundary diagram
3. Impact Level Rationale (1 slide): FIPS 199 values with rationale
4. P1 Inheritance (1 slide): "P1 covers X controls; we own Y residual controls"
5. Open Findings (1 slide): Twistlock findings + POA&M milestones; no Critical unmitigated
6. ConMon Plan (1 slide): Scanning, POA&M updates, review schedule
7. Risk Statement (1 slide): What risks remain; your acceptance rationale
8. Request for Authorization (1 slide): ATO vs. IATO recommendation; duration requested

**1300-1400: ISSM Review Pass**
- ISSM reviews complete package
- ISSM endorses in eMASS
- Package submitted to AO queue in eMASS

**1400-1500: Schedule AO Meeting**
- Contact AO's office for review meeting (1-5 business days out depending on AO availability)
- Share briefing deck 24 hours before meeting
- P1 CTSO may need to be on the call for platform-level questions

---

## Iron Bank Deep Dive

**What Iron Bank is**: DoD's approved container image repository, hosted at registry1.dso.mil. FOSS images are hardened, scanned, and re-published from Iron Bank.

**Access**: CAC required; register at repo1.dso.mil (NIPRNet access or approved VPN)

**Image naming convention**: `registry1.dso.mil/ironbank/<vendor>/<product>:<version>`
Examples:
- `registry1.dso.mil/ironbank/redhat/ubi/ubi8:8.9`
- `registry1.dso.mil/ironbank/opensource/nginx/nginx:1.25`
- `registry1.dso.mil/ironbank/opensource/postgres/postgresql:16.2`

**What Iron Bank provides per image:**
- Base STIG compliance (OS and application STIGs applied)
- Twistlock scan results (published with each image)
- SBOM (software bill of materials)
- Signed with Cosign for integrity verification

**How to check if an image is Iron Bank approved:**
1. Search repo1.dso.mil for the image name
2. Check the Twistlock scan results for the specific version
3. Review the STIG Viewer results (published alongside image)

**Iron Bank images with open CVEs:**
- Not all Iron Bank images are CVE-free — some CVEs are unavoidable at runtime
- Acceptable practice: POA&M entries for Iron Bank CVEs reference Iron Bank issue tracker
- Your POA&M entry: "CVE-XXXX-XXXX in [image] v[X.X]: Open in Iron Bank. Tracking issue [link]. Expected remediation: [date per Iron Bank milestone]."
- You are NOT responsible for Iron Bank's CVEs; you ARE responsible for documenting and tracking them

**If no Iron Bank image exists for your software:**
- Submit a hardening request to Iron Bank (ironbank.dso.mil/onboarding — DoD Jira account required)
- Process takes 2-8 weeks
- Interim option: build your own hardened image using an Iron Bank base + your application layer; submit for Iron Bank review; document deviation with P1 CTSO

---

## Big Bang Component → NIST Control Mapping

Understanding which Big Bang component satisfies which controls is essential for writing accurate Shared control narratives.

| Big Bang Component | NIST Controls Supported | Your Responsibility |
|-------------------|------------------------|---------------------|
| **Istio** (service mesh) | SC-7(4)(5)(7), SC-8/SC-8(1), AC-4, AC-3(9) | Set STRICT mTLS; write AuthorizationPolicies for your APIs |
| **Keycloak** (identity/SSO) | IA-2(1)(2)(8), IA-5(1)(2), IA-8(1)(2)(4) | Configure realm; federate your app's user store; enforce CAC |
| **Twistlock/Prisma** (container security) | SI-3(1)(2), SI-2(2), SI-7(1) | Review scan results; update images; enter findings in POA&M |
| **EFK/PLG stack** (logging) | AU-2, AU-3, AU-8, AU-9, AU-12 | Configure app log aggregation; set up alerts for your app events |
| **Kyverno/Gatekeeper** (policy) | CM-7, SC-3, SA-11 | Write policies for your specific pod security requirements |
| **Vault** (secrets) | IA-5(1)(7), SC-12, SA-9(6) | Store all credentials in Vault; no plaintext secrets in manifests |
| **GitLab** (CI/CD) | SA-10(1), CM-3, CM-5, SI-6 | Use GitLab for all deployments; enforce branch protection; require MR approvals |
| **ArgoCD** (GitOps) | CM-3(1), CM-5(2) | All production changes via GitOps; no out-of-band changes |
| **Prometheus/Grafana** (monitoring) | SI-4(2)(7), AU-6 | Configure dashboards for your app metrics; set up alerts |
| **cert-manager** | SC-12, SC-17 | Automate certificate rotation; tie to DoD PKI |

---

## Common P1 ATO Failure Modes

**Failure 1: Istio mTLS not in STRICT mode**
- Symptom: PeerAuthentication shows PERMISSIVE for application namespace
- Impact: SC-8(1) inheritance claim is invalid; AO or SCA discovers it during review
- Fix: Apply `PeerAuthentication` with `mtls.mode: STRICT` to all application namespaces; verify with `istioctl x describe pod [pod-name]`

**Failure 2: Non-Iron Bank images in production**
- Symptom: Twistlock shows images from docker.io, ghcr.io, or private registries
- Impact: SI-3 inheritance void; P1 CTSO may suspend namespace; AO finding
- Fix: Rebuild all Dockerfiles with Iron Bank base images; update all image references in Helm charts

**Failure 3: Claiming P1 inheritance without an approved system intake**
- Symptom: System is running on P1 but no formal intake was submitted/approved
- Impact: Your system is unauthorized; no legal basis for inheritance claim
- Fix: Submit system intake immediately; get P1 CTSO approval; document in SSP

**Failure 4: CAC not enforced end-to-end (soft CAC)**
- Symptom: Keycloak is configured but allows username/password as fallback; or CAC only enforced at front door but not for admin panels
- Impact: IA-2(1)/(2) inheritance void; all human authentication must go through CAC
- Fix: Disable all non-CAC authentication flows for human users in Keycloak; verify with test account

**Failure 5: Shared controls documented as inherited**
- Symptom: SSP marks IA-2 as "Inherited from P1" with no app-specific narrative
- Impact: SCA notes that P1 provides Keycloak but YOU must configure it; your app-level IA-2 has no evidence
- Fix: For every Shared control in the CRM, write both sides: "P1 provides [X]. This system leverages it by [Y]. Evidence: [Z]."

**Failure 6: ISSO not familiar with P1 toolchain**
- Symptom: POA&M has no Twistlock findings because ISSO hasn't accessed the dashboard
- Impact: Scans are happening but not being reviewed; AU-6 and SI-2 findings during assessment
- Fix: Mandatory Day 1 access to Twistlock console, EFK dashboard, and P1 Jira for the ISSO

**Failure 7: P1 CRM version mismatch**
- Symptom: ISSO is using a CRM from 2 years ago; P1 ATO has been updated; controls differ
- Impact: Inheritance claims reference controls that P1 no longer covers under current ATO
- Fix: Always get the current CRM from P1 CTSO; check P1 Confluence for last update date

**Failure 8: Service accounts with default tokens**
- Symptom: Kubernetes service accounts use auto-mounted default service account tokens
- Impact: AC-6 (least privilege) finding; service accounts can call K8s API with default permissions
- Fix: Set `automountServiceAccountToken: false` in all pod specs; use projected tokens with audience and expiry for service accounts that legitimately need K8s API access

---

## P1 Quick Reference

| Item | Value |
|------|-------|
| Iron Bank registry | `registry1.dso.mil` |
| P1 Jira (IL4) | `jira.il4.dso.mil` |
| P1 documentation | `confluence.il4.dso.mil` |
| P1 onboarding | `jira.il4.dso.mil` → submit System Intake ticket |
| CTSO contact | via P1 Jira (submit ticket; don't rely on email) |
| Big Bang source | `repo1.dso.mil/platform-one/big-bang/bigbang` |
| IL target for dedicated infra | Cloud One Dedicated (submit dedicated capacity request to P1 CTSO) |
| Scan tool in platform | Twistlock/Prisma Cloud (access via Big Bang-deployed console) |
| Log access | EFK/PLG deployed in `logging` namespace; access via Kibana/Grafana |
| ConMon scan schedule | Twistlock runs continuously; configure weekly full scans |
