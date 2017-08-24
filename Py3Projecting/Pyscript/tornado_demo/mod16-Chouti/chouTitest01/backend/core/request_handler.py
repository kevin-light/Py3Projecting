import tornado.web
from backend.sesion.session import SessionFactory

class BaseRequestHandler(tornado.web.RequestHandler):
    def initialize(self):

        self.session = SessionFactory.get_session_obj(self)
