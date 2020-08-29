#coding: utf-8

from flask import Flask

app = Flask(__name__)

# 跨域支持
def after_request(resp):
    resp.headers["Access-Control-Allow-Origin"] = '*'
    return resp

app.after_request(after_request)

@app.route('/')
def hello_world():
    return "就是用来测试的"

@app.route('/test2', methods=['POST'])
def hello_post():
    return "Hello Ajax Post"
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=7777
    )
