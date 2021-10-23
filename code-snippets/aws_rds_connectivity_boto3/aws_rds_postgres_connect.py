
#------------------------------------------------------------------------------
# https://github.com/asraful
# aws_rds_postgres_connect.py
#------------------------------------------------------------------------------


import psycopg2
import boto3
import base64
import requests
import json
import configparser

def connect_postgres(postgres_arn,postgres_host,postgres_port,postgres_db):

    try:

        session = boto3.session.Session()
        client = session.client('secretsmanager','us-west-2')

        response = client.get_secret_value(SecretId=postgres_arn)
        data = json.loads(response['SecretString'])

        connection = psycopg2.connect(user = data['username'],
                                      password = data['password'],
                                      host = postgres_host,
                                      port = postgres_port,
                                      database = postgres_db)
        cursor = connection.cursor()

        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        return len(record)

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()



def test_postgres_connect():

    run_rds_test_scripts = 'true'

    #------------------------------------------------
    # postgres_arn   =  replace with appropiate value
    # postgres_host  =  replace with appropiate value
    # postgres_port  =  replace with appropiate value
    # postgres_db    =  replace with appropiate value
    #------------------------------------------------

    postgres_arn = 'postgres_arn'
    postgres_host = 'postgres_host'
    postgres_port = 'postgres_port'
    postgres_db = 'postgres_db'

    if run_rds_test_scripts == 'true':
        record = connect_postgres(postgres_arn,postgres_host,postgres_port,postgres_db)
        assert 1 == record
    else:
        print('db connectivity test is disabled')


test_postgres_connect()


