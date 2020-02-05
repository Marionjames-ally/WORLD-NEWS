import os


class Config:
    """
    General configuration parent class
    """
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?&category=general&apiKey=06215d0c3c1f40c2a210d167dae1a44c'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    NEWS_ARTICLES_API_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    SOURCE_ARTICLES_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey='


class ProdConfig(Config):
    """
    Production configuration child class
    Args:
        Config:The parent configuration class with General configuration settings
    """


class DevConfig(Config):
    """
    Development configuration child class
    Args:
       Config:The parent configuration class with General configuration settings
    """
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
