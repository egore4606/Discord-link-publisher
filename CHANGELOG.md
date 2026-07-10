# Changelog

All notable changes to this project are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and releases use [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- Command-line interface with dry-run, ordering, and delay controls.
- Secure webhook configuration through `DISCORD_WEBHOOK_URL`.
- Retry handling for rate limits, temporary Discord errors, and network failures.
- Automated tests, linting, builds, CodeQL, dependency review, and Dependabot.
- Multilingual documentation and community health files.

### Changed

- Publishing failures now return a non-zero exit code instead of being silently ignored.
- The webhook URL and Discord response body are no longer printed.

[Unreleased]: https://github.com/egore4606/Discord-link-publisher/compare/Release...HEAD
