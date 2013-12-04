"""
Mock LTI server for manual testing.
"""

import threading
from mock_lti_server import MockLTIServer

server_port = 8034
server_host = 'localhost'
address = (server_host, server_port)

server = MockLTIServer(address)
server.oauth_settings = {
    'client_key': 'test_client_key',
    'client_secret': 'test_client_secret',
    'lti_base':  'http://{}:{}/'.format(server_host, server_port),
    'lti_endpoint': 'correct_lti_endpoint'
}
server.server_host = server_host

#flag for acceptance tests used for creating right callback_url
server.test_mode = True

try:
    server.serve_forever()
except KeyboardInterrupt:
    print('^C received, shutting down server')
    server.socket.close()
