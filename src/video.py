from src.channel import youtube


class Video:
    def __init__(self, video_id, video_name, video_url, views, likes):
        self. video_id = video_id
        self.video_name = video_name
        self.video_url = video_url
        self.views = views
        self.likes = likes

    def __str__(self):
        return self.video_name


class PLVideo:
    def __init__(self, video_id, playlist_id):
        self.video_id = video_id
        self.playlist_id = playlist_id

        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id
                                               ).execute()
        print(video_response)
        self.video_title: str = video_response['items'][0]['snippet']['title']
        self.view_count: int = video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.video_title
