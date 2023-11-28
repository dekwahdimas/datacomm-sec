from flask import Flask, jsonify, request, render_template


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    global t1, t2
    if(request.method == 'GET'):
        t3 = t1 - t2
        data = {
            't1': t1,
            't2': t2,
            't3': t3,
        }
        return render_template('index.html', context=data)
    else:
        return render_template('error_page.html')


t1 = 0
@app.route('/temperature_1', methods=['GET', 'POST'])
def receiveTemp1():
    global t1
    if request.method == 'POST':
        t1 = request.json.get('t1', 0)
        print(t1)
    return jsonify({
        't1': t1
    })


t2 = 0
@app.route('/temperature_2', methods=['GET', 'POST'])
def receiveTemp2():
    global t2
    if request.method == 'POST':
        t2 = request.json.get('t2', 0)
        print(t2)
    return jsonify({
        't2': t2
    })


if __name__ == '__main__':
    app.run(debug=True)