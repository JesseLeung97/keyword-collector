import os.path


def get_root_dir() -> str:
    return os.path.dirname(os.path.abspath(os.curdir))


class GlobalConstants:
    HTTP_RESPONSE_OK = 200
    DEFAULT_JSON_INDENT = 4
    ROOT_DIR = get_root_dir()
    OUTPUT_DIR = f"{get_root_dir()}/tag_data_json"
    SOURCE_G_NEWS = "Google News"
    SOURCE_TWITTER = "Twitter"
    G_NEWS_HEADLINES_US = "https://newsapi.org/v2/top-headlines?country=us&apiKey="
    TWITTER_HASHTAGS_US = "https://api.twitter.com/1.1/trends/place.json?id=23424977"


