import logging
import azure.functions as func
import os
# import pyodbc
import struct


def main(req: func.HttpRequest) -> func.HttpResponse:
    
    
    return func.HttpResponse(
            'Success',
            status_code=200
    )
    
    # logging.info('Python HTTP trigger function processed a request.')
    # server="alpha101.database.windows.net"
    # database="alpha101"
    # driver="{ODBC Driver 17 for SQL Server}"
    # query="SELECT * FROM dbo.Goal"
    # # Optional to use username and password for authentication
    # # username = 'name' 
    # # password = 'pass'
    # db_token = ''
    # connection_string = 'DRIVER='+driver+';SERVER='+server+';DATABASE='+database
    # #When MSI is enabled
    # if os.getenv("MSI_SECRET"):
    #     conn = pyodbc.connect(connection_string+';Authentication=ActiveDirectoryMsi')
    
    # #Used when run from local
    # else:
    #     SQL_COPT_SS_ACCESS_TOKEN = 1256

    #     exptoken = b''
    #     for i in bytes(db_token, "UTF-8"):
    #         exptoken += bytes({i})
    #         exptoken += bytes(1)

    #     tokenstruct = struct.pack("=i", len(exptoken)) + exptoken
    #     conn = pyodbc.connect(connection_string, attrs_before = { SQL_COPT_SS_ACCESS_TOKEN:tokenstruct })
    #     # Uncomment below line when use username and password for authentication
    #     # conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

    # cursor = conn.cursor()
    # cursor.execute(query) 
    # row = cursor.fetchone()

    # while row:
    #     print(row[0])
    #     row = cursor.fetchone()

    # return func.HttpResponse(
    #         'Success',
    #         status_code=200
    # )
