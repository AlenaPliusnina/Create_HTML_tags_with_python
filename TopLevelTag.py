class TopLevelTag:
    def __init__(self, tag):
        self.tag = tag

        self.children = []

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return self

    def __iadd__(self, other):
        self.children.append(other)
        return self

    def __str__(self):
        starting = "<{tag}> \n".format(tag=self.tag)
        internal = ""

        for child in self.children:
            internal += str(child)
        ending = "</{tag}> \n".format(tag=self.tag)

        return starting + internal + ending



