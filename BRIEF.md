# Set 3 - Notification Fanout

**Scenario.** An SNS topic fans out notifications. Email and SMS queues subscribe with filter policies on the `channel` attribute. Only the email queue is consumed by Lambda into DynamoDB. Ship it; review `crack-files/`.

## Part A - Build and deploy (50 points)

| What | Exact name or setting |
|---|---|
| ECR | `h3-<id>-fanout`, scan on push **on**, **IMMUTABLE**; image `:v1` |
| SNS | `h3-<id>-notifications` |
| SQS | `h3-<id>-notify-email`, `h3-<id>-notify-sms` |
| Subscriptions | Exact `channel=["email"]` / `channel=["sms"]` filters; raw delivery **true** on both |
| Queue policies | Both allow `sns.amazonaws.com`, scoped to the topic ARN and source account |
| DynamoDB | `h3-<id>-notifications`, partition key `event_id` (S), on-demand |
| Role | `h3-<id>-fanout-role` with the supplied permissions boundary |
| Lambda | `h3-<id>-fanout`, Image `:v1`, arm64, env `TABLE_NAME`, `APP_VERSION` |
| Event source | Email queue to Lambda; SMS queue intentionally has no consumer |
| Logs | `/aws/lambda/h3-<id>-fanout`, retention 14 |

**Live:** publish with `channel=email` → item appears; publish `channel=sms` → no table item.

Root Dockerfile: Lambda Python 3.12, `handler.lambda_handler`, and `APP_VERSION`. Root `deploy.yml`: tests, OIDC, ECR build/push, Terraform fmt/validate/plan, and no static AWS keys. Terraform must pass fmt/validate and contain no hardcoded account ID or credentials.

Run `python3 tools/check_build.py --id <id>` after deployment.

## Part B / C / Submit
Six fixes in `crack-files/` + `FINDINGS.md` + `tools/submit.py`. No destroy.
