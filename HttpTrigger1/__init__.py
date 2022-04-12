import logging
import requests
import azure.functions as func


#conn = pymssql.connect(server='sql-server-nick.database.windows.net', user='nick', password='Password01!', database='db-')  
#cursor = conn.cursor()  

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    token = req.headers.get('Authorization')
    data = req.get_json()
    
    #if not token:
     #   try:
     #       req_body = req.get_json()
    #    except ValueError:
    #        pass
    #    else:
    #        token = req_body.get('token')

    if token:
        my_headers = {'Authorization': token, 'Trace-Id':'1234'}
        language = data['applicationPreference']['language']
        response = requests.get("https://vm00004332.nl.eu.abnamro.com:15000/ico/userprofile/v1/userprofile", headers=my_headers, verify=False)
        response = response.json()

        'SG_APP_ICO_APPR_PAD_OFFICE' in response['roles']

        corpId = response['employee']['corpId'] 


        #cursor.execute('SELECT language from application_preference WHERE corpId = ' + corpId +';') 
        
       # cursor.execute('insert into application_preference (corpid, language) values ('corpId, language)';')
        
        return func.HttpResponse(f"Language successfully stored, {corpId}{language}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
