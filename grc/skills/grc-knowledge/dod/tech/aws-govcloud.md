# AWS GovCloud — DoD ATO Playbook

AWS GovCloud is the most common platform for DoD cloud deployments NOT on Platform One. It gives you strong infrastructure inheritance (FedRAMP High P-ATO + DISA IL4/IL5 PA) but requires significantly more configuration work than P1 — because there's no Big Bang between you and the cloud.

---

## What AWS GovCloud Is

**AWS GovCloud (US)** comprises two regions: `us-gov-east-1` (AWS GovCloud East) and `us-gov-west-1` (AWS GovCloud West). Both are isolated from AWS commercial regions and accessible only to US government entities and authorized contractors.

**Authorization status:**
- FedRAMP High P-ATO: Issued by GSA FedRAMP PMO (covers ~347 controls)
- DISA Provisional Authorizations: IL2, IL4, IL5 (specific services — check DISA Cloud Service Catalog)
- Applies to: US-Gov East, US-Gov West

**Accounts**: Requires .mil or .gov email, or sponsorship from an existing DoD customer. AWS GovCloud accounts are separate from commercial AWS accounts.

**CRM download**: AWS Artifact → go to `console.amazonaws-us-gov.com` → AWS Artifact → Reports → FedRAMP High CRM. Download the current version every time you start an ATO (it gets updated as AWS adds services).

---

## DISA Cloud Service Catalog Check (Critical)

**Not all AWS GovCloud services are IL4 or IL5 authorized.** Before architecting your system, run every planned service against the DISA Cloud Service Catalog (iase.disa.mil or the successor at disa.mil/cloud).

**Commonly misunderstood:**
- Amazon Bedrock (AI/ML): Check catalog — may not be IL4/IL5 authorized
- Amazon Connect: Check catalog
- AWS Amplify: Check catalog
- Third-party marketplace services: Typically NOT covered by AWS PA; require separate authorization

**Services confirmed IL5 PA (as of knowledge cutoff; verify current):**
- EC2 (with dedicated tenancy for IL5)
- EKS (Elastic Kubernetes Service) with dedicated node groups
- S3 (with encryption and access controls)
- RDS (PostgreSQL, MySQL, Aurora) with encryption
- Lambda (serverless; verify for IL5 dedicated execution)
- VPC, Route53, CloudFront for GovCloud
- IAM, KMS, CloudHSM
- CloudTrail, Config, Security Hub, GuardDuty, Inspector
- Systems Manager (SSM)
- Secrets Manager, Parameter Store

---

## ATO Process: Step-by-Step for AWS GovCloud

### Pre-Sprint: Account and Access Setup

Before the 3-day sprint:
- [ ] AWS GovCloud account active (not commercial AWS)
- [ ] AWS Artifact access configured — download latest FedRAMP High CRM and SAR
- [ ] CloudTrail enabled in all used regions (us-gov-east-1, us-gov-west-1)
- [ ] AWS Config enabled with NIST 800-53 conformance pack
- [ ] AWS Security Hub enabled with NIST 800-53 standard
- [ ] AWS Inspector enabled for EC2 and container image scanning
- [ ] GuardDuty enabled in all active regions
- [ ] Billing alerts configured (operational, not ATO — but DoD auditors ask)
- [ ] AWS Organizations with Service Control Policies (SCPs) if multi-account

### Day 1: Boundary, CRM, Scans, Registration

**0800-0900: Download and Review AWS CRM**
- Open AWS Artifact; download current FedRAMP High CRM (Excel or PDF)
- Identify: Inherited (AWS responsible) vs. Shared (AWS provides; you configure) vs. Customer (you own)
- Highlight your Shared column — these require documented configuration evidence in your SSP
- Key Shared controls to note: SC-7, SC-8, IA-2, AU-2, CM-6, SI-3, SI-4, CP-9

**0900-1030: Build Authorization Boundary Diagram**
Structure for AWS GovCloud diagram:
```
AWS GovCloud Account Boundary (VPC: 10.x.x.x/16)
├── Public Subnets (10.x.1.x/24, 10.x.2.x/24)
│   └── ALB / NLB (HTTPS:443)
├── Private Subnets (10.x.10.x/24, 10.x.11.x/24)
│   ├── EC2 / EKS Nodes (application layer)
│   └── RDS (database layer)
└── Management Subnet
    └── Bastion / SSM (no public SSH; SSM preferred)

External connections:
- Users → ALB → App (TLS 1.3)
- App → RDS (encrypted in transit, TLS 1.3)
- App → [External API/Service] (ISA required)
```
Every subnet, security group, and NAT gateway should be visible.

**1030-1100: FIPS 199 Categorization**
- Identify data types (CUI categories from CUI Registry if IL4)
- Assign C/I/A impact levels with rationale
- Get mission owner sign-off

**1100-1200: Register System in eMASS**
- Register in appropriate component eMASS tenant
- Import NIST High baseline (for IL4) or NIST High + overlay (for IL5)

**1200-1300: Start Compliance Scans**

*Enable and configure (these generate continuous findings):*

AWS Security Hub → NIST 800-53 standard:
```bash
aws securityhub enable-security-hub --enable-default-standards --region us-gov-east-1
aws securityhub batch-enable-standards --standards-subscription-requests \
  '[{"StandardsArn":"arn:aws-us-gov:securityhub:::ruleset/finding-format/v/4.0.0/ruleset/nist-800-53"}]'
```

AWS Config → NIST 800-53 conformance pack:
```bash
# Deploy NIST 800-53 conformance pack
aws configservice put-conformance-pack \
  --conformance-pack-name NIST-800-53-rev5 \
  --template-s3-uri s3://[bucket]/conformance-packs/nist-800-53-rev5.yaml
```

AWS Inspector v2 (EC2 + ECR scanning):
```bash
aws inspector2 enable --resource-types EC2 ECR
```

GuardDuty:
```bash
aws guardduty create-detector --enable --finding-publishing-frequency FIFTEEN_MINUTES
```

*These scans run continuously. Check results at start of Day 2.*

**1300-1500: Configure CloudTrail and Logging**

For DoD IL4/IL5, CloudTrail must be comprehensive:
```bash
# Enable multi-region trail with S3 + CloudWatch Logs
aws cloudtrail create-trail \
  --name dod-audit-trail \
  --s3-bucket-name [your-trail-bucket] \
  --include-global-service-events \
  --is-multi-region-trail \
  --cloud-watch-logs-log-group-arn [log-group-arn] \
  --cloud-watch-logs-role-arn [role-arn]

# Enable management events + data events for S3
aws cloudtrail put-event-selectors \
  --trail-name dod-audit-trail \
  --event-selectors '[{"ReadWriteType":"All","IncludeManagementEvents":true,"DataResources":[{"Type":"AWS::S3::Object","Values":["arn:aws-us-gov:::*"]}]}]'
```

VPC Flow Logs for every VPC:
```bash
aws ec2 create-flow-logs \
  --resource-type VPC \
  --resource-ids [vpc-id] \
  --traffic-type ALL \
  --log-destination-type cloud-watch-logs \
  --log-group-name /aws/vpc/flowlogs
```

**1500-1700: Configure FIPS Endpoints and Encryption**

For all connections to AWS services, use FIPS 140-2 validated endpoints:
- Region-level FIPS: `*.fips.us-gov-east-1.amazonaws.com` / `*.fips.us-gov-west-1.amazonaws.com`
- RDS: Use `rds.us-gov-east-1.amazonaws.com` with SSL + certificate verification
- S3: Enable SSE-KMS with customer-managed key; verify FIPS endpoint in SDK config
- KMS: Create customer-managed key (CMK) in each region; do not use AWS-managed keys for CUI data

Configure S3 bucket encryption:
```json
{
  "Rules": [{
    "ApplyServerSideEncryptionByDefault": {
      "SSEAlgorithm": "aws:kms",
      "KMSMasterKeyID": "[your-cmk-arn]"
    },
    "BucketKeyEnabled": true
  }]
}
```

### Day 2: SSP Writing + Scan Results Processing

**0800-0900: Review Security Hub + Inspector + GuardDuty Findings**
- Security Hub: Export NIST 800-53 findings to CSV → these become POA&M entries
- Inspector: Review EC2 and ECR vulnerabilities → Critical/High → POA&M
- GuardDuty: Review threat findings → any Active findings need immediate investigation
- Triage: Separate findings into "fix now" (Critical, < 4 hours of work) vs. POA&M entries

**0900-1700: Write SSP Narratives**

For AWS GovCloud, focus these in order:

1. **System Overview** (PL-2): Architecture narrative; describe VPC, subnets, services; reference AWS GovCloud as authorized infrastructure

2. **SC-7 (Boundary Protection)**: Critical narrative — AO will read this carefully.
   Pattern: "AWS GovCloud VPC provides the outer infrastructure boundary (inherited from AWS FedRAMP High, see CRM). [System name] implements application-layer boundary protection through: [specific security groups listing rules], [NACLs], [AWS Network Firewall or WAF if present]. All inbound traffic routes through ALB on port 443 (HTTPS only; HTTP redirected). Direct access to backend resources is prohibited by security group rules. VPC Flow Logs are enabled and retained for 90 days."

3. **SC-8/SC-8(1) (Transmission Protection)**:
   Pattern: "TLS 1.3 is enforced for all external-facing connections via ALB with the 'ELBSecurityPolicy-TLS13-1-2-2021-06' policy. Database connections use SSL with certificate verification. Internal service communication uses [TLS via ALB/NLB / mTLS via service mesh]. AWS ACM provides certificate management; certificates are rotated automatically by ACM."

4. **IA-2 (Authentication)**:
   Pattern: "All IAM users have MFA enforced by IAM policy (DenyWithoutMFA SCP applied at account level). Application user authentication is handled by [Cognito / AWS IAM Identity Center / ADFS / on-prem IdP]. CAC/PIV is enforced for [human interactive access / privileged access / all access per IL requirement]. Service-to-service authentication uses IAM roles with no long-term access keys."

5. **AU-2/AU-6 (Audit Events and Review)**:
   "All management events are logged by CloudTrail in multi-region trail with 90-day retention in S3 (7-year archive in S3 Glacier). VPC Flow Logs capture all network traffic. Application logs are aggregated in CloudWatch Logs. CloudWatch Alarms are configured to alert on: [root account use, failed console logins >5 in 5 min, security group changes, IAM policy changes, unauthorized API calls]. Alerts route to [SNS topic → email/PagerDuty]. ISSO reviews CloudWatch dashboards and Security Hub findings every [Monday / daily / per schedule] for anomalies."

6. **CM-6 (Configuration Settings)**:
   "AWS Config with NIST 800-53 conformance pack enforces configuration baselines. Non-compliant resources are automatically flagged and (where possible) auto-remediated via Config Rules. EC2 instances are hardened per [DISA RHEL 8 STIG / CIS Benchmark Level 2] applied via Systems Manager State Manager. Hardening is applied at launch via launch template user-data or SSM document [document-name]. Configuration drift detection: Config Rules alert on security group changes, public S3 buckets, unencrypted EBS volumes, and unrotated credentials."

7. **SI-2 (Flaw Remediation)**:
   "AWS Inspector v2 performs continuous vulnerability scanning of EC2 instances and ECR container images. Critical vulnerabilities are addressed within 30 days (per DoD policy); High within 30 days; Moderate within 90 days. Findings are exported to POA&M monthly. Patch management for EC2 instances uses Systems Manager Patch Manager on a [weekly/bi-weekly] patching schedule with Patch Baselines aligned to [AWS-provided baseline for OS type]."

8. **CP-9 (Information Backup)** — Important Shared control:
   "AWS RDS automated backups are enabled with 7-day retention (configurable up to 35 days). S3 versioning is enabled on all data buckets. Cross-region replication to us-gov-west-1 is configured for disaster recovery. Recovery procedures are tested [quarterly/annually] per contingency plan."

Continue with remaining families (IR, AT, PS, PL, RA, SA, etc.)

**1700: Begin POA&M Population**
- Enter all Security Hub + Inspector findings
- Assign scheduled completion dates
- Assign responsible parties

### Day 3: Finalize, Package, Submit

**0800-0900: Final Scan Run**
- Re-run Inspector scan (verify it's current as of today)
- Security Hub findings reviewed for any new Critical findings since yesterday
- Export fresh findings report

**0900-1000: Finalize POA&M**
- All findings entered with real dates
- ISSM review

**1000-1200: eMASS Package Assembly**
- All SSP narratives entered
- CRM uploaded (AWS CRM + your completed customer column)
- Scan reports attached (Security Hub export, Inspector report)
- System interconnections documented (any ISAs for external services)

**1200-1400: AO Briefing Deck**
(Same structure as P1 playbook; AWS-specific version)

**1400-1500: ISSM endorsement + Submit to AO**

---

## AWS GovCloud IL4 vs. IL5 Key Differences

### IL5 Additional Requirements

**Compute isolation:**
```bash
# Launch template must specify dedicated tenancy
aws ec2 create-launch-template --launch-template-data '{
  "Placement": {
    "Tenancy": "dedicated"
  }
}'

# For EKS node groups:
aws eks create-nodegroup --cluster-name [name] --nodegroup-name [name] \
  --instance-types m5.xlarge \
  --launch-template id=[lt-id],version=1
# Ensure launch template has dedicated tenancy
```

**KMS with CloudHSM (for IL5 key management):**
```bash
# Create CloudHSM cluster
aws cloudhsm create-cluster --hsm-type hsm1.medium \
  --subnet-ids [subnet-id-1] [subnet-id-2]

# Create KMS custom key store backed by CloudHSM
aws kms create-custom-key-store \
  --custom-key-store-name il5-key-store \
  --cloud-hsm-cluster-id [cluster-id] \
  --trust-anchor-certificate [cert]

# Create CMK in custom key store
aws kms create-key --custom-key-store-id [store-id] \
  --description "IL5 Customer Managed Key"
```

**US persons only — enforce via IAM condition:**
```json
{
  "Effect": "Deny",
  "Principal": "*",
  "Action": "*",
  "Condition": {
    "StringNotEquals": {
      "aws:SourceVpc": "[your-vpc-id]"
    }
  }
}
```
Combined with network controls (only allow access from DoD network/VPN), this limits access to authorized US-persons-only systems.

**Service availability verification:**
Before starting IL5 architecture, export your services list and check each against DISA Cloud Service Catalog. Example check:
```bash
aws ec2 describe-instances --region us-gov-east-1  # IL5 OK
aws bedrock list-foundation-models --region us-gov-east-1  # Verify IL5 PA status before using
```

---

## AWS Tool Chain for ATO Acceleration

| Need | AWS Tool | How to Use for ATO |
|------|---------|-------------------|
| Compliance posture | Security Hub + NIST 800-53 standard | Shows controls passing/failing; export for POA&M |
| Configuration compliance | AWS Config + conformance packs | Continuous; auto-creates findings for drift |
| Vulnerability scanning | Inspector v2 | EC2 + ECR; auto-findings; export to POA&M |
| Threat detection | GuardDuty | Enables SI-4; review findings daily |
| Audit logging | CloudTrail + CloudWatch | Satisfies AU-2/AU-3/AU-12; set alarms for key events |
| Network flow logging | VPC Flow Logs | Required for boundary/traffic analysis |
| Patch management | Systems Manager Patch Manager | EC2 patching; evidence for SI-2 |
| Configuration management | Systems Manager State Manager | Apply STIG/CIS baselines via SSM documents |
| Secrets management | Secrets Manager | Eliminates hardcoded credentials; satisfies IA-5(7) |
| Encryption | KMS (CMK) | Required for IL4 data at rest; CloudHSM for IL5 |
| Network security | Security Groups + NACLs + Network Firewall + WAF | Layered boundary protection |
| Inventory | Systems Manager Inventory | CM-8 evidence |
| Incident response | GuardDuty + Security Hub → EventBridge → SNS | Automated alerting for IR-6 |

---

## AWS GovCloud ATO Failure Modes

**Failure 1: Using commercial AWS endpoints instead of GovCloud FIPS endpoints**
- Symptom: SDK calls hitting `s3.us-east-1.amazonaws.com` instead of `s3-fips.us-gov-east-1.amazonaws.com`
- Impact: SC-13 (FIPS cryptographic protection) finding; SC-8 concern for data in transit
- Fix: Explicitly configure FIPS endpoints in all AWS SDKs and CLI configurations; use environment variable `AWS_USE_FIPS_ENDPOINT=true`

**Failure 2: Long-term IAM access keys in use**
- Symptom: IAM credential report shows access keys older than 90 days; keys attached to IAM users instead of roles
- Impact: IA-5 finding; rotation policy violation
- Fix: Audit with `aws iam generate-credential-report`; rotate or remove all long-term access keys; use IAM roles for all workloads

**Failure 3: CloudTrail not enabled in all regions**
- Symptom: CloudTrail shows single-region trail; resources exist in both us-gov-east-1 and us-gov-west-1
- Impact: AU-2/AU-12 finding; gap in audit record coverage
- Fix: Create multi-region trail covering all GovCloud regions; verify with `aws cloudtrail get-trail-status`

**Failure 4: Security groups with 0.0.0.0/0 inbound**
- Symptom: Security group allows inbound from anywhere (common in dev environments promoted to prod)
- Impact: SC-7 (boundary protection) finding; obvious to any scanner
- Fix: Audit with Security Hub "EC2.19" rule; restrict to specific CIDR ranges or prefix lists; ALB should be the only public-facing resource

**Failure 5: Unencrypted EBS volumes or S3 buckets**
- Symptom: Inspector or Config finds unencrypted storage
- Impact: SC-28 (protection of information at rest) finding; Critical finding for IL4 data
- Fix: Enforce encryption at account level via SCP; `aws ec2 enable-ebs-encryption-by-default`; S3 bucket policies + default encryption

**Failure 6: No MFA on root account**
- Symptom: IAM > Security Recommendations shows root account without MFA
- Impact: Security Hub "IAM.9" finding; IA-2(1) for highest-privileged account
- Fix: Enable hardware MFA on root account; store in secure location per COMSEC-like procedures

**Failure 7: Stale IAM CRM (downloaded 2 years ago)**
- Symptom: CRM references deprecated AWS service names; missing controls added in recent AWS FedRAMP updates
- Impact: AO or SCA notices misalignment; questions validity of inherited control claims
- Fix: Always download fresh AWS CRM from AWS Artifact when starting an ATO; note the download date in the SSP

**Failure 8: Service not on DISA IL4/IL5 authorized list**
- Symptom: Architecture uses AWS service (e.g., a newer analytics or AI service) that doesn't yet have DISA PA
- Impact: System operates outside authorized boundary; AO cannot sign
- Fix: Check DISA catalog before architecture is locked in; if service is needed, request DISA PA review (takes months) or find authorized alternative
