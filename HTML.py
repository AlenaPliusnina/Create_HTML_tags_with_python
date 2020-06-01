class HTML:
    def __init__(self, output=None):
        self.output = output
        self.children = []

    def __enter__(self):
        return self

    def __exit__(self, *args):
        # Write to file (Запись в файл)
        if self.output is not None:
            with open(self.output, 'w') as f:
                f.write("<html>\n")
                for child in self.children:
                    f.write(str(child))
                f.write("</html>")
        # Print to console (Вывод на консоль)
        else:
            html = "<html> \n"
            for child in self.children:
                html += str(child)
            html += "</html>"
            print(html)

    def __iadd__(self, other):
        self.children.append(other)
        return self











