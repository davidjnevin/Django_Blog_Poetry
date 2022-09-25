import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy

from .models import Post


class LatestPostsFeed(Feed):
    title = "My blog"
    link = reverse_lazy("blog:post_list")
    description = "New posts of my blog."

    def items(self):
        """Return a list of 5 most recent published posts."""
        return Post.published.all()[:5]

    def item_title(self, item):
        """Return post title."""
        return item.title

    def item_description(self, item):
        """Return the title of the post."""
        return truncatewords_html(markdown.markdown(item.body), 30)

    def item_pubdate(self, item):
        """Return the publish date."""
        return item.publish
