# Azure Government — DoD ATO Playbook

Azure Government is Microsoft's US-government-only cloud, comparable in DoD authorization to AWS GovCloud. It holds FedRAMP High and DISA IL5 Provisional Authorization. The toolchain is different from AWS but the ATO mechanics are similar: you inherit the infrastructure, you own configuration and application layer.

---

## What Azure Government Is

**Azure Government** comprises dedicated US regions: USGov Virginia, USGov Texas, USGov Arizona, and USDoD East/West (DoD-specific, highly restricted).

**Authorization status:**
- FedRAMP High P-ATO: Issued by GSA FedRAMP PMO
- DISA PA: IL2, IL4, IL5 (specific services and regions; check DISA Cloud Service Catalog)
- USDoD East/West: Additional isolation for sensitive DoD workloads; not all customers can access

**Accounts**: Requires .mil or .gov email or sponsorship. Azure Government is a separate tenant from commercial Azure. Sign up at azure.microsoft.com/government.

**CRM download**: Microsoft Service Trust Portal at servicetrust.microsoft.com → Compliance Documentation → DoD → Azure Government CRM. Always download the latest version.

**Service availability**: Not all Azure services are available in Azure Government, and not all Government services are IL5 authorized. Check: docs.microsoft.com/azure/azure-government/documentation-government-services

---

## DISA Cloud Service Catalog Check

Before designing your architecture, verify each Azure service against the DISA Cloud Service Catalog. Common services confirmed at IL5 (verify currency):
- Azure Virtual Machines (with Dedicated Host for IL5)
- Azure Kubernetes Service (AKS)
- Azure SQL Database / SQL Managed Instance
- Azure Blob Storage, Azure Files
- Azure Key Vault (HSM-backed)
- Azure Active Directory (now Entra ID Government)
- Azure Monitor, Log Analytics
- Microsoft Sentinel
- Microsoft Defender for Cloud
- Azure Policy
- Azure App Service (verify IL5 status)
- Azure Functions (verify IL5 status for dedicated tier)

---

## Key Azure Government Tools for ATO

| Tool | What It Does | ATO Control Families |
|------|-------------|---------------------|
| **Microsoft Defender for Cloud (MDfC)** | Security posture management, threat protection | SI-3, SI-4, RA-5, CA-7 |
| **Azure Policy** | Configuration enforcement and compliance | CM-6, CM-7, CA-7 |
| **Azure Monitor + Log Analytics** | Centralized logging and alerting | AU-2, AU-3, AU-12, AU-6 |
| **Microsoft Sentinel** | SIEM/SOAR | AU-6, IR-4, SI-4 |
| **Microsoft Entra ID Government** | Identity, MFA, Conditional Access | IA-2, IA-5, AC-2 |
| **Azure Key Vault (HSM)** | Secrets and key management | SC-12, IA-5(7) |
| **Azure Dedicated Host** | Physical isolation for IL5 | SC-28 (physical separation) |
| **Azure Security Center** (part of MDfC) | Regulatory compliance dashboard | CA-7, RA-5 |
| **Azure Advisor** | Best practice recommendations | SA-3 |
| **Azure Blueprints** | Governance guardrails at subscription level | CM-6, SA-8 |
| **Azure Arc** | Hybrid management (on-prem + cloud) | CM-8, CM-6 |

---

## ATO Process: Step-by-Step for Azure Government

### Pre-Sprint: Account and Access Setup

Before the sprint:
- [ ] Azure Government subscription active (separate from commercial Azure)
- [ ] Service Trust Portal access configured — download CRM and Azure Government compliance documentation
- [ ] Microsoft Defender for Cloud (MDfC) enabled — Standard (Defender) tier
- [ ] Azure Policy initiatives assigned: NIST 800-53 Rev 5, DoD IL4/IL5 (built-in initiatives)
- [ ] Azure Monitor and Log Analytics workspace configured
- [ ] Microsoft Sentinel enabled (connects to Log Analytics workspace)
- [ ] Diagnostic settings enabled on all resource types
- [ ] Azure AD (Entra ID Government) conditional access policies drafted

### Day 1: Boundary, CRM, Scans, Registration

**0800-0900: Download and Review Azure CRM**
- Download from Service Trust Portal: Azure Government FedRAMP High CRM
- Review three columns: Microsoft Responsibility / Shared / Customer Responsibility
- Highlight your "Shared" column — every Shared control needs a narrative in your SSP
- Key Shared controls: SC-7, SC-8, IA-2, AU-2, CM-6, SI-3, CP-9

**0900-1030: Build Authorization Boundary Diagram**

Azure structure for boundary diagram:
```
Azure Government Subscription (Resource Group: [your-rg])
├── Virtual Network: 10.x.x.x/16
│   ├── Frontend Subnet: 10.x.1.x/24
│   │   └── Application Gateway / Azure Front Door (WAF enabled)
│   ├── App Subnet: 10.x.10.x/24
│   │   └── AKS Cluster / App Service / VMs
│   ├── Data Subnet: 10.x.20.x/24
│   │   └── Azure SQL / Cosmos DB / Storage
│   └── Management Subnet: 10.x.99.x/24
│       └── Bastion Host / Jump Host
└── NSGs applied to each subnet
    └── Azure Firewall (if present)
```

Show: NSGs, Azure Firewall, Application Gateway + WAF, Private Endpoints for PaaS services, VNet Integration.

**1030-1100: FIPS 199 Categorization**
- Document C/I/A with rationale; get mission owner sign-off

**1100-1200: Register in eMASS**

**1200-1600: Configure Security Baselines and Compliance Scanning**

Assign NIST 800-53 policy initiative to subscription:
```bash
# Assign built-in NIST 800-53 Rev 5 initiative
az policy assignment create \
  --name "nist-800-53-rev5" \
  --display-name "NIST SP 800-53 Rev. 5" \
  --policy-set-definition "/providers/Microsoft.Authorization/policySetDefinitions/179d1daa-458f-4e47-8086-2a68d0d6c38f" \
  --scope "/subscriptions/[subscription-id]" \
  --assign-identity \
  --location usgovvirginia
```

Enable Microsoft Defender for Cloud for all resource types:
```bash
az security pricing create -n VirtualMachines --tier 'standard'
az security pricing create -n ContainerRegistry --tier 'standard'
az security pricing create -n Containers --tier 'standard'
az security pricing create -n AppServices --tier 'standard'
az security pricing create -n SqlServers --tier 'standard'
az security pricing create -n StorageAccounts --tier 'standard'
az security pricing create -n KeyVaults --tier 'standard'
az security pricing create -n Dns --tier 'standard'
az security pricing create -n Arm --tier 'standard'
```

Configure diagnostic settings (must be on every resource for AU compliance):
```bash
# Example: VM diagnostic settings → Log Analytics
az monitor diagnostic-settings create \
  --resource [vm-resource-id] \
  --name "security-audit-logs" \
  --workspace [log-analytics-workspace-id] \
  --logs '[{"category":"Administrative","enabled":true},{"category":"Security","enabled":true},{"category":"Alert","enabled":true},{"category":"Policy","enabled":true}]'
```

Enable Activity Log diagnostic settings at subscription level:
```bash
az monitor diagnostic-settings create \
  --name "subscription-activity-logs" \
  --subscription [subscription-id] \
  --workspace [log-analytics-workspace-id] \
  --logs '[{"category":"Administrative","enabled":true},{"category":"Security","enabled":true},{"category":"ServiceHealth","enabled":true},{"category":"ResourceHealth","enabled":true},{"category":"Alert","enabled":true},{"category":"Recommendation","enabled":true},{"category":"Policy","enabled":true}]'
```

**1600-1700: Configure Azure Key Vault**

For IL4 (software-protected keys acceptable):
```bash
az keyvault create \
  --name "[vault-name]" \
  --resource-group "[rg]" \
  --location "usgovvirginia" \
  --sku standard \
  --enabled-for-disk-encryption true
```

For IL5 (HSM-backed keys required):
```bash
az keyvault create \
  --name "[vault-name]" \
  --resource-group "[rg]" \
  --location "usgovvirginia" \
  --sku premium \  # Premium = HSM-backed
  --enabled-for-disk-encryption true
```

### Day 2: SSP Writing + Findings Review

**0800-0900: Review MDfC Compliance Dashboard**
- Defender for Cloud → Regulatory Compliance → NIST 800-53 Rev 5
- Export current compliance status (PDF or CSV)
- Failed controls = POA&M entries
- Note: MDfC maps to controls; many failures are "not configured yet" — document these as POA&M with remediation plan

**0900-1700: Write SSP Narratives**

Priority for Azure Government:

1. **SC-7 (Boundary Protection)**:
   "Azure Government Virtual Network (VNet) provides the infrastructure boundary (inherited per CRM). [System name] implements application-layer boundary protection through: Azure Network Security Groups (NSGs) applied to each subnet per least-privilege rules [list key rules]; Azure Application Gateway with WAF enabled in Prevention mode [or Azure Firewall]; Private Endpoints for all PaaS services (Azure SQL, Storage) eliminating public internet exposure. NSG flow logs are enabled and retained 90 days in Log Analytics."

2. **IA-2 / IA-2(1)/(2) (Authentication and MFA)**:
   For Azure Government with Entra ID (Azure AD Government):
   "User authentication is provided through Microsoft Entra ID Government. Conditional Access policy [policy-name] enforces MFA for all users accessing [system name]. CAC/PIV authentication is enforced through Entra ID certificate-based authentication (CBA) configured with the DoD PKI trust anchors (DoD Root CA 3/4/5 certificates imported to Entra ID Government). No username/password access is permitted for human users; service principals use managed identities or certificate credentials. MFA policy documentation: [reference Entra ID Conditional Access policy export]."

   CAC/PIV configuration in Entra ID (Certificate-Based Authentication):
   ```
   Azure AD → Security → Certificate Authorities → Upload DoD PKI roots
   Conditional Access policy: Require CBA for all cloud apps; block legacy authentication
   Authentication Methods → Certificate-based Authentication → Enable
   ```

3. **AU-2/AU-6 (Audit and Review)**:
   "All Azure management plane events are captured in Azure Activity Log, forwarded to Log Analytics workspace [workspace-name] with 90-day online retention (7-year archive in Azure Storage). All VM, AKS, and PaaS resource diagnostic logs are sent to the same workspace per diagnostic settings configuration. Microsoft Sentinel is configured with Azure-native data connectors (Azure Activity, Microsoft Entra ID, Defender for Cloud, Azure Firewall). Alert rules are configured for: privileged account activity, policy violations, anomalous authentication, lateral movement indicators. ISSO reviews Sentinel incidents [daily/weekly] and escalates per IR procedures."

4. **CM-6 (Configuration Settings)**:
   "Azure Policy with NIST 800-53 Rev 5 initiative assigned at subscription level continuously evaluates [X] controls. Non-compliant resources are reported in Defender for Cloud Regulatory Compliance dashboard. Auto-remediation policies are deployed for [list auto-remediated policies, e.g., 'require HTTPS on Storage Accounts', 'enable TDE on SQL']. VM configuration hardening: [AKS nodes / VMs] use CIS-hardened images from Azure Marketplace (or custom image) and are assessed by [MDfC VM configuration assessment / Azure Automanage]. Drift is detected by Policy compliance scans running every 24 hours."

5. **SC-28/SC-28(1) (Protection at Rest)**:
   "All data at rest is encrypted using AES-256 with Azure-managed or customer-managed keys:
   - Azure SQL: Transparent Data Encryption (TDE) enabled with customer-managed key stored in Azure Key Vault Premium (HSM-backed for IL5)
   - Azure Blob Storage: Storage Service Encryption (SSE) with CMK
   - AKS persistent volumes: Encrypted disks with CMK
   - VM OS and data disks: Azure Disk Encryption (ADE) with Key Vault CMK
   Key Vault access policies restricted to service identities; human access requires privileged access workflow."

Continue with IR, CP, AT, PS, RA, SA, PL, PM narratives.

**1700: Begin POA&M population from MDfC findings**

### Day 3: Finalize, Package, Submit

Same pattern as AWS GovCloud Day 3.

Export MDfC compliance report (fresh) → attach to eMASS package.

---

## IL5 on Azure Government: Additional Requirements

**Azure Dedicated Host:**
```bash
# Create dedicated host group
az vm host group create \
  --name "[hostgroup-name]" \
  --resource-group "[rg]" \
  --location "usgovvirginia" \
  --zone 1 \
  --platform-fault-domain-count 1

# Create dedicated host
az vm host create \
  --host-group "[hostgroup-name]" \
  --name "[host-name]" \
  --sku "DSv3-Type1" \
  --resource-group "[rg]" \
  --location "usgovvirginia"

# Deploy VM to dedicated host
az vm create ... --host "[host-id]"
```

**Azure Key Vault Premium (FIPS 140-3 Level 3 HSM):**
- Use `-sku premium` for all Key Vaults handling IL5 keys
- Do not use `-sku standard` (software-protected keys) for IL5 CMKs
- Consider Azure Dedicated HSM for highest sensitivity (NSA-grade key management for NSS)

**AKS for IL5:**
- Node pools must deploy to Dedicated Hosts or Isolated VMs
- Use Azure Policy for Kubernetes add-on to enforce Pod Security Standards
- Enable Azure AD integration for RBAC (Entra ID Government)
- Enable cluster monitoring with Container Insights
- Restrict API server access to specific IP ranges (authorized admin workstations only)

**US persons only enforcement:**
- Entra ID Conditional Access: Restrict sign-ins to trusted network locations (DoD IP ranges / DoD VPN)
- Deny all authentication from non-DoD networks
- Log and alert on any attempt from blocked networks

---

## Azure Government ATO Failure Modes

**Failure 1: Commercial Azure instead of Azure Government**
- Symptom: Resources in `eastus` or `westus2` regions (commercial regions)
- Impact: System is not in the authorized boundary; IL4/IL5 authorization doesn't apply to commercial Azure
- Fix: All DoD IL4/IL5 workloads must be in `usgovvirginia`, `usgovtexas`, or `usgovarizona`

**Failure 2: Diagnostic settings not configured on all resources**
- Symptom: MDfC / Policy flags multiple resources as non-compliant for "audit logs not sent to workspace"
- Impact: AU-2/AU-12 finding; gaps in audit coverage
- Fix: Azure Policy initiative "Deploy diagnostic settings to Log Analytics" applied across subscription; enforce with `DeployIfNotExists` effect

**Failure 3: Azure AD (Entra ID) not enforcing MFA via Conditional Access**
- Symptom: Security Defaults enabled instead of Conditional Access; or Conditional Access only applies to some apps
- Impact: IA-2(1) finding; MFA not enforced for all users
- Fix: Disable Security Defaults; create Conditional Access policy requiring MFA for all users, all apps, all platforms; test with break-glass account

**Failure 4: Public endpoints on PaaS services (SQL, Storage)**
- Symptom: Azure SQL firewall allows internet access; Storage Account has public blob access
- Impact: SC-7 finding; data exposed to internet even if "protected by credentials"
- Fix: Private Endpoints for all PaaS services; disable public network access; Policy to enforce (`Deny` effect)

**Failure 5: NSGs with Any-Any rules from development**
- Symptom: NSG has inbound rule allowing 0.0.0.0/0 on port 443 or any port
- Impact: SC-7 finding; ALB/App Gateway should be the only public-facing resource
- Fix: Audit NSGs; restrict all inbound to specific source IPs or Application Gateway subnet only

**Failure 6: Using software-protected Key Vault for IL5 keys**
- Symptom: Key Vault SKU is `Standard` (not `Premium`); keys are software-protected
- Impact: IL5 requires HSM-backed keys; software keys don't meet the requirement
- Fix: Create new Premium Key Vault; migrate CMKs; delete old Vault

**Failure 7: Not downloading fresh CRM before ATO**
- Same as AWS — CRM changes as Microsoft adds services and updates controls
- Fix: Download from Service Trust Portal on Day 1 of every ATO effort

**Failure 8: Azure Policy in Audit mode only (not enforcing)**
- Symptom: Azure Policy initiative assigned with all effects set to `Audit` — finds violations but doesn't stop them
- Impact: CM-6 is weakened; configuration drift continues; findings don't resolve
- Fix: For critical policies (require HTTPS, require encryption, prohibit public access), change to `Deny` effect; for others, `AuditIfNotExists` with auto-remediation via `DeployIfNotExists`

---

## CAC/PIV Configuration in Azure Government (Detailed)

This is the most common authentication challenge. Steps:

**1. Import DoD PKI root certificates:**
- Download DoD PKI root CAs from DoD PKI PMO (cyber.mil/PKI-PKE)
- In Entra ID Government: Security → Certificate Authorities → Add
- Upload: DoD Root CA 3, DoD Root CA 4, DoD Root CA 5, DoD Intermediate CAs

**2. Enable Certificate-Based Authentication:**
- Entra ID → Authentication Methods → Certificate-based Authentication → Enable
- Configure issuer: Match to DoD CA names
- Map certificates to user accounts via UPN or email in Subject Alternative Name

**3. Create Conditional Access Policy:**
```
Policy name: Require-CAC-All-Apps
Assignments:
  Users: All users (exclude break-glass accounts)
  Cloud apps: All cloud apps
  Conditions: Any device platform
Access controls:
  Grant: Require authentication strength → Certificate-based authentication
  Block: Legacy authentication clients (separate policy)
```

**4. Configure application authentication:**
- Web apps: Use Entra ID authentication middleware
- API: Validate tokens issued by Entra ID Government (not commercial Entra)
- OIDC endpoint: `https://login.microsoftonline.us/[tenant-id]/v2.0`

**5. Test with a test CAC:**
- Use a test certificate to verify the full flow before rollout
- Check that non-CAC fallback is disabled
- Verify certificate chain validates to DoD root CAs
