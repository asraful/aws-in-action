#------------------------------------------------------------------------------
# https://github.com/asraful
# S3_write_to_bucket.py
#------------------------------------------------------------------------------

import os.path
import boto3
import sys

import configparser

#------------------------------------------
# assign appropiate values to the variables
#------------------------------------------

def create_file():

    file = open("example.txt", "w")
    file.write("Your text goes here")

    ab_file_path = os.getcwd() + "/" + file.name

    file.close()

    print(ab_file_path)
    return ab_file_path


def upload_file(upload_path):
    ab_file_path = create_file()
    s3_client = boto3.client('s3')
    uploaded = s3_client.upload_file(ab_file_path,'bucket_name',upload_path+'/example.txt')
    return 1;

def test_init_():

    bucket_name = 'bucket_name'

    response = upload_file(bucket_name)

    assert 1 == response

test_init_()