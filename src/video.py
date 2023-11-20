import json
from src.channel import Channel


class Video(Channel):
    """Класс для видео с ютуб"""


    def __init__(self, video_id):
        self.__video_id = video_id
        youtube = self.get_service()
        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id).execute()
        self.title = video_response['items'][0]['snippet']['title']
        self.url = "https://www.youtube.com/watch?v=" + str(self.__video_id)
        self.like_count = int(video_response['items'][0]['statistics']['likeCount'])
        self.view_count = int(video_response['items'][0]['statistics']['viewCount'])


    @property
    def video_id(self):
        return self.__video_id


    def __str__(self):
        return f'{self.title}'


    def to_json(self, path) -> None:
        """Сохраняет в файл json информацию о видео"""
        new_dict = dict([('video_id', self.__video_id),
                         ('title', self.title),
                         ('url', self.url),
                         ('like_count', self.like_count),
                         ('view_count', self.view_count)])
        with open(path, 'w') as file:
            json.dump(new_dict, file)


class PLVideo(Video):
    """Класс для видео из плэйлиста ютуб"""
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
