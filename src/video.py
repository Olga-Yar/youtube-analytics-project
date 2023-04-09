from src.channel import youtube
from googleapiclient.errors import HttpError


class Video:
    def __init__(self, video_id):
        try:
            self.video_id = video_id
            video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                   id=video_id
                                                   ).execute()
            self.video_title: str = video_response['items'][0]['snippet']['title']
            self.video_url: str = video_response['items'][0]['snippet']['thumbnails']['default']['url']
            self.view_count: int = video_response['items'][0]['statistics']['viewCount']
            self.like_count: int = video_response['items'][0]['statistics']['likeCount']
        except HttpError as e:
            print(e)
            self.video_title: str = None
            self.video_url: str = None
            self.view_count: int = None
            self.like_count: int = None



    def __str__(self):
        return self.video_title


class PLVideo:
    def __init__(self, video_id):
        self.video_id = video_id

        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id
                                               ).execute()
        self.video_title: str = video_response['items'][0]['snippet']['title']
        self.view_count: int = video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.video_title
