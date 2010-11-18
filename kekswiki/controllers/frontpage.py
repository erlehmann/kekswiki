import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from kekswiki.lib.base import BaseController, render
from kekswiki.model import ArticleList

import kekswiki.lib.helpers as h

log = logging.getLogger(__name__)

class FrontpageController(BaseController):

    def index(self):
        list = ArticleList()
        c.titles = list.get_article_titles()
        return render('/frontpage.mako')
