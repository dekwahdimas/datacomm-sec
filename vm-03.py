from flask import Flask, jsonify, request, render_template
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        data = "hello world"
        return jsonify({
            'data': data
        })

@app.route('/home/<int:num>', methods=['GET'])
def disp(num):
    return jsonify({
        'data': num**2
    })

@app.route('/temperature_1', methods=['GET','POST'])
def receiveTemp1():
    t1 = request.json
    print(t1)
    return jsonify({
        't1': t1
    })
    
@app.route('/temperature_2', methods=['GET','POST'])
def receiveTemp2():
    if (request.method == 'POST'):
        t2 = request.json
        print(t2)
        return t2
    elif (request.method == 'GET'):
        t2 = request.args
        print(f"T2 >>> {t2}")
        return render_template('index.html', t2=t2) 


if __name__ == '__main__':
    app.run(debug=True)