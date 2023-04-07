import datetime

import isodate as isodate

from src.channel import youtube, Channel


class PlayList:

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.playlist = Channel.get_service().playlists().list(id=playlist_id,
                                                               part='contentDetails,snippet',
                                                               maxResults=50,
                                                               ).execute()
        self.title = self.playlist['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/playlist?list={self.playlist_id}'

    @property
    def total_duration(self):
        """
        Возвращает объект класса datetime.timedelta с суммарной длительность плейлиста
        (обращение как к свойству, использовать @property)
        """
        return self.get_time()

    def __str__(self):
        return self.get_time()

    def get_time(self):
        """
        Расчет суммарной длительности плейлиста
        """
        video_response = youtube.videos().list(part='contentDetails,statistics',
                                               id=','.join(self.get_video_ids())
                                               ).execute()
        delta = datetime.timedelta()
        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            delta += duration
        return delta

    def get_video_ids(self):
        """
        Возвращает список id видео в плейлисте
        """
        playlist_videos = youtube.playlistItems().list(playlistId=self.playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()

        # получить все id видеороликов из плейлиста
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        return video_ids

    def show_best_video(self):
        """
        Возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)
        """
        dict_id = {}
        for video in self.get_video_ids():
            video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                   id=video
                                                   ).execute()
            like_count: int = video_response['items'][0]['statistics']['likeCount']
            dict_id[like_count] = video
        return f'https://youtu.be/{dict_id[sorted(dict_id.keys())[0]]}'



