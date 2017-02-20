import tornado.ioloop
import tornado.web
from tornado.template import Template
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        html = Template(open("templation/header.html", "r").read() + open("templation/index.html", "r").read() + open("templation/footer.html", "r").read()).generate(
            title="Мой блог",
            Menu_big="Главная страница",
            menus=[{'name': "Новости", 'link': "l1"}, {'name': "Статьи", 'link': "l1"}, {'name': "Обратная связь", 'link': "l1"}],
            page_head="Page head",
            posts=[{'autorname': "autor name", 'link': "l1", 'title' : 'POST1', 'date': '2012 17 10', 'preview':'Random text'} ]
        )
        self.write(html)

class PostsHandler(tornado.web.RequestHandler):
    def get(self):
        html = Template(open("templation/header.html", "r").read() + open("templation/posts.html", "r").read() + open(
            "templation/footer.html", "r").read()).generate(
            title="Мой блог",
            Menu_big="Просмотр публикации...",
            menus=[{'name': "Новости", 'link': "l1"}, {'name': "Статьи", 'link': "l1"},
                   {'name': "Обратная связь", 'link': "l1"}],
        )
        self.write(html)

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/css/(.*)", tornado.web.StaticFileHandler, {"path": r"templation/css"}),
        (r"/js/(.*)", tornado.web.StaticFileHandler, {"path": r"templation/js"}),
        (r"/images/(.*)", tornado.web.StaticFileHandler, {"path": r"templation/images"}),
        (r"/fonts/(.*)", tornado.web.StaticFileHandler, {"path": r"templation/fonts"}),
        (r"/pages", PostsHandler),
        (r"/", MainHandler),
    ])
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()