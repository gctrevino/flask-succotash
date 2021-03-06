from flask import Flask,  json, request

app = Flask(__name__)


'''
@app.route("/", methods=['GET')
def home():
    return render_template("home.html")
'''


@app.route('/', methods=['GET', 'DELETE', 'POST', 'PUT'])
def index():
    res = {}
    try:
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
    except:
        res["error"] = "Please use the following json format for your requests: {'data': '0,1,2'}"

    return json.dumps(res)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

