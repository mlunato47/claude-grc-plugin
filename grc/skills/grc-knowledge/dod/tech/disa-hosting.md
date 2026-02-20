# DISA MilCloud 2.0 and On-Premises DoD Enclave — ATO Playbook

DISA MilCloud 2.0 is DoD-operated IaaS. It has higher trust than commercial cloud but less automation. You get the facility and hypervisor; you own everything from the OS up. On-premises DoD enclaves (installation/facility-owned infrastructure) are similar but with even less handed to you.

---

## What DISA MilCloud 2.0 Is

**MilCloud 2.0**: DISA-operated virtualized infrastructure in DISA data centers. Provides VMs, storage, and basic networking on DISA-managed hardware.

**Who operates it**: DISA's Cloud Services branch
**Access**: Via DISA STOREFRONT (storefront.disa.mil) — requires .mil account and sponsoring program
**Supported ILs**: IL4, IL5 (primary); some IL6 capability in specific facilities

**What it provides:**
- VMs (Windows Server and RHEL available)
- Virtual networking (vLAN/vDS-based, customer-configurable)
- Shared storage (SAN/NAS)
- DISA-managed hypervisors (VMware vSphere STIG-compliant)
- Physical security and environmental controls
- DISA network boundary protection (IronDome, JRSS integration)

**What it does NOT provide:**
- Pre-configured applications
- Identity management
- Container platforms (bring your own K8s/Docker)
- SIEM or logging aggregation (ACAS is available via DISA for scanning)
- Patch management for your guest OS
- Any application security tooling

---

## Key Authorities and Tooling

**Mandatory DoD tools in DISA-hosted environments:**

| Tool | Purpose | NIST Controls | Notes |
|------|---------|--------------|-------|
| **ACAS** (Assured Compliance Assessment Solution) | Vulnerability scanning | RA-5, SI-2 | Nessus-based; DISA operates enterprise ACAS; you can request scans or access |
| **ESS** (Endpoint Security Solution) | Host-based security (replaces HBSS) | SI-3, SI-7, AU-9 | Mandatory on all DoD endpoints in DISA environment |
| **STIG Viewer 2.x** | Manual STIG review | CM-6 | DISA-issued tool; download from public.cyber.mil/stigs/srg-stig-tools |
| **SCAP Compliance Checker (SCC)** | Automated STIG scanning | CM-6, CA-7 | Run against all systems; generates XCCDF/ARF results |
| **eMASS** | ATO package management | CA-6 | Your component's eMASS instance |

**ACAS specifics:**
- DISA operates ACAS at the enterprise level; many installations have local ACAS instances
- Contact DISA or the local ISSM to get credentialed ACAS scan results for your VMs
- You can also request a scan via the DISA ACAS team (submit ticket)
- Results come as .nessus files → import to eMASS or convert to PDF for package

**ESS specifics:**
- McAfee-based (transitioning to newer endpoint security solutions in DoD)
- ESS must be installed and checked into ePO (ePolicy Orchestrator) on every VM
- Proof of ESS enrollment = compliance with SI-3; without it, you have a Critical finding
- Request ESS agents from DISA STOREFRONT or local enclave IA team

---

## DISA MilCloud 2.0 ATO Process

### Pre-Sprint: STOREFRONT Provisioning

Before the sprint (this takes days to weeks — do not start ATO sprint until VMs are provisioned):
- [ ] DISA STOREFRONT account active
- [ ] Service Delivery Order (SDO) submitted for VM resources
- [ ] VMs provisioned and accessible
- [ ] DISA MilCloud CRM downloaded from STOREFRONT
- [ ] ESS agents obtained from DISA or local IA
- [ ] ACAS scanning access arranged (DISA-operated or local ACAS POC identified)

### Day 1: Install Tools, Scan, Boundary, Register

**0800-0900: Download MilCloud CRM**
- Log in to DISA STOREFRONT
- Download current MilCloud 2.0 Customer Responsibility Matrix
- Review: DISA responsible (physical, hypervisor, facility) vs. Shared vs. Customer (you)
- Note: MilCloud CRM is significantly smaller than AWS/Azure CRM — DISA covers less at the platform layer (IaaS only)

**0900-1000: Build Authorization Boundary Diagram**

MilCloud boundary structure:
```
DISA MilCloud Boundary (vSphere cluster - DISA-operated)
└── Your Authorization Boundary
    ├── vLAN: [subnet/24] - Application tier
    │   ├── VM-01: Windows Server 2022 (application server)
    │   └── VM-02: RHEL 8 (application support)
    ├── vLAN: [subnet/24] - Database tier
    │   └── VM-03: Windows Server 2022 + SQL Server
    └── vLAN: [subnet/24] - Management
        └── VM-04: Windows Server 2022 (jump server / Ansible controller)

External access:
- Users → DISA edge → your VMs (via NIPR or authorized VPN)
- Admin access: Jump server only (no direct RDP/SSH from outside)
```

Show the DISA IronDome boundary at the outer edge. Your boundary is the vLAN/VM cluster you own. The DISA network boundary and physical facility are inherited.

**1000-1100: FIPS 199 and eMASS Registration**

**1100-1200: Install ESS on All VMs**
- Deploy ESS agent to every VM immediately — without it, all scans are incomplete and you have a Critical finding
- Verify check-in to ePO: agents should show "connected" within 2 hours
- If using Windows: use ESS for Windows package
- If using RHEL: use ESS for Linux package

**1200-1400: Apply DISA STIGs**

This is the long pole for on-prem/MilCloud. Start immediately.

For Windows Server 2022:
```powershell
# Apply DISA GPO package
# Download from: public.cyber.mil/stigs/gpo
# Import to Group Policy Management Console (GPMC)
# GPOs include: STIG-compliant security settings for Windows Server

# After GPO application, run SCC scan
# SCC: scap-scc-x.x.x.x.exe (download from public.cyber.mil)
# SCC will score your system against Windows Server 2022 STIG
# Target: ≥95% compliance (CAT I findings = 0, CAT II minimized)
```

For RHEL 8:
```bash
# Apply DISA STIG using SCAP or Ansible
# DISA provides RHEL 8 STIG SCAP content: public.cyber.mil/stigs

# OpenSCAP automated remediation (Ansible-based):
# Download DISA RHEL 8 STIG Playbook from DISA
ansible-playbook -i inventory rhel8-stig.yml --tags high,medium

# Or use OpenSCAP directly:
oscap xccdf eval \
  --profile xccdf_org.ssgproject.content_profile_stig \
  --results-arf /tmp/rhel8-stig-results.xml \
  --report /tmp/rhel8-stig-report.html \
  /usr/share/xml/scap/ssg/content/ssg-rhel8-ds.xml
```

**1400-1600: Run ACAS Scans**
- Contact DISA ACAS team or local ACAS administrator
- Request credentialed scan of all your VMs (provide IP ranges and credentials for authenticated scan)
- Note: ACAS scans take 2-6 hours depending on how many hosts; schedule early
- If you have your own ACAS instance: configure Nessus scan with appropriate plugin families (DoD STIG, CVE checks, compliance checks)

**1600-1700: Configure Audit Logging**
This is entirely your responsibility on MilCloud — DISA does not aggregate your logs.

Windows (via Windows Event Forwarding or SIEM agent):
- Enable Advanced Audit Policy (via GPO or auditpol)
- Required audit categories: Logon/Logoff, Account Logon, Account Management, Object Access (for sensitive files), Policy Change, Privilege Use, Process Tracking (for high-value systems), System
- Forward to centralized SIEM (if available) or local SIEM (e.g., Splunk, ELK stack)
- Retention: 90-day online minimum; 3-year archival

RHEL 8:
```bash
# auditd configuration for STIG compliance
# /etc/audit/audit.rules should include:
-a always,exit -F arch=b64 -S execve -k exec
-a always,exit -F arch=b64 -S open,openat -F exit=-EACCES -k access
-w /etc/passwd -p wa -k identity
-w /etc/group -p wa -k identity
-w /etc/sudoers -p wa -k sudoers
-a always,exit -F arch=b64 -S setuid,setgid -k setuid
```

### Day 2: SSP Writing, STIG Remediation, Scan Processing

**0800-1000: Process ACAS Results + Begin STIG Remediation**
- Export ACAS results (Nessus format or CSV)
- Triage: CAT I (Critical/High STIG) — remediate today if possible
- CAT II (Medium STIG) — remediate before ATO or POA&M with 30-day timeline
- CAT III (Low STIG) — POA&M with 90-day timeline
- Known false positives: document in ACAS as exceptions with justification

Priority CAT I fixes that are typically auto-fixable:
- Disable SMBv1 (Windows): `Set-SmbServerConfiguration -EnableSMB1Protocol $false`
- Disable TLS 1.0/1.1: Registry keys or IIS settings
- Require NTLMv2: Group Policy → Network Security: LAN Manager Authentication Level → NTLMv2 only
- RHEL 8 FIPS mode: `fips-mode-setup --enable` (requires reboot; do this early)
- Password complexity: Via GPO or PAM configuration

**1000-1700: Write SSP Narratives**

Priority for MilCloud environment:

1. **SC-7 (Boundary Protection)**:
   "The [System Name] authorization boundary is implemented within DISA MilCloud 2.0 infrastructure. Physical boundary protection at the facility and network level is inherited from DISA (see CRM). [System Name] implements its authorization boundary through: vLAN segmentation separating application, database, and management tiers; firewall rules restricting inter-vLAN traffic to required ports only; no direct internet access from application or database tiers (all egress through DISA-provided proxy); jump server as the only administrative access point with CAC authentication enforced."

2. **CM-6 (Configuration Settings)**:
   "All Windows Server hosts are hardened to the DISA Windows Server 2022 STIG applied via DISA GPO package version [X.X, date]. RHEL 8 hosts are hardened per DISA RHEL 8 STIG using OpenSCAP/SCAP Security Guide. Automated SCAP/SCC scanning verifies STIG compliance monthly. Current compliance score: [X]% CAT I findings: [N] (all mitigated or POA&M'd); CAT II: [N]; CAT III: [N]. ACAS credentialed scans are performed monthly by [DISA enterprise ACAS / local ACAS]. Configuration baseline is documented in the CMP and enforced via Group Policy (Windows) and Ansible (RHEL)."

3. **IA-2 / IA-2(1)/(2) (Authentication)**:
   If using Active Directory + CAC:
   "User authentication is provided by Active Directory integrated with DoD PKI for CAC/PIV authentication. Group Policy enforces 'Interactive logon: Require smart card' for all interactive logins. Service accounts use complex, managed passwords stored in [CyberArk/Vault/Group Managed Service Accounts]. MFA is satisfied by CAC (physical factor + PIN = two-factor). Remote access via jump server requires CAC authentication enforced by RDP with NLA and smart card requirement. All administrative actions are logged to Windows Security Event Log category 'Account Logon' and 'Logon'."

4. **SI-3 (Malware Protection)**:
   "Endpoint Security Solution (ESS) is deployed on all system hosts and enrolled in ePO. ESS provides real-time malware scanning, host intrusion prevention, and file integrity monitoring. ESS signature updates are automated from DISA's enterprise DAT repository. On-demand scans run weekly. ESS alerts are configured to notify the ISSO on detection events. Evidence: ESS ePO dashboard showing all hosts as 'connected' and 'compliant'."

5. **AU-6 (Audit Review)**:
   "Windows Event Logs are collected by [SIEM agent/WEF] and aggregated in [Splunk/ELK/other SIEM]. RHEL audit logs (auditd) are forwarded to the same SIEM. The ISSO reviews SIEM dashboards [daily/weekly] for anomalous events. Alert rules are configured for: failed logon attempts >5, privilege escalation, account creation, security group changes, service starts/stops, audit log cleared. Alerts trigger [email/ticket] to ISSO within [X minutes]. Log retention: 90 days online in SIEM; [1/3/7] years in [archive location]."

Continue with IR, CP, AT, PS, PL, RA, SA narratives.

### Day 3: STIG Close-Out, Package, Submit

**0800-0900: Final SCAP/SCC Scan**
- Run SCC scan on all hosts after Day 2 remediation
- Export results as XCCDF ARF (for eMASS) and HTML (for human review)
- Confirm CAT I findings are zero (or documented as POA&M with accepted risk)

**0900-1000: Final ACAS Scan Request**
- Request final ACAS scan (or run if you have your own ACAS instance)
- Confirm scan is credentialed and current (today's date)
- Export Nessus results for eMASS attachment

**1000-1200: Assemble eMASS Package**
- SSP narratives entered
- DISA MilCloud CRM uploaded
- ACAS scan results attached
- SCC/SCAP results attached (XCCDF format preferred)
- ESS compliance evidence (screenshot of ePO console showing all hosts compliant)
- POA&M current
- System interconnections documented

**1200-1400: AO Briefing Deck**
For MilCloud/on-prem, AO briefing should emphasize:
- STIG compliance scores (CAT I/II/III counts)
- ESS enrollment status
- ACAS scan recency
- How boundary isolation is implemented in a shared DISA environment

**1400: ISSM endorsement and submit**

---

## On-Premises DoD Enclave (Non-DISA)

For programs running on their own hardware in a DoD facility (base IT / program-owned servers):

**What you inherit from the enclave:**
- PE controls: Inherited from the installation/facility AO (you reference their security plan)
- Network boundary at the base level: Inherited (NIPRNet connection is the base's responsibility)
- You document: "PE controls are inherited from [Installation Name, Base]. See [Installation Security Plan / POA&M reference]."

**What you own beyond MilCloud:**
- MA (maintenance): You manage your own hardware maintenance contracts
- MP: You manage your physical media destruction and protection
- All hardware lifecycle: procurement, receipt inspection, end-of-life destruction

**Key difference from MilCloud**: You need a hardware/software inventory in CM-8 that includes physical hardware (servers, switches, UPS, etc.) — not just VMs.

**Everything else**: Same as MilCloud — STIG everything, ESS on all hosts, ACAS scans, audit logging.

---

## DISA MilCloud / On-Prem ATO Failure Modes

**Failure 1: ESS not deployed before ACAS scans run**
- Symptom: ACAS results show "ESS agent not present" on hosts
- Impact: SI-3 Critical finding; stops ATO progress
- Fix: ESS must be installed and enrolled in ePO before ACAS scan; don't run ACAS without ESS

**Failure 2: STIG compliance below threshold**
- Symptom: SCC scan shows >5 CAT I findings or >50% CAT II non-compliance
- Impact: AO typically requires 95%+ CAT I compliance and clear POA&M for remaining
- Fix: Prioritize CAT I remediation in Day 2; use DISA GPO packages which auto-remediate many settings; use PowerSTIG or Ansible-STIG roles for bulk remediation

**Failure 3: Uncredentialed ACAS scans**
- Symptom: ACAS scan results show limited finding count because scanner couldn't authenticate to host
- Impact: RA-5 finding; uncredentialed scans are explicitly called out as insufficient in DoD policy
- Fix: Provide ACAS with service account credentials; ensure the ACAS scan is labeled as credentialed in the results; eMASS uploaders will check this

**Failure 4: No centralized logging (every VM logging locally only)**
- Symptom: AU-6 narrative says "logs are on the local system"
- Impact: AU-9 (audit protection) finding + AU-6 (review) finding; local logs are not protected and not being reviewed
- Fix: Deploy SIEM or at minimum Windows Event Forwarding to a central collector; even a standalone Splunk instance is acceptable for small deployments

**Failure 5: Administrative access not through jump server**
- Symptom: RDP/SSH directly to production servers from user workstations on admin network
- Impact: AC-17 (remote access) finding; no audit trail for admin sessions; no session recording
- Fix: Deploy bastion/jump server; require all admin access through it; enable session recording (Privileged Access Workstation pattern preferred)

**Failure 6: Using DISA MilCloud CRM from a previous year**
- DISA updates MilCloud CRM as they update the platform ATO
- Always download fresh from STOREFRONT

**Failure 7: No backup/recovery test for contingency plan**
- Symptom: CP section of SSP says "backups are performed" but no test evidence
- Impact: CP-4 (contingency plan testing) finding; AOs at military components often specifically ask
- Fix: Perform a tabletop recovery exercise before ATO; document results; attach to contingency plan

**Failure 8: Interconnection without ISA/MOU**
- Symptom: Application calls an external system (e.g., DCSA, another DoD system, commercial API) without documented interconnection
- Impact: CA-3 finding; AO won't authorize connections to undocumented external systems
- Fix: Document every external system connection as an ISA (Interconnection Security Agreement) or MOU; include in SSP Section 9 / System Interconnections
