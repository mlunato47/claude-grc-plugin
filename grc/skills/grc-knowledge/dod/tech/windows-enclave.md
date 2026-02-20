# Windows Server / Active Directory DoD Enclave — ATO Playbook

Windows-heavy DoD environments are the most common legacy scenario. Active Directory is the identity spine. Group Policy is the configuration engine. DISA STIGs are the compliance baseline. This playbook covers both standalone Windows applications and AD-integrated enterprise deployments.

---

## Technology Stack Overview

A typical Windows DoD enclave includes:
- **Windows Server 2022/2019** (application and services hosts)
- **Active Directory Domain Services** (identity, authentication, group policy)
- **IIS** (web services, if applicable)
- **SQL Server** (database, if applicable)
- **Windows Admin Center** or **SCCM/MECM** (systems management)
- **HBSS/ESS** (endpoint security — mandatory in DoD environments)
- **ACAS** (vulnerability scanning — DISA enterprise or local instance)

---

## Required STIGs (All Must Be Applied)

Every STIG application requires running SCC or STIG Viewer to generate evidence. Download all STIGs from: `public.cyber.mil/stigs`

| Component | STIG Title | Key CAT I Items |
|-----------|-----------|----------------|
| Windows Server 2022 | Windows Server 2022 STIG | Password complexity, SMBv1 disabled, NTLMv2 only, audit policy, local admin renamed |
| Windows Server 2019 | Windows Server 2019 STIG | Same categories |
| Active Directory | Active Directory Domain Services STIG | Admin tier model, privileged account separation, Kerberos settings, AdminSDHolder |
| DNS (Windows DNS) | Microsoft Windows DNS STIG | Zone transfer restrictions, DNSSEC |
| IIS 10 | IIS 10 Server STIG + IIS 10 Site STIG | TLS 1.2+ only, SSL cipher restrictions, HTTP to HTTPS redirect, directory browsing off |
| SQL Server 2019 | MS SQL Server 2019 STIG | SA account disabled, audit enabled, encrypted connections |
| .NET Framework | Microsoft .NET Framework STIG | Code signing, trust levels, error handling |
| Internet Explorer (legacy) | IE STIG | Disable if not needed |

**DISA GPO Package**: DISA provides pre-built Group Policy Objects that implement most Windows STIG settings automatically. Download from: `public.cyber.mil/stigs/gpo`

Applying DISA GPOs covers approximately 60-70% of Windows STIG checks automatically.

---

## Active Directory Architecture for ATO Compliance

A compliant AD deployment for DoD requires an administrative tier model to satisfy AC-5 (separation of duties) and AC-6 (least privilege).

**AD Tiering (Microsoft Tier Model, aligned to DISA AD STIG):**

```
Tier 0: Domain Controllers and Identity Infrastructure
  - Domain Admins, Schema Admins, Enterprise Admins
  - ONLY accessible from Tier 0 PAWs (Privileged Access Workstations)
  - No one should do daily work from a Tier 0 admin account
  - Accounts: domain-adminXXX (dedicated accounts; never used for email)

Tier 1: Servers and Applications
  - Local admins on member servers
  - Application service accounts
  - Accessible from Tier 1 PAWs or jump server

Tier 2: User Workstations
  - Standard user accounts
  - Helpdesk/workstation support
```

**For ATO, you need to document this in AC-5 and AC-6 narratives.** The AO will ask: "Who has domain admin rights and how is it controlled?"

**Protected Users Security Group**: Add all highly privileged accounts (Tier 0) to the Protected Users group. This prevents Kerberos delegation, RC4 usage, and WDigest credential caching for these accounts — satisfying several IA STIG requirements automatically.

---

## CAC/PIV Authentication for Windows

For DoD, CAC/PIV smart card authentication is the IA-2(1)/(2) solution. Configuration:

**Domain-wide smart card enforcement (Group Policy):**
```
Computer Configuration → Windows Settings → Security Settings → Local Policies → Security Options
  "Interactive logon: Require smart card" = Enabled
  "Interactive logon: Smart card removal behavior" = Lock workstation
```

**Certificate trust configuration:**
- Import DoD Root CA certificates to Trusted Root Certification Authorities (via GPO)
- Import DoD Intermediate CAs to Intermediate Certification Authorities
- Configure CRL distribution points to be accessible from the domain (or use OCSP)
- GPO path: Computer Configuration → Windows Settings → Security Settings → Public Key Policies

**NPS/RADIUS for network device authentication (if applicable):**
- Configure NPS with certificate-based authentication
- Maps CAC certificates to AD accounts via User Principal Name (UPN) matching

**Service accounts (no smart card):**
- Use Group Managed Service Accounts (gMSA) for services that run as service accounts
- gMSA automatically rotates passwords (240-character complex passwords, rotated every 30 days)
- Satisfies IA-5(1) (password-based authenticator management) for service accounts
- Configuration: `New-ADServiceAccount -Name [name] -DNSHostName [fqdn] -PrincipalsAllowedToRetrieveManagedPassword [computer-group]`

---

## Day-by-Day ATO Process for Windows Environment

### Pre-Sprint: Prerequisites

- [ ] DISA STIGs downloaded for all relevant components
- [ ] DISA GPO package downloaded
- [ ] SCC (SCAP Compliance Checker) installed on a management workstation
- [ ] STIG Viewer 2.x installed
- [ ] ACAS scanning arranged (DISA enterprise or local)
- [ ] ESS deployed on all hosts (critical — do not start ATO without this)
- [ ] PowerSTIG module available (optional but highly recommended for automation)

### Day 1: STIG Application, Scans, Registration, Boundary

**0800-1000: Apply DISA GPO Package**

```powershell
# Import DISA GPO package to AD
# GPOs are .zip files from public.cyber.mil/stigs/gpo
# Each GPO targets a specific STIG (Windows Server, IE, etc.)

# Create and link GPO for Windows Server STIG
New-GPO -Name "DISA-Windows-Server-2022-STIG" -Comment "v1r4" |
  Import-GPO -BackupGpoName "DoD Windows Server 2022 STIG" -Path "C:\DISA-GPOs\" |
  New-GPLink -Target "OU=Servers,DC=domain,DC=mil" -LinkEnabled Yes

# PowerSTIG module (alternative/supplement)
Install-Module PowerSTIG
Invoke-DscBuild -OsVersion 2022 -StigVersion 1.4

# Apply immediately with DSC
Start-DscConfiguration -Path C:\PowerSTIG\Output -Force -Wait -Verbose
```

**1000-1100: Run Initial SCC Scan (Baseline Assessment)**
```powershell
# SCC is a GUI tool; also has CLI mode
# Point SCC at the Windows Server 2022 STIG SCAP content
# Result: XCCDF ARF file + HTML report showing CAT I/II/III findings

# CLI mode example:
& "C:\Program Files\DISA\SCC 5.6\cscc.exe" `
  -f XCCDF `
  -x "C:\SCAP\U_Windows_Server_2022_V1R4_STIG_SCAP_1-3_Benchmark.zip" `
  -r "C:\SCAP\Results\"
```

**1100-1200: Triage SCC Results**
- CAT I findings (Open): must be mitigated or accepted with AO approval before ATO
- CAT II findings: most are auto-fixed by GPO; remainder POA&M with 90-day timeline
- CAT III: POA&M with 180-day timeline

Common auto-fixable CAT I items (post-GPO application):
- `WN22-CC-000020`: IE Enhanced Security Configuration must be enabled — auto-fixed by GPO
- `WN22-SO-000050`: SMBv1 must be disabled — `Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force`
- `WN22-SO-000070`: NTLM LAN Manager hash must not be stored — GPO auto-sets
- `WN22-AU-000500`: Audit policy must capture specific events — GPO sets auditpol

**1200-1300: Build Boundary Diagram + FIPS 199 + eMASS Registration**

**1300-1600: Configure Advanced Audit Policy**

For AU controls (this is a common SCC finding and a common AO question):
```powershell
# Apply comprehensive audit policy via auditpol
# These settings satisfy NIST AU-2 event logging requirements

auditpol /set /subcategory:"Logon" /success:enable /failure:enable
auditpol /set /subcategory:"Logoff" /success:enable
auditpol /set /subcategory:"Account Lockout" /success:enable /failure:enable
auditpol /set /subcategory:"Account Management" /success:enable /failure:enable
auditpol /set /subcategory:"Directory Service Access" /success:enable /failure:enable
auditpol /set /subcategory:"Privilege Use" /success:enable /failure:enable
auditpol /set /subcategory:"Policy Change" /success:enable /failure:enable
auditpol /set /subcategory:"System Events" /success:enable /failure:enable
auditpol /set /subcategory:"Process Creation" /success:enable /failure:enable
auditpol /set /subcategory:"Object Access" /success:enable /failure:enable

# Increase Security Event Log size (STIG requirement: minimum 1GB)
wevtutil sl Security /ms:1073741824

# Configure log forwarding (WEF - Windows Event Forwarding)
# On collector server:
wecutil cs subscription.xml  # Subscription XML defines what to collect

# Enable Windows Remote Management on source servers
winrm quickconfig -q
```

**1600-1700: Launch ACAS Scan**
Contact DISA ACAS or local administrator; provide host IPs and request credentialed scan.

### Day 2: SSP Writing, STIG Remediation

**0800-1000: Remediate Remaining CAT I Findings**

Focus on highest-impact fixes that can be done in < 2 hours each:
- Rename local Administrator account: `Rename-LocalUser -Name "Administrator" -NewName "[custom-name]"`
- Disable Guest account: `Disable-LocalUser -Name "Guest"`
- Configure FIPS-compliant algorithms: `Computer Configuration → Security Settings → Local Policies → Security Options → System cryptography: Use FIPS compliant algorithms` = Enabled
- BitLocker on all volumes: `Enable-BitLocker -MountPoint "C:" -EncryptionMethod XtsAes256 -TpmProtector` (requires TPM)
- Disable unnecessary services: disable Print Spooler, Browser, Fax on servers that don't need them

**1000-1700: Write SSP Narratives**

Windows-specific priority order:

1. **CM-6 (Configuration Settings)** — AO's primary concern for Windows:
   "All Windows Server 2022 hosts are hardened to DISA Windows Server 2022 STIG Version [X.X] applied via DISA GPO package v[X.X] linked to the '[OU-name]' OU. SCAP/SCC scanning (version [X.X]) verifies STIG compliance monthly using DISA SCAP content. Current compliance: [X]% overall; CAT I: [N] remaining (see POA&M entries WN-001 through WN-[N]); CAT II: [N]; CAT III: [N]. Configuration drift detection is performed by [SCCM Compliance Baseline / monthly SCC scans] with alerts to the ISSO on deviations. Active Directory STIG Version [X.X] is applied to the domain via DISA GPO package linked to the Domain Controllers OU."

2. **IA-2 / IA-2(1)/(2) (Authentication)**:
   "User authentication to [System Name] is provided by Active Directory integrated with DoD PKI for CAC/PIV authentication. Group Policy object 'DISA-Windows-Server-2022-STIG' enforces 'Interactive logon: Require smart card' for all interactive console and RDP sessions. Smart card removal triggers workstation lock. Network authentication uses Kerberos (NTLMv2 for legacy fallback only, restricted by GPO). Service accounts use Group Managed Service Accounts (gMSA) with automatic password rotation. Domain Admin accounts are restricted to Tier 0 Privileged Access Workstations and used exclusively for domain administration (not email or general use)."

3. **AC-2 (Account Management)**:
   "User accounts are managed in Active Directory by the ISSO or designated System Administrator. Account lifecycle: creation requires [approval workflow — e.g., supervisor email + ISSO confirmation]; modification requires change request ticket; review is conducted quarterly via AD account audit (last logon date, group membership review); termination is completed within 24 hours of personnel departure by disabling and then deleting the AD account. Privileged accounts (Tier 0/1) are separate from user accounts and require additional approval. Service accounts are inventoried in [CMDB/spreadsheet] and reviewed annually. Shared accounts are prohibited."

4. **AU-2/AU-6 (Audit Logging and Review)**:
   "Windows Advanced Audit Policy is configured to log [all AU-2 required event categories] as documented in the attached auditpol export. Event logs are collected by [Windows Event Forwarding / SIEM agent] and forwarded to [Splunk/ELK/other SIEM] with 90-day online retention. ISSO reviews SIEM dashboards [daily/weekly] for anomalous events. Alert rules detect: consecutive failed logons (>5 in 15 minutes), privilege escalation events (4672), account created (4720), service installed (7045), audit log cleared (1102). Alerts route to [email/ticket system] within 15 minutes. Log retention: 90 days online, 3 years archival."

5. **SC-28 (Protection at Rest)**:
   "Data at rest is protected by BitLocker Drive Encryption (AES-256, XtsAes256 mode) with TPM 2.0 protection on all server volumes. BitLocker recovery keys are stored in Active Directory (requires AD schema extension for BitLocker). SQL Server data files are encrypted via Transparent Data Encryption (TDE) using an AES-256 symmetric key protected by a certificate stored in the SQL master database. Database backups are encrypted. Evidence: BitLocker status reports from [SCCM / BitLocker Management]."

6. **SI-2 (Flaw Remediation)**:
   "Operating system and application patches are managed via [WSUS / MECM / SCCM] on a [monthly] patching cycle aligned to Microsoft Patch Tuesday. Critical patches are evaluated within 24 hours of release and deployed within [30] days. ACAS credentialed scans are performed monthly and results entered into the POA&M within [5] business days. Patch compliance reporting is available via [SCCM compliance dashboard]. ESS provides real-time exploit detection as a compensating control for vulnerabilities pending patching."

7. **IR-6 (Incident Reporting)**:
   "Security incidents are reported per [DoD/component] incident reporting requirements. ISSO is notified of incidents via SIEM alerting. ISSO escalates to ISSM within [4] hours for significant incidents. Category 1-3 incidents are reported to [ARCYBER/AFCYBER/NAVWAR] CERT within [1 hour / 24 hours per component policy]. Evidence: Incident reporting contact list in IRP Appendix A."

### Day 3: Final Scans, Package, Submit

**0800-0900: Final SCC Scan**
Run SCC after all Day 2 remediation. Export XCCDF ARF for eMASS.

**0900-1000: Final ACAS Scan**
Verify ACAS scan results are current. Export for eMASS.

**1000-1200: eMASS Package Assembly**
- SSP narratives entered
- SCC results attached (XCCDF format)
- ACAS results attached (.nessus or PDF)
- ESS compliance screenshot
- MilCloud or facility CRM uploaded (if applicable)
- POA&M current
- Interconnections documented (ISAs for AD domain connections to other systems)

---

## Windows STIG Automation Reference

**PowerSTIG** (PowerShell DSC-based STIG automation):
```powershell
# Install PowerSTIG
Install-Module -Name PowerSTIG -Force

# Generate DSC configuration for Windows Server 2022 STIG
configuration WindowsServer2022STIG {
    Import-DscResource -ModuleName PowerSTIG

    WindowsServer BaseStig {
        OsVersion = '2022'
        StigVersion = '1.4'
        OrgSettings = 'C:\PowerSTIG\OrgSettings.xml'  # Your organization's parameter values
        Exception = @{
            'V-253254' = @{  # Example: exception for a STIG check
                Identity = @('DOMAIN\ServiceAccount1')
            }
        }
    }
}

# Apply configuration
WindowsServer2022STIG -OutputPath C:\DSCConfig\
Start-DscConfiguration -Path C:\DSCConfig\ -Force -Wait
```

**SCC CLI for automated scanning:**
```batch
rem Run SCC from command line for CI/CD integration or automated scanning
"C:\Program Files\DISA\SCC 5.6\cscc.exe" ^
  -f XCCDF ^
  -x "U_MS_Windows_Server_2022_STIG_SCAP_1-3_Benchmark.zip" ^
  -s "Microsoft Windows Server 2022" ^
  -r C:\SCCResults\ ^
  -q
```

---

## Active Directory STIG Key Requirements

The AD STIG has specific requirements that often surprise teams:

**AdminSDHolder abuse**: Accounts with elevated permissions that are NOT in Protected Groups may have AdminSDHolder applied incorrectly. Audit: `Get-ADObject "CN=AdminSDHolder,CN=System,DC=..." -Properties nTSecurityDescriptor`

**Kerberos settings (AD STIG)**:
- Maximum service ticket lifetime: 10 hours (Default Domain Policy)
- Maximum ticket lifetime: 10 hours
- Maximum tolerance for computer clock synchronization: 5 minutes
- These prevent Kerberoasting attacks when combined with strong service account passwords

**Privileged account review**: AD STIG requires quarterly review of Domain Admins, Schema Admins, Enterprise Admins, Account Operators, Backup Operators. Document this review process in AC-2 narrative.

**DNS zone transfers restricted**: AD DNS STIG — zone transfers must be restricted to authorized secondary DNS servers only. Do not allow zone transfer to any host (ZONE TRANSFER: only to specific IPs).

---

## Windows Enclave Failure Modes

**Failure 1: FIPS Mode causing application failures**
- Symptom: After enabling FIPS via GPO/Registry, some applications fail (older .NET apps, SQL Server connections, legacy authentication)
- Impact: Team disables FIPS to fix apps; SC-13 finding
- Fix: Test FIPS mode in dev environment first; identify non-FIPS-compliant cipher usage in apps; update apps to use TLS 1.2+ with FIPS-approved cipher suites

**Failure 2: Local admin accounts with default/known passwords**
- Symptom: ACAS finds local administrator accounts with same password across all hosts, or default password
- Impact: IA-5 finding; AC-6 finding; commonly exploited in DoD pen tests
- Fix: Implement LAPS (Local Administrator Password Solution) — generates unique, complex password per host, stored in AD. Microsoft LAPS is built into Windows Server 2022.
```powershell
# Enable LAPS via Group Policy
# Computer Configuration → Administrative Templates → LAPS → Enable Local Admin Password Management
Set-AdmPwdAuditing -OrganizationalUnit "OU=Servers,DC=domain,DC=mil" -AuditedPrincipals "Domain Admins"
```

**Failure 3: SMBv1 still enabled**
- Symptom: SCC returns CAT I finding for `WN22-CC-000000` SMBv1 enabled
- Impact: Known critical vulnerability (used by EternalBlue/WannaCry)
- Fix: `Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force; Set-SmbClientConfiguration -EnableSMB1Protocol $false -Force`

**Failure 4: Event log size too small + no forwarding**
- Symptom: Security event log fills up; events overwritten before review
- Impact: AU-9 finding (overwriting audit records); AU-11 finding (retention)
- Fix: Increase Security log to at least 1GB; configure Windows Event Forwarding immediately

**Failure 5: No separation between admin and user accounts**
- Symptom: Domain Admins use their DA account for email and daily work
- Impact: AC-5, AC-6 findings; this is explicitly tested in pen tests and DoD assessments
- Fix: Enforce tiered admin model; DA accounts for domain admin tasks only; standard accounts for daily work

**Failure 6: SQL Server SA account enabled with known password**
- Symptom: SQL Server STIG check finds SA account enabled or using default/weak password
- Impact: IA-5 finding; Critical vulnerability
- Fix: Disable SA account (`ALTER LOGIN sa DISABLE`); use Windows Integrated Authentication for SQL connections instead of SQL authentication

**Failure 7: IIS running with directory browsing enabled**
- Symptom: IIS STIG check finds directory browsing enabled
- Impact: CAT II finding; information disclosure
- Fix: `Set-WebConfigurationProperty /system.webServer/directoryBrowse -PSPath IIS:\ -Name enabled -Value False`

**Failure 8: ACAS scan done without credentials**
- All Windows scans must be credentialed (authenticated)
- Uncredentialed scan will show far fewer findings than reality
- Provide ACAS with a domain service account with local admin rights to all target hosts
