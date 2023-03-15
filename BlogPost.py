class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.posts = []


class BlogPost:
    def __init__(self, title, subtitle, body):
        self.title = title
        self.subtitle = subtitle
        self.body = body


new_user = User(
    name="Angela",
    email="angela@email.com",
    password=123456
)
