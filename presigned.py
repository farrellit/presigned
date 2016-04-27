#!/usr/bin/env python
import botocore.session
import sys
session = botocore.session.get_session()
client = session.create_client('s3')
presigned_url = client.generate_presigned_url(
    'get_object',
    Params={'Bucket':sys.argv[1],'Key': sys.argv[2] }
)
print(presigned_url)
