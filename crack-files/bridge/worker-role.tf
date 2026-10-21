resource "aws_iam_role" "bridge" {
  name = "notify-bridge"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
      Action    = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy" "bridge" {
  role = aws_iam_role.bridge.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = ["sns:*", "sqs:*", "iam:PassRole"]
      Resource = "*"
    }]
  })
}
