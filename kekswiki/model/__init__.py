from dulwich.repo import Repo
from dulwich.objects import Blob, Tree, Commit, parse_timezone

class Article(object):
    def __init__(self, title):
        self.title = title
        self.repo = Repo("wiki")

        self.head = self.repo.get_object(self.repo.head())
        self.tree = self.repo.get_object(self.head.tree)

        try:
            sha = self.tree[self.title][1]
            self.content = self.repo[sha].data
        except KeyError:
            self.content = u'Hier koennte ihre Werbung stehen.'

    def __str__(self):
        return self.title

    def get_content(self):
        return self.content

    def get_title(self):
        return self.title

    def update_content(self, new_content, author, email, message):
        # create blob, add to tree
        #blob = Blob.from_string(new_content)
        blob = Blob.from_string('lalala')
        self.tree[self.title] = (0100644, blob.id)

        # commit
        commit = Commit()
        commit.tree = self.tree.id
        commit.parents = [self.head.id]
        commit.author = commit.committer = "%s <%s>" % (author, email)
        commit.commit_time = commit.author_time = int(time())
        tz = parse_timezone('+0100')[0]  # FIXME: get proper timezone
        commit.commit_timezone = commit.author_timezone = tz
        commit.encoding = "UTF-8"
        commit.message = message

        # save everything
        object_store = self.repo.object_store
        object_store.add_object(blob)
        object_store.add_object(tree)
        object_store.add_object(commit)

        repo.refs['refs/heads/master'] = commit.id

    def update_title(self, new_title):
        pass
