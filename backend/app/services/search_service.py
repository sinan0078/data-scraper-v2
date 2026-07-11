
from app.sources.reddit.adapter import RedditAdapter
from app.sources.hackernews.adapter import HackerNewsAdapter
from app.sources.blogs.adapter import BlogAdapter

class SearchService:
    def __init__(self):
        self.sources = [RedditAdapter(), HackerNewsAdapter(), BlogAdapter()]
