from Google import Create_Service
from datetime import date, timedelta
from googleapiclient.http import MediaFileUpload

def upload(today, last_month):
    CLIENT_SECRET_FILE = 'client_secret_425712180042-p1rrbt7p73l6s2hr9hc7td7h7pu17o1t.apps.googleusercontent.com.json'
    API_NAME = 'drive'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/drive']

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    folder_id = '1PbrqOc-pxDBoyf65eUWgN-raTirIGJyD'
    file_names = [f'artists({today})-({last_month}).csv', f'top-artists({today})-({last_month}).csv']
    mime_type = 'text/csv'

    for file_name in file_names:
        metadata = {
            'name': file_name,
            'parents': [folder_id]
        }
        media = MediaFileUpload(filename=file_name, mimetype=mime_type)
        service.files().create(body=metadata,media_body=media,fields='id').execute()
    