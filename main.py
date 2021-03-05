from flask import Flask,  json, request

app = Flask(__name__)

'''
@app.route("/")
def home():
    return render_template("home.html")
    
# @app.route('/', methods=['PUT'])
# @app.route('/', methods=['POST'])
# @app.route('/', methods=['DELETE'])
'''


@app.route('/', methods=['GET', 'POST', 'PUT'])
def index():
    res = {}
    if request.method == 'PUT' or request.method == 'POST':
        json_data = json.loads(request.data)
        for k, v in json_data.items():
            data = k
            values = list([int(x) for x in v.split(',')])
            values.sort()
            values = ','.join(map(str, values))
            res[data] = values
    else:
        res["error"] = "Please use PUT or POST for your requests..."

    return json.dumps(res)


if __name__ == "__main__":
    app.run(debug=True)

