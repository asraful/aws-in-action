#------------------------------------------------------------------------------
# https://github.com/asraful
# aws_rds_mssql_connect.py
#------------------------------------------------------------------------------


import pyodbc
import boto3
import base64
import requests
import json
import configparser


def connect_mssql(mssql_arn,mssql_host,mssql_port,mssql_db):
    session = boto3.session.Session()
    client = session.client('secretsmanager','us-west-2')

    response = client.get_secret_value(SecretId=mssql_arn)
    data = json.loads(response['SecretString'])

    username = data['username']
    password = data['password']

    print ('user name : ' + data['username'])
    print ('user name : ' + data['password'])

    driver = sorted(pyodbc.drivers()).pop()

    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+mssql_host+';DATABASE='+mssql_db+';UID='+username+';PWD='+ password)

    return cnxn;

def test_mssql_connect():

    run_rds_test_scripts = 'true'
    #------------------------------------------------------------------------------    
    # mssql_arn   =  replace with appropiate value
    # mssql_host  =  replace with appropiate value
    # mssql_port  =  replace with appropiate value
    # mssql_db    =  replace with appropiate value
    #------------------------------------------------------------------------------
    mssql_arn = 'mssql_arn'  
    mssql_host = 'mssql_host'
    mssql_port = 'mssql_port'
    mssql_db = 'mssql_db'

    if run_rds_test_scripts == 'true':
        cnxn = connect_mssql(mssql_arn,mssql_host,mssql_port,mssql_db)
        cursor = cnxn.cursor()
        cursor.execute ("SELECT DB_NAME()")
        row = cursor.fetchone()
        con = 'master' in row
        assert True == con
    else:
        print('no run')

test_mssql_connect()





