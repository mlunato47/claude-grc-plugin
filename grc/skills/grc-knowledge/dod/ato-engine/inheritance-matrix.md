# Inheritance Matrix: Platform × Impact Level → Control Ownership

Reference for the ATO acceleration engine. For each platform and Impact Level combination, this file defines what is **inherited** (platform's ATO covers it), **shared** (platform provides capability; you must configure it), and **residual** (entirely your responsibility).

Understanding this matrix is the single biggest accelerator: teams that don't know their inheritance waste days documenting controls the platform already covers.

---

## How DoD Control Inheritance Works

The inheritance model follows a layered ATO structure:

1. **CSP infrastructure ATO** (AWS GovCloud FedRAMP High P-ATO, Azure Government FedRAMP High, etc.) — covers physical, environmental, and some logical infrastructure controls
2. **Platform ATO** (Platform One Cloud One ATO, DISA MilCloud ATO, etc.) — covers OS hardening, container runtime, network fabric, identity integration
3. **Mission App ATO** — covers the application itself: its logic, users, data flows, change management, policies, and training

Each layer builds on the one below. Your SSP says: "Control X is inherited from [Platform]. See [Platform] CRM." You don't write implementation narratives for inherited controls — only for residual ones.

**Conditions for inheritance to apply:**
- You must actually USE the platform's capability (can't claim Istio mTLS inheritance if you bypassed Istio)
- You must reference the platform's ATO by package ID in your CRM
- The platform's ATO must be current (not expired)
- You must operate within the platform's authorization boundary (can't deploy outside it)

---

## Platform One (P1) / Cloud One at IL4 and IL5

**Platform**: Platform One (P1) / Cloud One, managed by AFLCMC/HNA
**Underlying infrastructure**: AWS GovCloud (Cloud One)
**Platform ATO holder**: P1 CTSO (Cloud Transformation and Support Organization)
**Supported ILs**: IL2, IL4, IL5 (IL5 on dedicated Cloud One infrastructure)
**NIST baseline at IL4**: High (~392 controls); at IL5: High + NSS overlay

### What Platform One Inherits for Your App

**PE — Physical and Environmental Protection (18 controls): FULL INHERITANCE**
AWS GovCloud + DISA data center controls cover all physical/environmental requirements.
- PE-1 through PE-20: Fully covered by AWS/Cloud One infrastructure ATO
- Your CRM entry: "Inherited from Cloud One/AWS GovCloud infrastructure. See Cloud One CRM."

**MA — Maintenance (6 controls): FULL INHERITANCE**
- MA-1 through MA-6: Physical maintenance of cloud infrastructure is AWS's responsibility
- Your residual: Only if you add physical hardware to the environment (edge nodes, etc.)

**MP — Media Protection (9 controls): PARTIAL**
- Inherited: MP-2 (physical media access), MP-4 (physical storage), MP-5 (media transport), MP-6 (media sanitization for hardware retirement), MP-7 (media use at infra level)
- Your residual: MP-1 (media protection policy), MP-3 (media marking for data you generate)

**SC — System and Communications Protection (partially inherited):**
Inherited through Istio service mesh + AWS infrastructure:
- SC-5 (DoS protection): Inherited — AWS Shield + Istio rate limiting
- SC-7(4)/(5)/(7)/(8) (boundary sub-controls): Inherited via Istio ingress gateway + Kubernetes NetworkPolicy
- SC-8 / SC-8(1) (transmission confidentiality/integrity): Inherited — Istio mTLS in STRICT mode covers service-to-service; AWS TLS covers ingress. **Condition**: Istio PeerAuthentication must be set to STRICT, not PERMISSIVE.
- SC-12 (cryptographic key establishment): Inherited — AWS KMS handles key lifecycle
- SC-13 (cryptographic protection): Inherited — FIPS 140-2 validated modules in AWS FIPS endpoints; Istio uses FIPS-compliant TLS
- SC-17 (PKI certificates): Inherited — Platform One uses DoD PKI via Keycloak integration
- SC-20/SC-21/SC-22 (DNS security): Inherited at infrastructure level (AWS Route53 + CoreDNS on K8s)
- SC-28/SC-28(1) (protection at rest): Inherited — AWS KMS + EBS/EFS encryption at rest enabled by Cloud One
- SC-39 (process isolation): Inherited — Kubernetes namespace isolation + container runtimes

Not inherited from P1 (your residual for SC):
- SC-1 (communications protection policy): Your policy
- SC-2 (application partitioning): Your app's microservice design — K8s provides the mechanism but you design the separation
- SC-3 (security function isolation): Your specific isolation design within your namespace
- SC-4 (info in shared resources): Your responsibility for data in your namespace
- SC-7 (base control): Shared — P1 provides boundary at K8s level; you own your app's specific ingress rules and any additional boundaries you create

**AU — Audit and Accountability (partially inherited):**
Inherited through PLG/EFK stack:
- AU-2 (event logging): Inherited — Big Bang EFK/PLG collects K8s audit logs, container logs, control plane logs
- AU-3 (audit record content): Inherited — standard log format established by PLG/EFK
- AU-8 (time stamps): Inherited — synchronized to AWS NTP infrastructure
- AU-9 (audit record protection): Inherited — PLG/EFK with RBAC restricts log tampering
- AU-12 (audit generation): Inherited — logging agents on all nodes

Not inherited (your residual for AU):
- AU-1 (audit policy): Your policy document
- AU-6 (audit review, analysis, and reporting): **SHARED** — P1 provides the tool; you must actively review logs and create alerts for your app-specific events. AOs will test this.
- AU-11 (audit record retention): Shared — P1 retains platform logs; you must configure your app's log retention (90-day online minimum per NIST AU-11)

**IA — Identification and Authentication (partially inherited):**
Inherited through Keycloak + DoD PKI integration:
- IA-2(1)/(2) (network access MFA): Inherited — Keycloak enforces CAC/PIV for all interactive logins. **Condition**: Your app must federate to P1's Keycloak realm.
- IA-2(8) (replay-resistant authentication): Inherited — Keycloak + DoD PKI handles replay protection
- IA-3 (device identification): Inherited at infrastructure level
- IA-5(1)/(2) (authenticator management): Inherited — DoD PKI certificate lifecycle managed by P1/DEERS
- IA-8(1)/(2)/(4) (non-org users): Inherited if all external users go through Keycloak CAC flow

Not inherited (your residual for IA):
- IA-1 (identification and authentication policy): Your policy
- IA-2 (base control): **SHARED** — P1 provides Keycloak; you must configure your app's authentication integration correctly
- IA-4 (identifier management): Your user identifier lifecycle — who creates accounts, how are they named, how are they deprovisioned
- IA-5 (authenticator management base): Your responsibility for managing your app's service accounts and any non-CAC credentials

**SI — System and Information Integrity (partially inherited):**
Inherited through Twistlock/Prisma Cloud + Big Bang:
- SI-2(2) (automated flaw remediation): Inherited — Twistlock scans container images and alerts on CVEs
- SI-3 / SI-3(1)/(2) (malware protection): Inherited — Twistlock/Prisma provides runtime threat detection and malware scanning for containers. **Condition**: Must use Iron Bank images.
- SI-7/SI-7(1) (software integrity): Inherited — Iron Bank image signing (Cosign) + Notary v2 ensures image integrity
- SI-16 (memory protection): Inherited — container isolation provides memory separation

Not inherited (your residual for SI):
- SI-1 (system and information integrity policy): Your policy
- SI-2 (flaw remediation base): **SHARED** — P1 scans and reports; you must act on findings within POA&M timelines
- SI-4 (system monitoring): **SHARED** — P1 provides infrastructure monitoring; you must configure application-level monitoring, alerting, and incident detection for your app
- SI-5 (security alerts): Your responsibility to subscribe to relevant threat feeds and act on them

**CM — Configuration Management (partially inherited):**
Inherited through Big Bang hardened defaults:
- CM-6 (configuration settings): **SHARED** — Big Bang applies CIS Kubernetes Benchmark hardened settings. You inherit the K8s platform config. Your residual: your application-level configuration settings.
- CM-7 (least functionality): **SHARED** — Iron Bank images are minimally provisioned. Your residual: your app's unnecessary services/features must be disabled.
- CM-11 (user-installed software): Inherited — container immutability + read-only filesystems prevent arbitrary user software installs

Not inherited:
- CM-1 (configuration management policy): Your policy
- CM-2 (baseline configuration): Your application baseline — what YOUR system looks like when correctly configured
- CM-3 (configuration change control): Your change management process
- CM-4 (security impact analysis): Your process for analyzing changes before implementing
- CM-5 (access restrictions for change): Your SCM/GitOps access controls
- CM-8 (system component inventory): Your component inventory — P1 owns platform components, you own your app's components
- CM-9 (configuration management plan): Your CMP document

**AC — Access Control (partially inherited):**
Inherited:
- AC-3(9) (access enforcement — kernel-based): Inherited — Kubernetes + Istio AuthorizationPolicy at infrastructure level
- AC-4 (information flow enforcement): Inherited — Kubernetes NetworkPolicy + Istio enforces information flow rules
- AC-17(1)/(2) (remote access cryptographic protection): Inherited — TLS/mTLS enforced by P1

Not inherited:
- AC-1 (access control policy): Your policy
- AC-2 (account management): Your user lifecycle — P1 has users; YOUR app has users too. You own AC-2 for your application's accounts.
- AC-3 (access enforcement base): **SHARED** — P1 provides Istio/OPA; you must write AuthorizationPolicies specific to your app's API and namespace access model
- AC-5 (separation of duties): Your team structure — you define who can approve, who can deploy, who can access production
- AC-6 (least privilege): Your RBAC roles — not K8s system roles, but YOUR app's service accounts and user roles
- AC-7/AC-8/AC-9 (logon settings): Your application login settings (lockout, banners, re-auth)
- AC-11/AC-12 (session management): Your app's session timeout settings
- AC-14 (permitted actions without identification): Your public-access policy

### Families You 100% Own on Platform One (No Inheritance)

| Family | Why You Own It |
|--------|---------------|
| **PL — Planning** | Your SSP, CONOPS, rules of behavior. No one else writes your plan. |
| **PS — Personnel Security** | Your people undergo screening. P1 handles P1 admins; you handle your team. |
| **AT — Awareness and Training** | Your users take training. P1 trains P1 operators. |
| **RA — Risk Assessment** | Your FIPS 199, your RA, your vulnerability ID process. |
| **CA — Assessment/Authorization** | You get YOUR ATO. P1's ATO covers P1, not you. |
| **IR — Incident Response** | Your IRP, your team, your contact list, your runbooks. |
| **CP — Contingency Planning** | Your application-layer BCP/DR. Includes your RTO/RPO for the app. |
| **SA — System/Services Acquisition** | Your SDLC security practices, developer training, code review, supply chain. |
| **PM — Program Management** | Your risk strategy, enterprise architecture role. |
| **PT — PII Processing** | Your PIA, your consent mechanisms, your privacy notices. |
| **SR — Supply Chain** | Your software supply chain management, SBOM, third-party library vetting. |

### P1 Inheritance Summary

| Category | Approx. Control Count | Notes |
|----------|----------------------|-------|
| Fully inherited | ~120-140 controls | PE, MA, most MP, infra-level SC, core AU logging |
| Shared (P1 provides tool; you configure) | ~60-80 controls | AU-6, CA-7, IA-2, AC-3, SC-7, SI-2, SI-4, CM-6 |
| Your residual | ~180-220 controls | All PL/PS/AT/RA/CA/IR/CP/SA/PM + app-layer AC/IA/CM/SI/SC |

**Bottom line**: At IL4 on P1, you own roughly 45-55% of the NIST High baseline. The 3-day ATO is achievable because P1 handles the infrastructure-heavy families.

---

## AWS GovCloud (Standalone — Not on Platform One)

**Platform**: AWS GovCloud (without P1 on top)
**AWS ATO holder**: AWS FedRAMP High P-ATO (GSA FedRAMP PMO)
**DISA PA**: IL2, IL4, IL5 PAs from DISA for applicable services
**Download**: AWS CRM from AWS Artifact (aws.amazon.com/artifact — requires AWS GovCloud account)

### What AWS GovCloud Inherits for You

**PE — Physical and Environmental (all 18): FULL INHERITANCE**
- All PE controls: Fully inherited. AWS owns every data center.

**MA — Maintenance: FULL INHERITANCE**
- All MA controls at infrastructure level.

**MP — Media Protection: PARTIAL**
- Inherited: MP-2/MP-4/MP-5/MP-6/MP-7 (physical media handling)
- Your residual: MP-1 (policy), MP-3 (marking your data)

**AT — Training: PARTIAL**
- Inherited: AWS trains AWS employees (AT-2/AT-3 for AWS staff)
- Your residual: AT-1/AT-2/AT-3 for YOUR users and administrators

**SA-9 — External System Services: SHARED**
- AWS is your external provider; document it in your CRM as a service provider relationship
- Your residual: manage the relationship, monitor AWS's FedRAMP package status

### What AWS Provides But You Must Configure (Shared — Do Not Claim as Inherited)

**SC-7 (Boundary Protection)**: AWS provides VPC, subnets, and route tables. YOU must configure:
- Security groups (least-privilege inbound/outbound rules)
- NACLs for subnet-level restrictions
- AWS Network Firewall or WAF for application-layer filtering
- VPC Flow Logs enabled (required for boundary monitoring)

**SC-8 / SC-8(1) (Transmission Protection)**: AWS provides TLS capability via:
- ACM (AWS Certificate Manager) for certificate issuance
- ELB/ALB/NLB with TLS termination
YOU must implement: Actually configure TLS everywhere; disable HTTP; use TLS 1.2+; configure FIPS-compliant endpoints.

**AU-2/AU-3/AU-12 (Audit Events)**: AWS provides:
- CloudTrail for management/API plane events
- VPC Flow Logs for network events
- Config for resource state changes
YOU must: Enable CloudTrail in all active regions; enable all management events; enable S3 data events if S3 stores your data; configure retention.

**IA-2 (Authentication)**: AWS IAM is the tool. YOU must:
- Enforce MFA for all IAM users (console + API)
- Use IAM roles (not long-term access keys) for workloads
- Configure SCPs (Service Control Policies) if using Organizations

**CM-6 (Configuration Settings)**: AWS doesn't harden your EC2s. YOU must:
- Apply DISA STIG to EC2 operating systems (or CIS Benchmark as alternative)
- Use Systems Manager for compliance scanning
- Use Config rules for drift detection

**SI-3 (Malware Protection)**: AWS provides GuardDuty and Inspector. YOU must:
- Enable GuardDuty in all regions (threat detection)
- Enable Inspector for EC2 and container image scanning
- Have a process to act on findings within POA&M timelines

**SI-4 (System Monitoring)**: YOU must:
- Enable CloudWatch with alerting on security-relevant events
- Configure Security Hub with NIST 800-53 standard
- Define what anomalies trigger alerts

### What You Own Entirely (No AWS Inheritance)

Same as P1 for PL, PS, AT (for your users), RA, CA, IR, CP, SA, PM, PT, SR — plus:
- All application-layer AC controls (AC-2, AC-5, AC-6, AC-7, AC-11)
- All application-layer IA controls (IA-4, IA-5 for your app credentials)
- Application CM (your app baseline, change control, inventory)
- Application SI (flaw remediation for your code, SBOM)

**AWS GovCloud inheritance summary:**

| Category | Approx. Control Count |
|----------|----------------------|
| Fully inherited | ~80-100 controls |
| Shared (AWS provides tool; you configure) | ~100-120 controls |
| Your residual | ~170-200 controls |

**Bottom line**: At IL4 on AWS GovCloud standalone, you own ~55-65% of the NIST High baseline. More than P1 because there's no hardened platform layer between AWS and your app.

### IL5 on AWS GovCloud (Additional Requirements)

Beyond IL4, for IL5 on AWS GovCloud:
- **EC2**: Must use Dedicated Hosts or Dedicated Instances. `tenancy: dedicated` in launch template. No Spot instances.
- **EKS**: Must configure EKS with dedicated node groups on Dedicated Instances.
- **KMS**: Must use Customer Managed Keys (CMK) with imported key material OR AWS CloudHSM (FIPS 140-3 Level 3).
- **US persons only**: Implement IAM conditions to restrict access by geography/network; document in SSP.
- **Service availability**: Verify every AWS service used is IL5-authorized on DISA's catalog. Not all GovCloud services have IL5 PA.
- **Networking**: Additional isolation from non-DoD workloads; dedicated VPC; consider dedicated endpoints.

---

## Azure Government (Standalone)

**Platform**: Microsoft Azure Government
**Azure ATO holder**: Azure Government FedRAMP High P-ATO
**DISA PA**: IL2, IL4, IL5 (specific regions and services)
**Download**: Azure CRM from Microsoft Service Trust Portal (servicetrust.microsoft.com)

### What Azure Government Inherits for You

**PE — Physical and Environmental: FULL INHERITANCE**
- All PE controls covered by Microsoft data centers.

**MA — Maintenance: FULL INHERITANCE**

**MP — Media Protection: PARTIAL** (physical media only)

**AT — Training: PARTIAL** (Microsoft trains Microsoft employees)

### Shared Controls (Azure Provides Tool; You Configure)

**SC-7**: Azure provides VNet, NSGs, Azure Firewall capability. YOU must configure NSG rules, Azure Firewall policies, and UDRs.

**SC-8**: Azure provides TLS capability (App Gateway, Front Door, API Management). YOU must configure and enforce.

**IA-2**: Azure AD Government / Microsoft Entra ID provides MFA capability. YOU must enforce Conditional Access policies requiring MFA for all users.

**CM-6**: Azure Policy provides configuration governance. YOU must assign the NIST 800-53 or DoD IL4/IL5 Azure Policy initiative and remediate non-compliant resources.

**AU-2/AU-12**: Azure Monitor and Diagnostic Settings provide logging capability. YOU must enable diagnostic settings on every resource and configure Log Analytics workspace retention.

**SI-3/SI-4**: Microsoft Defender for Cloud (MDfC) provides threat detection. YOU must enable MDfC Standard tier and configure alerts.

### IL5 on Azure Government (Additional)

- Use **Azure Government** regions designated for DoD IL5 (USGov Virginia, USGov Texas for most services)
- Dedicated hardware: Azure Dedicated Host for compute if required
- CAC/PIV authentication: Configure Entra ID with certificate-based authentication (CBA) using DoD PKI
- Customer-managed keys: Azure Key Vault with HSM-backed keys required (FIPS 140-3 Level 3 HSM)
- Verify each service against Microsoft's FedRAMP High and IL5 dashboard

### Azure GovCloud Inheritance Summary

| Category | Approx. Control Count |
|----------|----------------------|
| Fully inherited | ~80-100 controls |
| Shared (Azure provides tool; you configure) | ~100-120 controls |
| Your residual | ~170-200 controls |

---

## DISA MilCloud 2.0

**Platform**: DISA MilCloud 2.0 — DISA-operated IaaS in DISA data centers
**ATO holder**: DISA holds the platform ATO
**Supported ILs**: IL4, IL5 (primary use), some IL6 capability
**Access**: Provisioned through DISA STOREFRONT

### What DISA MilCloud Inherits for You

**PE — Physical and Environmental: FULL INHERITANCE**
- DISA data centers: scif-grade physical security, environmental controls, power, cooling

**MA — Maintenance: FULL INHERITANCE**
- DISA handles all physical maintenance

**MP — Media Protection: PARTIAL**
- Physical media: Inherited
- Data classification and marking: Your residual

**DISA infrastructure controls:**
- Hypervisor STIG (VMware vSphere STIG): DISA applies and maintains
- Physical network STIG: DISA applies at the facility network layer
- Boundary protection at facility level: IronDome + DISA network protections

### What You Own (MilCloud 2.0)

Because MilCloud provides VMs (IaaS), you own everything from the OS up:
- All OS-level controls: OS STIG (Windows Server or RHEL) is YOUR job
- All application-layer controls
- All policy documents
- All identity management
- Your app's logging (MilCloud provides the infrastructure; you configure)
- All application CM

Your network controls:
- MilCloud provides virtual networking; you configure your VLANs and firewall rules
- DISA manages the physical network; you manage the virtual network layer

### MilCloud 2.0 Inheritance Summary

| Category | Approx. Control Count |
|----------|----------------------|
| Fully inherited | ~60-80 controls |
| Shared | ~80-100 controls |
| Your residual | ~210-250 controls |

**Bottom line**: MilCloud gives you less inheritance than AWS/Azure because it's pure IaaS with no platform layer. You own the OS and everything above.

---

## On-Premises DoD Enclave (Program-Owned or Leased Facility)

**Environment**: Program-owned infrastructure in a DoD-accredited facility (not DISA MilCloud)
**ATO structure**: You own everything; the enclave owner (base/installation) holds physical security ATO
**Supported ILs**: Depends on facility accreditation; typically IL4-IL6 capable

### What the Enclave Inherits for You

**PE — Physical and Environmental: INHERITED FROM ENCLAVE OWNER**
- The installation/facility AO holds PE controls
- You document this as "Inherited from [Installation Name] Physical Security ATO"
- Your CRM references the installation's SSP for PE

**Network boundary at facility level: SHARED**
- NIPR/SIPR boundary protection at the base is inherited
- Your system's internal network segmentation is your residual

### What You Own Entirely in On-Prem

Everything except PE (physical from facility):
- All MA (you contract/manage your own hardware maintenance)
- All MP (media policies and procedures are yours)
- All OS-level controls (DISA STIG compliance on every system)
- All IA (your Active Directory / identity infrastructure)
- All application controls
- All policy documents
- All network segmentation within your boundary
- HBSS/ESS on every endpoint (required by DoD policy)
- ACAS scanning (required; you run your own ACAS or schedule with the installation's ACAS)

### On-Prem Inheritance Summary

| Category | Approx. Control Count |
|----------|----------------------|
| Inherited (PE from facility) | ~20-30 controls |
| Shared | ~20-30 controls |
| Your residual | ~330-360 controls |

**Bottom line**: On-prem means you own almost everything. Don't start an on-prem ATO and expect shortcuts.

---

## Control Family Ownership Quick Reference

For rapid assessment, here's how control family ownership typically breaks down across platforms:

| Family | P1/Cloud One | AWS GovCloud | Azure Gov | DISA MilCloud | On-Prem |
|--------|-------------|--------------|-----------|---------------|---------|
| **AC** | Shared | Your residual | Your residual | Your residual | Your residual |
| **AT** | Your residual | Your residual | Your residual | Your residual | Your residual |
| **AU** | Shared | Shared | Shared | Your residual | Your residual |
| **CA** | Your residual | Your residual | Your residual | Your residual | Your residual |
| **CM** | Shared | Your residual | Shared | Your residual | Your residual |
| **CP** | Your residual | Your residual | Your residual | Your residual | Your residual |
| **IA** | Shared | Your residual | Shared | Your residual | Your residual |
| **IR** | Your residual | Your residual | Your residual | Your residual | Your residual |
| **MA** | Inherited | Inherited | Inherited | Inherited | Your residual |
| **MP** | Partial inherit | Partial inherit | Partial inherit | Partial inherit | Your residual |
| **PE** | Inherited | Inherited | Inherited | Inherited | Inherited (facility) |
| **PL** | Your residual | Your residual | Your residual | Your residual | Your residual |
| **PM** | Your residual | Your residual | Your residual | Your residual | Your residual |
| **PS** | Your residual | Your residual | Your residual | Your residual | Your residual |
| **PT** | Your residual | Your residual | Your residual | Your residual | Your residual |
| **RA** | Your residual | Your residual | Your residual | Your residual | Your residual |
| **SA** | Your residual | Your residual | Your residual | Your residual | Your residual |
| **SC** | Shared | Shared | Shared | Your residual | Your residual |
| **SI** | Shared | Shared | Shared | Your residual | Your residual |
| **SR** | Your residual | Your residual | Your residual | Your residual | Your residual |

**Legend**: Inherited = platform ATO covers, you reference in CRM. Shared = platform provides tool/capability; you configure for your app and document both sides. Your residual = entirely your implementation and documentation.
