

def application(environ, start_response):
    """
    Reference: http://wsgi.tutorial.codepoint.net/application-interface
    :environ        -- CGI environment variables.
    :start_response -- a callback function supplied by the server which takes
                       the HTTP status and headers as arguments.
    """
    message = b'li8 web framework'
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [message]


def not_found(environ, start_response):
    message = b'Page that you looking found was not found.'
    start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
    return [message]
