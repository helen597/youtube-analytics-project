import pytest
from src.video import Video, PLVideo


@pytest.fixture
def video1():
    return Video('AWX4JnAnjBE')


@pytest.fixture
def video2():
    return PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')


def test_video_init(video1):
    assert video1.video_id == "AWX4JnAnjBE"


def test_video_init(video2):
    assert video2.video_id == "4fObz_qw9u4"
    assert video2.playlist_id == "PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC"


def test_video_to_json(video1):
    assert video1.to_json('video1.json') == None


def test_video_str(video1, video2):
    assert str(video1) == "GIL в Python: зачем он нужен и как с этим жить"
    assert str(video2) == "MoscowPython Meetup 78 - вступление"
