# Security policy

## Supported versions

Security fixes are provided for the latest release and the current `main` branch.

## Reporting a vulnerability

Please use [GitHub private vulnerability reporting](https://github.com/egore4606/Discord-link-publisher/security/advisories/new). Do not create a public issue for a suspected vulnerability.

Include the affected version, reproduction steps, expected impact, and any suggested mitigation. Remove webhook URLs, tokens, channel content, and other personal data from the report.

You should receive an acknowledgement within seven days. A confirmed report will be handled privately until a fix and coordinated disclosure are ready.

## Webhook exposure

If a Discord webhook URL is exposed, delete it immediately in Discord, create a replacement, and check the channel for unauthorized posts. Removing a secret from the newest commit does not remove it from Git history.
