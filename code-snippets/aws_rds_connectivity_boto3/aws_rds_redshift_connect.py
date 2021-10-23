
#------------------------------------------------------------------------------
# https://github.com/asraful
# aws_rds_redshift_connect.py
#------------------------------------------------------------------------------

import psycopg2
import boto3
import base64
import requests
import json
import configparser

def connect_redshift(redshift_arn,redshift_host,redshift_port,redshift_db):

    try:

        session = boto3.session.Session()
        client = session.client('secretsmanager','us-west-2')

        response = client.get_secret_value(SecretId=redshift_arn)
        data = json.loads(response['SecretString'])

        connection = psycopg2.connect(user = data['username'],
                                      password = data['password'],
                                      host = redshift_host,
                                      port = redshift_port,
                                      database = redshift_db)
        cursor = connection.cursor()

        # Print Redshift version
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        return len(record)

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to Redshift", error)
    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()

def test_redshift_connect():

    run_rds_test_scripts = 'true'

    #------------------------------------------------
    # redshift_arn   =  replace with appropiate value
    # redshift_host  =  replace with appropiate value
    # redshift_port  =  replace with appropiate value
    # redshift_db    =  replace with appropiate value
    #------------------------------------------------

    redshift_arn = 'redshift_arn'
    redshift_host = 'redshift_host'
    redshift_port = 'redshift_port'
    redshift_db = 'redshift_db'


    if run_rds_test_scripts == 'true':
        record = connect_redshift(redshift_arn,redshift_host,redshift_port,redshift_db)
        assert 1 == record
    else:
        print('db connectivity test is disabled')


test_redshift_connect()


