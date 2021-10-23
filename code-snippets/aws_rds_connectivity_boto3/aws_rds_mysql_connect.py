
#------------------------------------------------------------------------------
# https://github.com/asraful
# aws_rds_mysql_connect.py
#------------------------------------------------------------------------------

import pymysql
import boto3
import configparser

def connect_mysql(mysql_arn,mysql_host,mysql_port,mysql_db):
    session = boto3.session.Session()
    client = session.client('secretsmanager','us-west-2')

    response = client.get_secret_value(SecretId=mysql_arn)

    data = json.loads(response['SecretString'])

    username = data['username']
    password = data['password']

    print ('user name : ' + data['username'])
    print ('user name : ' +data['password'])

    # Open database connection
    db = pymysql.connect(mysql_host,username,password,mysql_db)

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT VERSION()")

    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    print ("Database version : %s " % data)

    execute_query = cursor.execute("SELECT id FROM rml_address LIMIT 1")

    result = cursor.fetchone()

    db.close()

    return execute_query

def test_mysql_connectivity():
    
    run_rds_test_scripts = 'true'

    #----------------------------------------------
    # mysql_arn   =  replace with appropiate value
    # mysql_host  =  replace with appropiate value
    # mysql_port  =  replace with appropiate value
    # mysql_db    =  replace with appropiate value
    #----------------------------------------------

    mysql_arn = 'mysql_arn'
    mysql_host = 'mysql_host'
    mysql_port = 'mysql_port'
    mysql_db = 'mysql_db'

    if run_rds_test_scripts == 'true':
        query_executed = connect_mysql(mysql_arn,mysql_host,mysql_port,mysql_db)
        assert query_executed == 1
    else:
        print('no run')

test_mysql_connectivity()
