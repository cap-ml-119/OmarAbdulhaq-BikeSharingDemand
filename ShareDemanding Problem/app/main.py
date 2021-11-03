from flask import Flask

from modelAPIroutes import PreApi
app = Flask(__name__)

app.register_blueprint(PreApi)

if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
