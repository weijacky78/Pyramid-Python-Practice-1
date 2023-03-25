from wsgiref.simple_server import make_server
from pyramid.config import Configurator

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('home', '/')
        config.add_route('hello', '/howdy')
        config.add_route('redirect', '/goto')
        config.add_route('exception', '/problem')
        config.include('pyramid_chameleon')
        config.scan('views')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
