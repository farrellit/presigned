#!/bin/bash
bucket=$1
prefix=$2
exp=900
aws s3 ls s3://$bucket/$prefix | awk '{print "'$prefix'" $4 }' | xargs -I % ./presigned.py $bucket % 300 | sed -e "s/^/curl '/" -e "s/$/'/"
