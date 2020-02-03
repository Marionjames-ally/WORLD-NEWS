import urllib.request, json
from .models import Sources

# Getting api key
api_key = None
# Getting the movie base url
base_url = None


def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_sources(category):
    """
    function that gets the json to respond to our requests
    :param category:
    :return:
    """
    get_sources_url = base_url.format(category, api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None
        if get_sources_response['results']:
            sources_results_list = get_sources_response['results']
            sources_results = process_results(sources_results_list)

        return sources_results


def process_results(sources_list):
    """
    Function  that processes the sources result and transform them to a list of Objects
    :return:a list of sources objects
    """
    sources_results = []
    for sources_item in sources_list:
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')
        sources_object = Sources(name, description, url)
        sources_results.append(sources_object)

    return sources_results
