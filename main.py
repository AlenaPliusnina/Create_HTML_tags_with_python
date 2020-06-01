""" Adding html code to a file test.html (Добавление кода html в файл test.html) or output it to the console
    Добавление html кода в файл test.html или вывод его в консоль
    
<html>
<head>
  <title>hello</title>
</head>
<body>
    <h1 class="main-text">Test</h1>
    <div class="container container-fluid" id="lead">
        <p>another test</p>
        <img src="/icon.png" data-image="responsive"/>
    </div>
</body>
</html>

"""

from HTML import HTML
from Tag import Tag
from TopLevelTag import TopLevelTag


if __name__ == "__main__":
    # If you want to add html code to the file (test.html) replace output=None with output="test.html"
    # Если Вы хотите добавить html код в файл (test.html) замените output=None на output="test.html"
    with HTML(output=None) as doc:
        with TopLevelTag("head") as head:
            with Tag("title") as title:
                title.text = "hello"
                head += title
                doc += head

                with TopLevelTag("body") as body:
                    with Tag("h1", klass=("main-text",)) as h1:
                        h1.text = "Test"
                        body += h1

                    with Tag("div", klass=("container", "container-fluid"), id="lead") as div:
                        with Tag("p") as paragraph:
                            paragraph.text = "another test"
                            div += paragraph

                        with Tag("img", is_single=True, src="/icon.png", data_image="responsive") as img:
                            div += img

                    body += div
                doc += body






