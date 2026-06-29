# devsecops-lab

A deliberately vulnerable Flask app used to learn DevSecOps tooling.

## Intentional vulnerabilities
- SQL injection (`/user?username=`)
- Command injection (`/ping?host=`)
- Path traversal (`/file?name=`)
- Hardcoded secrets
- Overprivileged Docker container

## Pipeline
- SAST: Semgrep
- Secrets: Gitleaks
- Container scan: Trivy (coming soon)
