# Sentinel

> *"The watchful eye that never sleeps."*

## Overview

Sentinel is a security-focused file integrity monitoring tool that watches over your critical files and alerts on unauthorized changes. Built on the Ironcreed principles of defense in depth and eternal vigilance.

## Features

- **Hash-based verification** - SHA-256 checksums for tamper detection
- **Baseline snapshots** - Establish known-good states
- **Change detection** - Identify modifications, additions, and deletions
- **Audit logging** - Complete record of all scans and changes
- **Configurable monitoring** - Watch specific directories and their contents
- **No dependencies** - Pure Python 3.6+ implementation

## Installation

```bash
cd tools/sentinel
python3 sentinel.py --help
```

## Usage

### Initialize Baseline
```bash
# Create initial snapshot of files to monitor
python3 sentinel.py init /path/to/critical/files
```

### Verify Integrity
```bash
# Check for changes since baseline
python3 sentinel.py verify
```

### Show Status
```bash
# Display current monitoring status
python3 sentinel.py status
```

## Philosophy

Sentinel embodies key Ironcreed principles:

- **Defensive Design** - Assumes hostile environment, validates all inputs
- **Fail Secure** - Errors don't disable monitoring
- **Auditability** - All actions logged with timestamps
- **Simplicity** - No complex dependencies, easy to audit and verify
- **Resilience** - Continues monitoring even with partial failures

## Use Cases

- Monitor system configuration files for unauthorized changes
- Detect tampering with critical application code
- Verify integrity of deployment artifacts
- Audit security-sensitive directories
- Compliance monitoring for regulatory requirements

## Security Considerations

- Baseline stored with restricted permissions (0600)
- Hash algorithms resistant to collision attacks
- Audit logs protected from tampering
- No network communication (local-only operation)
- Memory-efficient processing of large file sets

## Limitations

- Does not prevent changes, only detects them
- Requires regular execution to be effective
- Baseline must be established in trusted state
- Does not detect runtime memory modifications

## Development

```bash
# Run with verbose logging
python3 sentinel.py verify --verbose

# Run tests (when available)
python3 -m pytest tests/
```

## Contributing

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for guidelines.

## License

See [LICENSE](../../LICENSE) for details.

---

*The sentinel watches. The fortress holds.*
