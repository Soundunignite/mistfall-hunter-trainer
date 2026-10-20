# Security Policy

## Supported Versions

| Trainer Version | Mistfall Hunter Build | Supported |
|-----------------|-----------------------|-----------|
| 1.4.x           | 2026.01.x             | Yes       |
| 1.3.x           | 2025.12.x             | No        |

## Reporting a Vulnerability

If you discover a security issue in the trainer (e.g. unsafe memory writes,
privilege escalation in the injector, or signature leaks), please **do not**
open a public issue. Instead, contact the maintainers via the private channel
listed in the repository profile.

We aim to respond within 72 hours.

## Scope

- Memory read/write safety
- DLL injection stability
- Credential / config handling
- Anti-cheat bypass safety (avoid triggering kernel bans)

## Out of Scope

- Game-side anti-cheat updates
- Server-side detection logic