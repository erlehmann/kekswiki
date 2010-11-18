from kekswiki.tests import *

class TestArticleController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='article', action='index', title='Mudkipz'))
        assert 'Mudkipz' in response

    def test_commit(self):
        assert False  # FIXME

    def test_edit(self):
        response = self.app.get(url(controller='article', action='index', title='Mudkipz'))
        assert 'Mudkipz' in response

    def test_preview(self):
        response = self.app.get(url(controller='article', action='index', title='Mudkipz'))
        assert 'Mudkipz' in response
