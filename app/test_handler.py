import os
import unittest
from unittest import mock

os.environ["TABLE_NAME"] = "h3-p01-notifications"
os.environ["APP_VERSION"] = "v1"

import handler  # noqa: E402


class FanoutTests(unittest.TestCase):
    def test_raw_json_body(self):
        with mock.patch.object(handler, "table") as tbl:
            event = {"Records": [{"body": '{"event_id":"e1","body":"hi"}'}]}
            handler.lambda_handler(event, None)
        item = tbl.return_value.put_item.call_args.kwargs["Item"]
        self.assertEqual(item["event_id"], "e1")
        self.assertEqual(item["channel"], "email")

    def test_sns_envelope(self):
        envelope = {
            "Type": "Notification",
            "TopicArn": "arn:aws:sns:ap-south-1:111111111111:t",
            "Message": '{"event_id":"e2","body":"x"}',
        }
        with mock.patch.object(handler, "table") as tbl:
            handler.lambda_handler({"Records": [{"body": __import__("json").dumps(envelope)}]}, None)
        self.assertEqual(tbl.return_value.put_item.call_args.kwargs["Item"]["event_id"], "e2")


if __name__ == "__main__":
    unittest.main()
