import os
from urllib import response
import googleapiclient.http
import googleapiclient.discovery
import google_auth_oauthlib.flow

class YouTubeClient(object):
    def __init__(self, credentials):
        youtube_dl.utils.std_headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
        scopes = ['https://www.googleapis.com/auth/youtube.upload']
        os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
        api_service_name = 'youtube'
        api_version = 'v3'
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            credentials, scopes)
        credentials = flow.run_console()
        youtube_client = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)
        self.youtube = youtube_client
    
    def set_thumbnail(self, video_id, thumbnail):
        response = self.youtube.thumbnails().set(
            videoId=video_id,
            media_body=MediaFileUpload(thumbnail, mimetype='image/jpeg')
        )
        response.execute()
        return response