## Requirements:
* botocore

## Invocation:
    ./presigned.py <bucket> <key> <expiry-secs>

Key should _not_ start with '/'

## Generate CURL commands for each s3 key in a directory

This is a little bash pipeline that can help with that:

    ./dir-commands.sh <bucket> <prefix> 

In this case, `<prefix>` _must_ end in `/`.  Expiry seconds is 15 minutes in this case.  
