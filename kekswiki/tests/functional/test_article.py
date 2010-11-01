from kekswiki.tests import *

class TestArticleController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='article', action='index'))
        # Test response...
