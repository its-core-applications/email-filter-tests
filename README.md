These tests exercise the email content filters and reduce the need for manual
testing of filter changes.

To run them, clone this repository to a nonprod MX host and run `./setup.sh`,
followed by `pytest`.

# TODO
- make test suite work on non-MX hosts
- add tests for `logclient`, `userthrottle`, and `ipt` (relay-only filters)
- improve test coverage for `spf`, `rspamd`, `clamav`, and `pb`
- add integration tests (sending a message via simta, not just mocking up what
  we think simta should do.)
