from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    # Print the string in the console
    print(param)
    # Display the string in the web browser
    return f'<p>Printed string: {param}</p>'

@app.route('/count/<int:param>')
def count(param):
    # Create a string containing numbers in the range of the parameter
    numbers = '\n'.join(str(i) for i in range(param + 1))
    # Display the numbers in the web browser
    return f'<pre>{numbers}</pre>'

@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Division by zero is not allowed."
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation. Supported operations: +, -, *, div, %"

    return f'<p>{num1} {operation} {num2} = {result}</p>'

if __name__ == '__main__':
    app.run(debug=True)


