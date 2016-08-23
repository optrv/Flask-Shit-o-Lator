from flask import Flask, render_template, request
from decimal import Decimal, InvalidOperation

app = Flask(__name__, static_url_path='/static')

class EmptyFieldError(Exception):
    """Raise when the input field is empty"""

class DivZeroError(Exception):
    """Raise when dividing on zero"""

@app.route('/')
def shit_o_lator():
    return render_template('shit-o-lator.html')

@app.route('/calculate', methods = ['POST'])
def calculate():
    """Get the form data"""
    digit1 = request.form['digit1']
    digit2 = request.form['digit2']
    operation = request.form['operation']

    try:
        # Check whether the fields are not empty
        if digit1 == "" or digit2 == "":
            raise EmptyFieldError("EmptyFieldError")

        # Check dividing on zero
        if operation == '/' and digit2 == '0':
            raise DivZeroError("DivZeroError")

        # Check whether digits
        digit1 = Decimal(digit1)
        digit2 = Decimal(digit2)

    except (EmptyFieldError, DivZeroError, InvalidOperation) as exception:
        return render_template('message.html', exception = exception.args[0])

   # Calculation
    operation_kind = {'+': lambda digit1, digit2: digit1 + digit2,
                      '-': lambda digit1, digit2: digit1 - digit2,
                      '*': lambda digit1, digit2: digit1 * digit2,
                      '/': lambda digit1, digit2: digit1 / digit2}

    summ = operation_kind[operation](digit1, digit2)

    # Output
    message = "{0:.4g}".format(summ)
    return render_template('message.html', message = message)

if __name__ == '__main__':
    app.run()
