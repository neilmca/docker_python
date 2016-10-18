import webapp2
import logging
import sys

class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
    	logging.info('neil serving url = tb')
    	sys.stdout.write('stdout logged line')
        self.response.write('Hello, webapp2!')

app = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
], debug=True)

logging.getLogger().setLevel(logging.DEBUG)

def main():
    from paste import httpserver
    # Bind to all addresses (i.e. 0.0.0.0), otherwise the world outside this
    # Docker container won't be able to see the server
    #Running locally can still use 127.0.0.1 without change
    httpserver.serve(app, host='0.0.0.0', port='8080')

if __name__ == '__main__':
    main()