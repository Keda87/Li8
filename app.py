from __future__ import print_function
from wsgiref.simple_server import make_server

from core.server import application


if __name__ == '__main__':
    try:
        httpd = make_server('127.0.0.1', 8081, application)
        banner = """
li8 web framework, running at %s:%d
version 0.0.0 (Bleeding edge)
Stop the server with Ctrl + C
""" % httpd.server_address
        print(banner)
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Bye..')

