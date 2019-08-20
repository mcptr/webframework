from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server


def simple_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]

    start_response(status, headers)
    return ""


httpd = make_server('', 8000, simple_app)
print("Serving on port 8000...")
httpd.serve_forever()
