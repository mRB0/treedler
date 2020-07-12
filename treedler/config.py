import attr

AWS_REGION = 'us-east-2'

@attr.s
class Config:
    aws_access_key_id = attr.ib()
    aws_secret_access_key = attr.ib()
    s3_bucket_name = attr.ib()
