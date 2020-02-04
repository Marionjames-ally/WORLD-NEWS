from flask import render_template, redirect, request, url_for
from ..requests import get_sources, get_articles
from . import main


@main.route('/')
def index():
    """
   A view root page function that returns the index page and its data
    """

    general_news = get_sources('general')
    sports_news = get_sources('sports')
    health_news = get_sources('health')
    business_news = get_sources('business')
    return render_template('index.html', general=general_news, sports=sports_news, health=health_news,
                           business=business_news)


@main.route('/sourceArticles/<id>')
def sourceArticles(id):
    """
   A view sourceArticles page function that returns the sourceArticles details and its data
    """
    all_articles = articles_source(id)
    source = id
    return render_template('articlessource.html', articles=all_articles, source=source)


@main.route('/news-Articles')
def newsArticles():
    """
   A view function that returns the news articles details and its data

    """
    bussiness_articles = get_articles('bussiness')
    entertainment_articles = get_articles('entertainment')
    health_articles = get_articles('health')
    return render_template('articles.html', business=bussiness_articles, entertainment=entertainment_articles,
                           health=health_articles)


