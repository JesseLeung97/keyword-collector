from dotenv import load_dotenv, find_dotenv
from constants.environment_variables import ENV
from os import getenv
from discord_logger import log_error


class Config:
    def __init__(self):
        env = find_dotenv()
        if env == '':
            log_error("There was no .env file found in keyword_collector.  Execution halted.")
            raise Exception("No .env file found.")

        if not load_dotenv(env):
            log_error("There are no environment variables set in the .env file found in "
                      "keyword_collector.  Execution halted.")
            raise Exception("There are no environment variables set in the .env file.")

        self.g_news_api_key = getenv(ENV.G_NEWS_API_KEY)
        self.json_out_dir = getenv(ENV.JSON_OUT_DIR)
        self.twitter_api_key = getenv(ENV.TWITTER_API_KEY)
        self.twitter_api_key_secret = getenv(ENV.TWITTER_API_KEY_SECRET)
        self.twitter_bearer_token = getenv(ENV.TWITTER_BEARER_TOKEN)
