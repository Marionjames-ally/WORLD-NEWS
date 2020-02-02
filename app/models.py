class Sources:
    """
    Sources class to define the sources objects
    """

    def __init__(self, name, description, url, language):
        self.name = name
        self.description = description
        self.url = url


class Articles:
    """
    article class to define the articles object
    """

    def __init__(self, title, author, urlToImage, description,url, content):
        self.url = url
        self.content = content
        self.description = description
        self.title = title
        self.author = author
        self.urlToImage = urlToImage
