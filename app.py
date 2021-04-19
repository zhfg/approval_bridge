from flask import Flask, request
import requests


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/approval')
def approval_url():
    approval_url = request.args.get('url')
    print("get url:", approval_url)
    if approval_url is None:
        print("NONE_APPROVAL_URL")
        return 'OK'
    req = requests.post(
        approval_url,
        data="{'data':'ok'}"
    )

    return str(req.status_code)


if __name__ == '__main__':
    app.run()
