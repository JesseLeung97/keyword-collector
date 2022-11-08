import json

from keyword_collector.config import Config
from keyword_collector.tag_data import TagData
from datetime import datetime
from discord_logger import log_error
from constants.global_constants import GlobalConstants
from typing import List


def _file_name() -> str:
    today = datetime.today().strftime('%Y_%m_%d')
    return f"{today}_tag_data.json"


def _get_date() -> str:
    return datetime.today().strftime('%Y/%m/%d')


class FileWriter:

    def __init__(self, config: Config):
        self.config = config
        self.data: List[TagData] = []

    def add_g_news_data(self, g_news_data: List[TagData]):
        self.data.extend(g_news_data)

    def add_twitter_trending_data(self, twitter_data: List[TagData]):
        self.data.extend(twitter_data)

    def write_file(self):
        try:
            output_file_name = f"{GlobalConstants.OUTPUT_DIR}/{_file_name()}"
            with open(output_file_name, "x") as file:
                json.dump(
                    self.data,
                    file,
                    ensure_ascii=False,
                    indent=GlobalConstants.DEFAULT_JSON_INDENT,
                    sort_keys=True)
        except IOError as e:
            log_error("An IO error occurred when opening the output JSON file.", f"{e}")
            raise Exception(f"{e}")
        return
