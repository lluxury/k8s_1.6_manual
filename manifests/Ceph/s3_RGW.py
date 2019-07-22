import boto
import boto.s3.connection
access_key = '32XTAG36CWVOJO1C6RF2'
secret_key = 'ebqJpzyDsfo7BbCxO8NKtoW83qt19iNLMjrBoJeq'
conn = boto.connect_s3(
    aws_access_key_id = access_key,
    aws_secret_access_key = secret_key,
    host = 'admin', port=7480,
    is_secure=False,
    calling_format = boto.s3.connection.OrdinaryCallingFormat(),
)

bucket = conn.create_bucket('my-first-s3-bucket')

for bucket in conn.get_all_buckets():
        print "{name}\t{created}".format(
                name = bucket.name,
                created = bucket.creation_date,
)
