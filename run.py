from app import app
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer

# app.run(host='0.0.0.0')
#app.run(debug=True)

http_server = WSGIServer(('',5000), app, handler_class=WebSocketHandler)
http_server.serve_forever()