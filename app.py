from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    num1 = float(data['num1'])
    num2 = float(data['num2'])
    operation = data['operation']
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2 if num2 != 0 else 'Error: Divide by Zero'
    elif operation == '%':
        result = num1 % num2 if num2 != 0 else 'Error: Divide by Zero'
    elif operation == '**':  # power
        result = num1 ** num2
    elif operation == '//':  # floor division
        result = num1 // num2 if num2 != 0 else 'Error: Divide by Zero'
    else:
        result = 'Invalid Operation'
    

    return jsonify({'result': result})
@app.route('/discount')
def discount_page():
    return render_template('discount.html')


@app.route('/calculate_discount', methods=['POST'])
def calculate_discount():
    data = request.get_json()
    price = float(data['price'])
    discount_percent = float(data['discount'])
    
    discounted_price = price - (price * discount_percent / 100)
    
    return jsonify({'discounted_price': discounted_price})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
