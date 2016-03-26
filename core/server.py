from .utils import get_template


class Li8App(object):

    def __call__(self, environ, start_response):
        """
        Reference: http://wsgi.tutorial.codepoint.net/application-interface
        :environ        -- CGI environment variables.
        :start_response -- a callback function supplied by the server which takes
                           the HTTP status and headers as arguments.
        """
        start_response('200 OK', [('Content-Type', 'text/html')])
        with open(get_template('default.html')) as template:
            return [template.read().encode()]


class Li8NotFoundApp(Li8App):

    def __call__(self, environ, start_response):
        start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
        with open(get_template('404.html')) as template:
            return [template.read().encode()]
