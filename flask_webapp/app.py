from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
   respbody = {
      'abb': 122,
      'ccc': 333,
   }
   return jsonify(respbody)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=True)
