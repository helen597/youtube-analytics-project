import pytest
from src.playlist import PlayList
import isodate
from datetime import timedelta


@pytest.fixture
def playlist1():
    return PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')

def test_playlist_init(playlist1):
    assert playlist1.title == "Moscow Python Meetup №81"
    assert playlist1.url == "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"
    assert playlist1.total_duration == isodate.parse_duration("PT1H49M52S")

def test_playlist_total_duration(playlist1):
    duration = playlist1.total_duration
    assert str(duration) == "1:49:52"
    assert isinstance(duration, timedelta)
    assert duration.total_seconds() == 6592.0
    # playlist1.total_duration = timedelta()
    # assert playlist1.total_duration == isodate.parse_duration("PT0M0S")

def test_playlist_show_best_video(playlist1):
    assert playlist1.show_best_video() == "https://youtu.be/cUGyMzWQcGM"
