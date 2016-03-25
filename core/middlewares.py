

class ErrorMiddleware(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        status = '500 INTERNAL SERVER ERROR'
        start_response(status, [('Content-Type', 'text/html')])
        yield 'Unknown error occured'
