import urllib.request, json
from .models import Sources, Articles


def configure_request(app):
    global api_key, s_url, art_url
    api_key = app.config['NEWS_API_KEY']
    s_url = app.config['NEWS_API_BASE_URL']
    art_url = app.config['NEWS_ARTICLES_API_URL']


def get_sources(category):
    """
    Function that gets the response from json to the url request
    """

    get_sources_url = s_url.format(category, api_key)

    # get_sources_response = requests.get(get_sources_url).json()
    with urllib.request.urlopen(get_sources_url) as url:
        sources_data = url.read()
        sources_response = json.loads(sources_data)

        # get_sources_response = None

        if sources_response.get('sources'):
            sources_results_items = sources_response.get('sources')
            sources_results = process_new_sources(sources_results_items)
            return sources_results


def process_new_sources(sources_list):
    """
    Function that processes the sources result and transform them to a list of Objects
    Args:
    source_list:A list of dictionaries that contain source details
    Returns:
        sources_results: A list of sources objects
    """
    sources_results = []

    for one_source_item in sources_list:
        name = one_source_item.get('name')
        id = one_source_item.get('id')
        url = one_source_item.get('url')
        category = one_source_item.get('category')
        language = one_source_item.get('language')
        country = one_source_item.get('country')
        description = one_source_item.get('description')

        new_source = Sources(name, id, url, category, language, country, description)
        sources_results.append(new_source)
    return sources_results


def get_articles(articles):
    """
    Function that will get the news articles
    """
    articles_url = art_url.format(articles, api_key)
    with urllib.request.urlopen(articles_url) as url:
        articles_data = url.read()
        articles_response = json.loads(articles_data)

        articles_results = None

        if articles_response['articles']:
            articles_results_items = articles_response['articles']
            articles_results = process_new_articles(articles_results_items)
        return articles_results


def process_new_articles(articles_list):
    """
    Function that processes the new articles and puts them in an array
    """
    articles_results = []

    for one_article in articles_list:
        title = one_article.get('title')
        url = one_article.get('url')
        description = one_article.get('description')
        author = one_article.get('author')
        urlToImage = one_article.get('urlToImage')
        publishedAt = one_article.get('publishedAt')
        new_article = Articles(title, url, description, author, urlToImage, publishedAt)
        articles_results.append(new_article)

    return articles_results