# Authorization Boundary Guidance

Guidance for defining, documenting, and defending system authorization boundaries. The boundary is arguably the most critical element of an SSP — everything else depends on it being right.

## What Is an Authorization Boundary?

The authorization boundary defines the scope of the system that is being authorized to operate. It encompasses all hardware, software, firmware, networks, data, and personnel associated with the system. Everything inside the boundary is subject to the security controls in the SSP. Everything outside is not — but connections to outside systems must be documented.

Per NIST 800-37: "The authorization boundary identifies the information resources that are included within the scope of the authorization decision."

## Boundary Components

### Must Be Inside the Boundary

| Component Type | Examples |
|---------------|----------|
| Application tier | Web servers, application servers, APIs, microservices |
| Data tier | Databases, data stores, caches, message queues |
| Management plane | Admin consoles, CI/CD pipelines, deployment tools |
| Monitoring | SIEM, logging infrastructure, alerting |
| Security services | WAF, IDS/IPS, vulnerability scanners, SOAR |
| Identity/auth | IdP, MFA infrastructure, certificate management |
| Network infrastructure | VPCs, subnets, load balancers, firewalls, DNS |
| Storage | Object storage, file systems, backup storage |
| Encryption | Key management, HSMs, certificate stores |
| Development/staging | If used for production data or accessible from production |

### Typically Outside the Boundary (but documented as interconnections)

| Component | Boundary Treatment |
|-----------|-------------------|
| Underlying IaaS/PaaS provider | Outside — inherited controls, documented via CRM |
| Corporate network | Outside — interconnection documented via ISA |
| Third-party SaaS tools | Outside — documented as external services |
| Client/user endpoints | Outside — documented as external users |
| Internet | Outside — boundary protection at the edge (SC-7) |
| Agency systems | Outside — interconnection via ISA/MOU |

### Gray Areas That Need Decisions

| Component | Considerations |
|-----------|---------------|
| CI/CD pipeline | Inside if it can deploy to production or access production data |
| Developer laptops | Typically outside, but if they have direct production access, consider including |
| Shared services (logging, monitoring) | Inside if they store/process system data |
| Third-party APIs called by the system | Outside, but the connection point is inside |
| CDN/edge services | Can be inside or outside — depends on whether they process/store data |
| DNS (external) | Typically outside — but DNS configuration that affects routing is inside |
| Email/notification services | Usually outside — documented as external service |
| Container registries | Inside if they store production images |
| Secrets management | Inside — critical security component |
| Backup/DR site | Inside the boundary (same security controls apply) |

## Cloud-Specific Boundary Patterns

### IaaS Pattern (e.g., AWS, Azure, GCP)
```
┌─────────────────────────────────────────────────┐
│              AUTHORIZATION BOUNDARY              │
│                                                  │
│  ┌──────────────┐  ┌──────────────┐             │
│  │  Application  │  │   Database   │             │
│  │   Servers     │  │   Servers    │             │
│  └──────────────┘  └──────────────┘             │
│  ┌──────────────┐  ┌──────────────┐             │
│  │   Network    │  │  Monitoring  │             │
│  │  (VPC/VNET)  │  │  & Logging   │             │
│  └──────────────┘  └──────────────┘             │
│  ┌──────────────┐  ┌──────────────┐             │
│  │   Security   │  │    CI/CD     │             │
│  │   Services   │  │  Pipeline    │             │
│  └──────────────┘  └──────────────┘             │
│                                                  │
└────────────────────┬────────────────────────────┘
                     │ Interconnection (SC-7)
┌────────────────────┴────────────────────────────┐
│        INHERITED (IaaS Provider Boundary)        │
│  Hypervisor, Physical network, Data centers      │
│  (Covered by provider's FedRAMP authorization)   │
└─────────────────────────────────────────────────┘
```

### SaaS Pattern
```
┌─────────────────────────────────────────────────┐
│              AUTHORIZATION BOUNDARY              │
│                                                  │
│  ┌──────────────────────────────────────┐       │
│  │    Complete SaaS Application Stack    │       │
│  │  (App + Data + Network + Security)    │       │
│  └──────────────────────────────────────┘       │
│  ┌──────────────┐  ┌──────────────┐             │
│  │  Admin/Mgmt  │  │  Monitoring  │             │
│  │   Console    │  │  & Logging   │             │
│  └──────────────┘  └──────────────┘             │
│                                                  │
└─────────────────────────────────────────────────┘
         │                        │
    Interconnection          Interconnection
    (IaaS/PaaS provider)    (Customer tenants)
```

### Multi-Tenant Considerations
- Each tenant's data must be logically separated
- The boundary covers the platform, not individual tenants
- Customer responsibilities documented in CRM
- Data isolation mechanisms must be described in SSP

## Boundary Diagram Requirements

### Authorization Boundary Diagram Must Show
- [ ] Clear boundary line encompassing all in-scope components
- [ ] All major system components within the boundary
- [ ] All external connections crossing the boundary
- [ ] Direction of data flow for each connection
- [ ] Ports and protocols for each connection
- [ ] Authentication mechanisms at boundary crossing points
- [ ] Which components are inherited (and from whom)
- [ ] Legend explaining symbols and line types

### Network Architecture Diagram Must Show
- [ ] Network segmentation (subnets, VPCs, security groups)
- [ ] Firewall/ACL placement
- [ ] Load balancers and traffic flow
- [ ] Management network (separate from production)
- [ ] DMZ or public-facing components
- [ ] Internal service communication paths
- [ ] Encryption in transit indicators

### Data Flow Diagram Must Show
- [ ] How data enters the system
- [ ] How data moves between components
- [ ] Where data is stored (at rest)
- [ ] How data exits the system
- [ ] Encryption points (in transit and at rest)
- [ ] Data classification levels if multiple types
- [ ] PII/CUI flow if applicable

## Common Boundary Mistakes

### Boundary Too Small
| Mistake | Consequence |
|---------|-------------|
| Excluding CI/CD pipeline | Deployments bypass security controls; assessor will flag |
| Excluding monitoring/logging | Audit controls (AU family) have no boundary coverage |
| Excluding management plane | Admin access not covered by AC/IA controls |
| Excluding backup/DR site | CP controls don't cover the recovery environment |
| Excluding dev/staging with prod data | Data protection gaps |

### Boundary Too Large
| Mistake | Consequence |
|---------|-------------|
| Including corporate IT infrastructure | Massive increase in control scope and assessment cost |
| Including all employee laptops | PE, CM controls now apply to hundreds of endpoints |
| Including third-party SaaS tools | You're now responsible for their control implementation |
| Including customer environments | Impossible to control and assess |

### Boundary Unclear
| Mistake | Consequence |
|---------|-------------|
| Diagram doesn't show clear boundary line | 3PAO will require redrawing before assessment |
| Components listed but not shown in diagram | Mismatch between SSP text and diagrams |
| Interconnections cross boundary without documentation | CA-3 findings |
| Shared services not clearly designated | Unclear responsibility for controls |

## Boundary Defense Strategies

When a 3PAO challenges your boundary, prepare for these questions:

### "Why isn't X inside the boundary?"
- State the rationale (e.g., "CI/CD runs in a separate account with no production data access")
- Show that the connection is documented as an interconnection
- Demonstrate that security controls apply at the boundary crossing point
- Provide evidence that excluding it doesn't create a security gap

### "How do you know the boundary is complete?"
- Reference the hardware/software inventory (CM-8) matching the boundary
- Show ports/protocols/services table aligns with boundary connections
- Demonstrate data flow diagrams account for all data paths
- Point to regular boundary reviews during SSP updates

### "How do you handle boundary changes?"
- Reference significant change process (CM-3)
- Show that boundary additions trigger SIA and SSP updates
- Demonstrate that new interconnections go through CA-3 process
- Point to change management board review for boundary-affecting changes

## Interconnection Documentation (CA-3)

Every connection crossing the authorization boundary requires:

| Element | Description |
|---------|-------------|
| Interconnection name | Descriptive name for the connection |
| Remote system | Name and authorization status of the remote system |
| Connection type | Dedicated, VPN, API, internet, etc. |
| Direction | Inbound, outbound, bidirectional |
| Ports/protocols | Specific ports and protocols used |
| Data exchanged | What data crosses the boundary |
| Security measures | Encryption, authentication, filtering |
| ISA/MOU | Interconnection agreement reference |
| Authorization | Is the remote system authorized? At what level? |
| Owner | Who owns and manages the connection |

## Boundary Review Triggers

Update the boundary documentation when:
- New components are added to the system
- Components are decommissioned
- New external connections are established
- Service model changes (e.g., migrating from self-managed to managed service)
- New data types are introduced
- Infrastructure provider changes
- Annual SSP review (at minimum)
