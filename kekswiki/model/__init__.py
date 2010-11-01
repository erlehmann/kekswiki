from dulwich.repo import Repo
from dulwich.objects import Blob, Tree, Commit, parse_timezone

class Article(object):
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title

    def get_content(self):
        return '<h1>hurr durr</h1><p>Bla from dulwich.objects import Blob, Tree, Commit, parse_timezone from dulwich.objects import Blob, Tree, Commit, parse_timezone from dulwich.objects import Blob, Tree, Commit, parse_timezone from dulwich.objects import Blob, Tree, Commit, parse_timezone from dulwich.objects import Blob.</p><p>Bla from dulwich.objects import Blob, Tree, Commit, parse_timezone from dulwich.objects import Blob, Tree, Commit, parse_timezone from dulwich.objects import Blob, Tree, Commit, parse_timezone from dulwich.objects import Blob, Tree, Commit, parse_timezone from dulwich.objects import Blob.</p><h1>blupp</h1><p>Dies ist <b style="color:red;">ein Test</b>.<script>evil();</script>\n    < << + ++ > >> - -- &lt; &gt; &amp;</p>'

    def get_title(self):
        return self.title

    def update_content(self, new_content):
        pass

    def update_title(self, new_title):
        pass
