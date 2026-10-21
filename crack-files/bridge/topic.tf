resource "aws_sns_topic" "bridge" {
  name = "notify-bridge"
}

resource "aws_sns_topic_policy" "bridge" {
  arn = aws_sns_topic.bridge.arn
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = "*"
      Action    = "sns:Publish"
      Resource  = aws_sns_topic.bridge.arn
    }]
  })
}
