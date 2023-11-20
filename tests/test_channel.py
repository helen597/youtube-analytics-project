import pytest
from src.channel import Channel


@pytest.fixture
def channel1():
    return Channel('UC-OVMPlMA3-YCIeg4z5z23A')


@pytest.fixture
def channel2():
    return Channel('UC-b89a0Fw6pNoP-g-_qLeiw')


@pytest.fixture
def dict1():
    return r'''{
    "kind": "youtube#channelListResponse",
    "etag": "tBDRT3nNevoPM5PpFtMU0Ky1HKs",
    "pageInfo": {
    "totalResults": 1,
    "resultsPerPage": 5
    },
  "items": [
    {
      "kind": "youtube#channel",
      "etag": "rCpK6CMfwieTDVto_nGPXJHfICw",
      "id": "UC-OVMPlMA3-YCIeg4z5z23A",
      "snippet": {
        "title": "MoscowPython",
        "description": "Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\nПрисоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)",
        "customUrl": "@moscowdjangoru",
        "publishedAt": "2012-07-13T09:48:44Z",
        "thumbnails": {
          "default": {
            "url": "https://yt3.ggpht.com/ytc/APkrFKaVrRJTNkDjSnvpVAYDqbQ5S1VMHWaZhOauk5M10Q=s88-c-k-c0x00ffffff-no-rj",
            "width": 88,
            "height": 88
          },
          "medium": {
            "url": "https://yt3.ggpht.com/ytc/APkrFKaVrRJTNkDjSnvpVAYDqbQ5S1VMHWaZhOauk5M10Q=s240-c-k-c0x00ffffff-no-rj",
            "width": 240,
            "height": 240
          },
          "high": {
            "url": "https://yt3.ggpht.com/ytc/APkrFKaVrRJTNkDjSnvpVAYDqbQ5S1VMHWaZhOauk5M10Q=s800-c-k-c0x00ffffff-no-rj",
            "width": 800,
            "height": 800
          }
        },
        "localized": {
          "title": "MoscowPython",
          "description": "Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\nПрисоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)"
        },
        "country": "RU"
      },
      "statistics": {
        "viewCount": "2454741",
        "subscriberCount": "26700",
        "hiddenSubscriberCount": false,
        "videoCount": "720"
      }
    }
  ]
}'''


def test_channel_init(channel1):
    assert channel1.channel_id == "UC-OVMPlMA3-YCIeg4z5z23A"


def test_channel_init(channel2):
    assert channel2.channel_id == "UC-b89a0Fw6pNoP-g-_qLeiw"


def test_channel_printj(dict1):
    assert Channel.printj(dict1) == None


def test_channel_print_info(channel1):
    assert channel1.print_info() == None


def test_channel_to_json(channel1):
    assert channel1.to_json('channel1.json') == None


def test_channel_str(channel1, channel2):
    assert str(channel1) == "MoscowPython(https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)"
    assert str(channel2) == "sndk(https://www.youtube.com/channel/UC-b89a0Fw6pNoP-g-_qLeiw)"


def test_channel_add(channel1, channel2):
    assert channel1.subscriber_count == 26800
    assert channel2.subscriber_count == 7680000
    assert channel1.subscriber_count + channel2. subscriber_count == 7706800
    assert channel1 + channel2 == 7706800


def test_channel_sub(channel1, channel2):
    assert channel1 - channel2 == -7653200
    assert channel2 - channel1 == 7653200


def test_channel_compare(channel1, channel2):
    assert (channel1 < channel2) == True
    assert (channel1 <= channel2) == True
    assert (channel1 > channel2) == False
    assert (channel1 >= channel2) == False
    assert (channel1 == channel2) == False
