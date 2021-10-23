#------------------------------------------------------------------------------
# https://github.com/asraful
# S3_read_from_bucket.py
#------------------------------------------------------------------------------

import os.path
import boto3
import sys
import configparser
  
#------------------------------------------
# assign appropiate values to the variables
#------------------------------------------


def download_content(remote_path):
    s3_bucket_name = 'example_name'
    s3_client = boto3.client('s3')
    response = s3_client.download_file(s3_bucket_name,remote_path+'/example.txt','downloaded.txt')
    return response;

def test_init_():
    
    remote_path = 'project_bucket'
    response = download_content(remote_path)

    is_file = os.path.isfile('downloaded.txt')

    assert is_file == True

test_init_()