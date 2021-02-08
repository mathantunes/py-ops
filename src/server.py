from flask import Flask
server = Flask(__name__)
import sys

@server.route("/")
def hello():
   print(sys.version)
   return "Hello World!"

if __name__ == "__main__":
   server.run(host='0.0.0.0')