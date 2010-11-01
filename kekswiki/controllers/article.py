import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from kekswiki.lib.base import BaseController, render
from kekswiki.model import Article

import kekswiki.lib.helpers as h

log = logging.getLogger(__name__)

class ArticleController(BaseController):

    def index(self, title):
        article = Article(title)
        c.title = article.get_title()
        c.content = article.get_content()
        return render('/article.mako')

    def commit(self, title):
        pass

    def edit(self, title):
        article = Article(title)
        c.title = article.get_title()
        c.content = article.get_content()
        return render('/article-edit.mako')

    def preview(self, title):
        c.title = title
        c.content = request.GET['article-text']
        return render('/article-preview.mako')
