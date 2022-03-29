import logging

import azure.functions as func

import os
import pyodbc
import struct

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    server="alpha101.database.windows.net"
    database="alpha101"
    driver="{ODBC Driver 17 for SQL Server}"
    query="SELECT * FROM dbo.Goal"
    # Optional to use username and password for authentication
    # username = 'name' 
    # password = 'pass'
    db_token = ''
    connection_string = 'DRIVER='+driver+';SERVER='+server+';DATABASE='+database
    #When MSI is enabled

    conn = pyodbc.connect(connection_string+';Authentication=ActiveDirectoryMsi')
    
    cursor = conn.cursor()
    cursor.execute(query) 
    row = cursor.fetchone()

    while row:
        print(row[1])
        row = cursor.fetchone()

    return func.HttpResponse(

            'Success fetch',
            status_code=200
    )
