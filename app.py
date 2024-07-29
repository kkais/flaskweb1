from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/test', methods=['POST'])
def hello():
    data = request.json
    print(data.get('name'))
    return f"Hello, {data.get('name')}!"

if __name__ == '__main__':
    app.run(port=5000, debug=True)