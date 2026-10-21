# Set 3 - Notification Fanout

**Scenario.** An SNS topic fans out notifications. Email and SMS queues subscribe with filter policies on the `channel` attribute. Only the email queue is consumed by Lambda into DynamoDB. Ship it; review `crack-files/`.

## Part A names
| Resource | Name |
|---|---|
| ECR / Lambda / role | `h3-<id>-fanout` (+ `-role`) |
| SNS topic | `h3-<id>-notifications` |
| SQS | `h3-<id>-notify-email`, `h3-<id>-notify-sms` |
| DynamoDB | `h3-<id>-notifications` (pk `event_id`) |

Subscriptions: filter `channel` = `email` vs `sms`, **raw message delivery** on, queue policies scoped to the topic ARN.

**Live:** publish with `channel=email` → item appears; publish `channel=sms` → no table item.

Same packaging/CI/OIDC/ECR IMMUTABLE rules as other sets.

## Part B / C / Submit
Six fixes in `crack-files/` + `FINDINGS.md` + `tools/submit.py`. No destroy.
