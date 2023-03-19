import os

from googleapiclient.discovery import build

from helper.youtube_api_manual import youtube, api_key
import json
from pyyoutube import Api

api_key: str = os.getenv('YT_API_KEY')

class Channel:
    """Класс для ютуб-канала"""



    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id

        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.title = channel['items'][0]['snippet']['title']
        self.about = channel['items'][0]['snippet']['description']
        self.url = channel['items'][0]['snippet']['thumbnails']['default']['url']
        self.followers = channel['items'][0]['statistics']['subscriberCount']
        self.video_count = channel['items'][0]['statistics']['videoCount']
        self.views = channel['items'][0]['statistics']['viewCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        return channel


    @classmethod
    def get_service(cls):
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube


    def to_json(self, name):
        with open(name, 'w', encoding='utf-8') as outfile:
            json.dump(self.print_info(), outfile, indent=2, ensure_ascii=False)


