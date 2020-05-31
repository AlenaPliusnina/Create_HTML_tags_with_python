class HTML:
    def __init__(self, output=None):
        self.output = output
        self.children = []

    def __enter__(self):
        return self

    def __exit__(self, *args):
        # Write to file
        with open(self.output, 'w') as f:
            f.write("<html>\n")
            for child in self.children:
                f.write(str(child))
            f.write("</html>")

    def __iadd__(self, other):
        self.children.append(other)
        return self









