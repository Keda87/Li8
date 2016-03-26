from __future__ import print_function
from wsgiref.simple_server import make_server

from core.server import Li8App


if __name__ == '__main__':
    application = Li8App()
    # Example to using middleware
    # application = ErrorMiddleware(app=application)
    try:
        httpd = make_server('127.0.0.1', 8081, application)
        banner = 'Li8 web framework, running at %s:%d\n'\
                 'version 0.0.0 (Bleeding edge)\n'\
                 'Stop the server with Ctrl + C\n' % httpd.server_address
        print(banner)
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Bye..')

