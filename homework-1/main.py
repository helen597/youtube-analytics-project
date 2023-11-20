# from src.channel import Channel
#
# if __name__ == '__main__':
#     moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
#     # moscowpython.print_info()
#
#     """
# {
#   "kind": "youtube#channelListResponse",
#   "etag": "uAdmwT0aDhY9LmAzJzIafD6ATRw",
#   "pageInfo": {
#     "totalResults": 1,
#     "resultsPerPage": 5
#   },
#   "items": [
#     {
#       "kind": "youtube#channel",
#       "etag": "cPh7A8SKcZxxs_UPCiBaXP1wNDk",
#       "id": "UC-OVMPlMA3-YCIeg4z5z23A",
#       "snippet": {
#         "title": "MoscowPython",
#         "description": "Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\nПрисоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)",
#         "customUrl": "@moscowdjangoru",
#         "publishedAt": "2012-07-13T09:48:44Z",
#         "thumbnails": {
#           "default": {
#             "url": "https://yt3.ggpht.com/ytc/AGIKgqNv2rZ6mOSuXvJLYhmTc0nd-LtI5RiDtsEBpguJXA=s88-c-k-c0x00ffffff-no-rj",
#             "width": 88,
#             "height": 88
#           },
#           "medium": {
#             "url": "https://yt3.ggpht.com/ytc/AGIKgqNv2rZ6mOSuXvJLYhmTc0nd-LtI5RiDtsEBpguJXA=s240-c-k-c0x00ffffff-no-rj",
#             "width": 240,
#             "height": 240
#           },
#           "high": {
#             "url": "https://yt3.ggpht.com/ytc/AGIKgqNv2rZ6mOSuXvJLYhmTc0nd-LtI5RiDtsEBpguJXA=s800-c-k-c0x00ffffff-no-rj",
#             "width": 800,
#             "height": 800
#           }
#         },
#         "localized": {
#           "title": "MoscowPython",
#           "description": "Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\nПрисоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)"
#         },
#         "country": "RU"
#       },
#       "statistics": {
#         "viewCount": "2303120",
#         "subscriberCount": "25900",
#         "hiddenSubscriberCount": false,
#         "videoCount": "685"
#       }
#     }
#   ]
# }
#
#     """
#     highload = Channel('UCwHL6WHUarjGfUM_586me8w')
#
#     # Используем различные магические методы
#     print(moscowpython)  # 'MoscowPython (https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)'
#     print(moscowpython + highload)  # 100100
#     print(moscowpython - highload)  # -48300
#     print(highload - moscowpython)  # 48300
#     print(moscowpython > highload)  # False
#     print(moscowpython >= highload)  # False
#     print(moscowpython < highload)  # True
#     print(moscowpython <= highload)  # True
#     print(moscowpython == highload)  # False
from src.video import Video, PLVideo

if __name__ == '__main__':
    # Создаем два экземпляра класса
    video1 = Video('AWX4JnAnjBE')  # 'AWX4JnAnjBE' - это id видео из ютуб
    video2 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')
    assert str(video1) == 'GIL в Python: зачем он нужен и как с этим жить'
    assert str(video2) == 'MoscowPython Meetup 78 - вступление'
