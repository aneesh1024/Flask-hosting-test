import Flask from flask

app = Flask(__name__)

@app.route("/")
def index():
  return {'route':'Flask API working properly'}

if __name__ == '__main__':
  app.run(debug=True)
