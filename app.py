from flask import Flask
import requests


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/<approval_url>')
def approval_url(approval_url):
    if approval_url is None:
        print("NONE_APPROVAL_URL")
        return 'OK'
    return(
        requests.Post(
            approval_url,
            data="{'data':'ok'}"
        )
    )

if __name__ == '__main__':
    app.run()
