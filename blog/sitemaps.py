from django.contrib.sitemaps import Sitemap

from .models import Post


class PostSitemap(Sitemap):
    """Set change frequence and priority relevance."""

    changefreq = "weekly"
    priority = 0.9

    def items(self):
        """return all published posts."""
        return Post.published.all()

    def lastmod(self, obj):
        """Update objects in sitemap with the last modified date."""
        return obj.updated
