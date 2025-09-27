import os, re

BLOG_HTML = """
<!DOCTYPE html>
<html lang="en">

<head>
    <base href="../../../" />

    <meta charset="utf-8" />
    <meta content="width=device-width, initial-scale=1, viewport-fit=cover" name="viewport" />
    <title>{title} | zydezu.com</title>
    <meta content="{description}" name="description">
    <link rel="icon" href="https://zydezu.com/assets/favicon.jpg" type="image/jpg">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/blogpage.css">
    <link rel="stylesheet" href="css/bgvideo.css">

    <meta content="{title} | zydezu.com" property="og:title" />
    <meta content="website" property="og:type" />
    <meta content="https://zydezu.com/" property="og:url" />
    <meta content="https://zydezu.com/assets/favicon.jpg" property="og:image" />
    <meta content="{description}" property="og:description" />
    <meta content="#3fa0f5" name="theme-color" />
    <meta content="summary_large_image" name="twitter:card" />

    <script src="scripts/p3animation.js" type="module"></script>
</head>

<body>
    <div id="blurred-glass-pane"></div>
    <img src="assets/bg/p3rbg.avif" class="page-bg-video">

    <div class="blog">
        <a href="">Back</a>
        <h1>{title} ({date}) {tags}</h1>
        <div class="blog-contents">
            {content}
        </div>
    </div>
</body>
</html>
"""

class Blog:
    def __init__(self, title, date):
        self.title = title
        self.date = date

    def __str__(self):
        return f"{self.title} ({self.date}) {f"{self.tags}" if self.tags else ""}\n{self.description if self.description else ""}\n\n{self.content if self.content else ""}"

    def add_description(self, description):
        self.description = description

    def add_tags(self, tags):
        self.tags = tags.split(",")

    def add_content(self, content):
        self.content = content

    def create_html(self, path):
        html_file_path = os.path.join(path, "index.html")

        def replace_img(match):
            src = match.group(1)
            alt = match.group(2)
            return f'<img src="{os.path.join(path, src).replace("\\","/")}" class="image" alt="{alt}">'

        pattern = re.compile(r'\[!img\|([^|]+)\|([^\]]+)\]')
        self.replaced_content = pattern.sub(replace_img, self.content)

        with open(html_file_path, "w") as f:
            html_string =  (BLOG_HTML
                .replace("{title}", self.title)
                .replace("{date}", self.date)
                .replace("{tags}", str(self.tags))
                .replace("{description}", self.description)
                .replace("{content}", self.replaced_content)
            )

            f.writelines(
                html_string
            )

def create_article(file):
    with open(file) as f:
        data = f.readlines()

    if len(data) < 3:
        print("File malformed!")

    article = Blog(data[0].strip(), data[1].strip())
    startofcontent = False
    content = ""

    for i, line in enumerate(data):
        if i == 2:
            article.add_description(line.strip())
        elif i == 3:
            article.add_tags(line.strip())
        elif i > 3:
            if startofcontent:
                content += line
            startofcontent = True

    article.add_content(content)
    article.create_html(os.path.dirname(file))

def main():
    blog_articles = []

    for path, subdirs, files in os.walk("blog"):
        for name in files:
            if name.split(".")[-1] == "zyblog":
                blog_articles.append(create_article(os.path.join(path, name)))

if __name__ == "__main__":
    main()