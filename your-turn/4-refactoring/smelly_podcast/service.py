import requests
from xml.etree import ElementTree
from collections import namedtuple

Episode = namedtuple('Episode', 'title link pubdate show_id')
episode_data = {}


def download_episodes():
    url = 'https://talkpython.fm/episodes/rss'
    resp = requests.get(url)
    resp.raise_for_status()

    dom = ElementTree.fromstring(resp.text)
    episode_count = len(dom.findall('channel/item'))

    for idx, item in enumerate(dom.findall('channel/item')):
        episode = Episode(
            item.find('title').text,
            item.find('link').text,
            item.find('pubDate').text,
            episode_count - idx - 1
        )
        episode_data[episode.show_id] = episode


def show_id_latest():
    return max(episode_data.keys())


def get_episodes(show_id):
    return episode_data.get(show_id)

