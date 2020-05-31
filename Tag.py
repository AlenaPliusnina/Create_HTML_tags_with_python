class Tag:
    def __init__(self, tag, is_single=False, klass=None, **kwargs):
        self.tag = tag
        self.text = ""
        self.attributes = {}

        self.is_single = is_single
        self.children = []

        if klass is not None:
            self.attributes["class"] = " ".join(klass)

        for attr, value in kwargs.items():
            if "_" in attr:
                attr = attr.replace("_", "-")
            self.attributes[attr] = value

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def __iadd__(self, other):
        self.children.append(other)
        return self

    def __str__(self):
        attrs = []
        for attribute, value in self.attributes.items():
            attrs.append('%s="%s"' % (attribute, value))
        attrs = " ".join(attrs)

        if len(self.children) > 0:
            opening = "    <{tag} {attrs}> \n".format(tag=self.tag, attrs=attrs)
            if self.text:
                internal = "%s" % self.text
            else:
                internal = ""
            for child in self.children:
                internal += str(child)
            ending = "    </%s> \n" % self.tag
            return opening + internal + ending
        else:
            if self.is_single:
                return "        <{tag} {attrs}> \n".format(tag=self.tag, attrs=attrs)
            else:
                if attrs:
                    return "    <{tag} {attrs}>{text}</{tag}> \n".format(tag=self.tag, attrs=attrs, text=self.text)
                elif self.tag == "title":
                    return "  <{tag}>{text}</{tag}> \n".format(tag=self.tag, attrs=attrs, text=self.text)
                else:
                    return "        <{tag}>{text}</{tag}> \n".format(tag=self.tag, attrs=attrs, text=self.text)
















