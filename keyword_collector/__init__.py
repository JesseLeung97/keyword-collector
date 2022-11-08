from keyword_collector.config import Config
from keyword_collector.file_writer import FileWriter
from keyword_collector.data_fetcher import DataFetcher


def main():
    print("Welcome to the keyword collector")
    config = Config()
    file_writer = FileWriter(config)
    data_fetcher = DataFetcher(config)

    g_news_tag_data = data_fetcher.get_google_news_headlines()
    twitter_tag_data = data_fetcher.get_twitter_hashtags()

    file_writer.add_g_news_data(g_news_tag_data)
    file_writer.add_twitter_trending_data(twitter_tag_data)
    file_writer.write_file()


if __name__ == "__main__":
    main()
