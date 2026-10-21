"""Notification Fanout - consume email-channel SQS messages into DynamoDB."""
import json
import os

TABLE_NAME = os.environ.get("TABLE_NAME", "")
APP_VERSION = os.environ.get("APP_VERSION", "dev")

_table = None


def table():
    global _table
    if _table is None:
        import boto3
        _table = boto3.resource("dynamodb").Table(TABLE_NAME)
    return _table


def parse_body(record):
    raw = record.get("body") or "{}"
    data = json.loads(raw)
    # Raw delivery: body is the publish message string (JSON).
    if isinstance(data, dict) and "Message" in data and "TopicArn" in data:
        data = json.loads(data["Message"])
    return data


def lambda_handler(event, context):
    for record in event.get("Records") or []:
        data = parse_body(record)
        event_id = str(data.get("event_id") or "").strip()
        if not event_id:
            continue
        table().put_item(Item={
            "event_id": event_id,
            "channel": "email",
            "body": str(data.get("body") or ""),
            "version": APP_VERSION,
        })
    return {"ok": True}
