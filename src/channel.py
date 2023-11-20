import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    __api_key: str = os.getenv('YT_API_KEY')


    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала.
        Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        youtube = self.get_service()
        channel = youtube.channels().list(id=self.channel_id,
                                          part='snippet,statistics').execute()
        self.title = channel['items'][0]["snippet"]['title']
        self.description = channel['items'][0]['snippet']['description']
        self.url = channel['items'][0]['snippet']['thumbnails']['default']['url']
        self.subscriber_count = int(channel['items'][0]['statistics']['subscriberCount'])
        self.video_count = int(channel['items'][0]['statistics']['videoCount'])
        self.view_count = int(channel['items'][0]['statistics']['viewCount'])


    @property
    def channel_id(self):
        return self.__channel_id


    def __str__(self):
        return f'{self.title}(https://www.youtube.com/channel/{self.channel_id})'


    def __add__(self, other):
        return self.subscriber_count + other.subscriber_count


    def __sub__(self, other):
        return self.subscriber_count - other.subscriber_count


    def __lt__(self, other):
        return self.subscriber_count < other.subscriber_count


    def __le__(self, other):
        return self.subscriber_count <= other.subscriber_count


    def __gt__(self, other):
        return self.subscriber_count > other.subscriber_count


    def __ge__(self, other):
        return self.subscriber_count >= other.subscriber_count


    def __eq__(self, other):
        return self.subscriber_count == other.subscriber_count


    @classmethod
    def get_service(cls):
        """Создает специальный объект для работы с API"""
        youtube = build('youtube', 'v3', developerKey=cls.__api_key)
        return youtube


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        youtube = self.get_service()
        channel = youtube.channels().list(id=self.channel_id,
                                          part='snippet,statistics').execute()
        self.printj(channel)


    def to_json(self, path) -> None:
        """Сохраняет в файл json информацию о канале"""
        new_dict = dict([('channel_id', self.__channel_id),
                         ('title', self.title),
                         ('description', self.description),
                         ('url', self.url),
                         ('subscriber_count', self.subscriber_count),
                         ('video_count', self.video_count),
                         ('view_count', self.view_count)])
        print(new_dict)
        with open(path, 'w') as file:
            json.dump(new_dict, file)


    @staticmethod
    def printj(dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))
