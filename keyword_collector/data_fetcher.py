import json

import requests

from constants.global_constants import GlobalConstants
from discord_logger import log_error
from tag_data import TagData
from datetime import datetime
from config import Config
from typing import List


def _get_date() -> str:
    return datetime.today().strftime('%Y/%m/%d')


def _convert_google_news_to_tag_data(json_data: str) -> List[TagData]:
    tag_data_list: List[TagData] = []
    for article in json_data["articles"]:
        title = article["title"].rsplit('-', 1)[0]
        title = title.rsplit('|', 1)[0]

        tag_data = TagData(GlobalConstants.SOURCE_G_NEWS, _get_date(), title)
        tag_data_list.append(tag_data.to_dict())

    return tag_data_list


def _convert_twitter_hashtags_to_tag_data(json_data: str) -> List[TagData]:
    tag_data_list: List[TagData] = []
    for hashtag in json_data[0]["trends"]:
        name = hashtag["name"]
        if name[0] == "#":
            name = name[1:]

        tag_data = TagData(GlobalConstants.SOURCE_TWITTER, _get_date(), name)
        tag_data_list.append(tag_data.to_dict())

    return tag_data_list


class DataFetcher:
    def __init__(self, config: Config):
        self.config = config

    def _get_google_news_headlines(self) -> str:
        response = requests.get(f"{GlobalConstants.G_NEWS_HEADLINES_US}{self.config.g_news_api_key}")
        if response.status_code != GlobalConstants.HTTP_RESPONSE_OK:
            log_error(
                error_message="There was an HTTP error when connecting to the Google News API.",
                stack_trace=json.dumps(response.json(), indent=GlobalConstants.DEFAULT_JSON_INDENT))
            raise Exception("There was an HTTP error when connecting to the Google News API.")

        return response.json()

    def get_google_news_headlines(self) -> List[TagData]:
        data = self._get_google_news_headlines()
        if data is None:
            log_error("No data was returned from Google News.")
            raise Exception("No data was returned from Google News.")

        tag_data = _convert_google_news_to_tag_data(data)

        return tag_data

    def _get_twitter_hashtags(self) -> List[TagData]:
        headers = {"Authorization": f"Bearer {self.config.twitter_bearer_token}"}
        response = requests.get(f"{GlobalConstants.TWITTER_HASHTAGS_US}", headers=headers)
        if response.status_code != GlobalConstants.HTTP_RESPONSE_OK:
            log_error(
                error_message="There was an HTTP error when connecting to the Twitter API.",
                stack_trace=json.dumps(response.json(), indent=GlobalConstants.DEFAULT_JSON_INDENT))
            raise Exception("There was an HTTP error when connecting to the Twitter API.")

        return response.json()

    def get_twitter_hashtags(self) -> List[TagData]:
        data = self._get_twitter_hashtags()
        if data is None:
            log_error("No data was returned from Twitter.")
            raise Exception("No data was returned from Twitter.")

        tag_data = _convert_twitter_hashtags_to_tag_data(data)

        return tag_data







