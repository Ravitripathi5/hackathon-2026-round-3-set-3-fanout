# Set 3 - Notification Fanout.
#
# TODO SNS ${local.prefix}-notifications
# TODO SQS ${local.prefix}-notify-email and ${local.prefix}-notify-sms
# TODO SNS subscriptions with filter_policy channel=email|sms, raw_message_delivery=true
# TODO Queue policies allowing only that topic and source account
# TODO DynamoDB ${local.prefix}-notifications (pk event_id)
# TODO ECR/Lambda/role ${local.prefix}-fanout (+ ESM on email queue)
#      Lambda env TABLE_NAME and APP_VERSION; log retention 14
