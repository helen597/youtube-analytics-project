from src.channel import Channel
from datetime import timedelta
import isodate


class PlayList(Channel):
    """Класс для плейлиста"""

    def __init__(self, playlist_id):
        """
        Инициализация экземпляра класса
        param playlist_id: ID плейлиста
        """
        self.__playlist_id = playlist_id
        youtube = self.get_service()
        playlist_response = youtube.playlists().list(id=playlist_id, part='snippet,contentDetails',
                                                     maxResults=50).execute()
        self.title = playlist_response['items'][0]["snippet"]['title']
        self.url = "https://www.youtube.com/playlist?list=" + self.__playlist_id
        self.__total_duration = isodate.parse_duration("PT0M0S")
        self.count_duration()

    @property
    def total_duration(self):
        return self.__total_duration

    # @total_duration.setter
    # def total_duration(self, duration: timedelta):
    #     self.__total_duration = duration

    def count_duration(self):
        """Подсчёт длительности видеороликов из плейлиста"""
        youtube = self.get_service()
        playlist_videos = youtube.playlistItems().list(playlistId=self.__playlist_id,
                                                       part='snippet,contentDetails',
                                                       maxResults=50).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]

        video_response = youtube.videos().list(part='contentDetails,statistics',
                                               id=','.join(video_ids)
                                               ).execute()
        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            self.__total_duration += duration

    def show_best_video(self):
        """
        Возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)
        """
        youtube = self.get_service()
        playlist_videos = youtube.playlistItems().list(playlistId=self.__playlist_id,
                                                       part='snippet,contentDetails',
                                                       maxResults=50).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]

        video_response = youtube.videos().list(part='statistics',
                                               id=','.join(video_ids)
                                               ).execute()
        video_dict = {video["id"]: video["statistics"]["likeCount"] for video in video_response['items']}
        for key in video_dict.keys():
            if video_dict[key] == max(video_dict.values()):
                best_video = f"https://youtu.be/{key}"
        return best_video
