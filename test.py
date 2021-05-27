import boto3
from config import *

s3 = boto3.resource('s3')

try:
    count = 0
    for i in s3.Bucket(custombucket).objects.all():
        count = count + 1
    print(count)
