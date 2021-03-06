from Google import Create_Service
from datetime import date, timedelta
from googleapiclient.http import MediaFileUpload

today = date.today()
last_month = date.today()-timedelta(21)

def upload():
    CLIENT_SECRET_FILE = 'credentials.json'
    API_NAME = 'drive'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/drive']

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    
    file_names = [f'artists({today})-({last_month}).csv', f'top-artists({today})-({last_month}).csv']

    for file_name in file_names:
        metadata = {
            'name': file_name[:-4],
            'mimeType': 'application/vnd.google-apps.spreadsheet'
        }
        
        media = MediaFileUpload(filename=file_name, mimetype='text/csv')
        
        service.files().create(
            body=metadata,
            media_body=media,
            fields='id').execute()
