import os

from googleapiclient.discovery import build

import json

api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


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

    # @classmethod
    # def get_channel(cls, channel_id):
    #     return cls.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()

    def to_json(self, name):
        with open(name, 'w', encoding='utf-8') as outfile:
            json.dump(self.print_info(), outfile, indent=2, ensure_ascii=False)

    def __str__(self):
        return f'{self.title} ({self.url})'     # <название_канала> (<ссылка_на_канал>)

    def __add__(self, other):
        return self.followers + other.followers

    def __sub__(self, other):
        return int(self.followers) - int(other.followers)

    def __ge__(self, other):
        return int(self.followers) >= int(other.followers)