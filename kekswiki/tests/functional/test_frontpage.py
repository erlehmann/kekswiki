from kekswiki.tests import *

class TestFrontpageController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='frontpage', action='index'))
        # Test response...
