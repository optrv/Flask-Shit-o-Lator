from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def shit_o_lator():
    return render_template('shit-o-lator.html')

@app.route('/calculate', methods = ['POST'])
def calculate():
    # Get the form data
    digit1 = request.form['digit1']
    digit2 = request.form['digit2']
    operation = request.form['operation']

    # Check whether digits & dividing on zero
    try:
        digit1 = float(digit1)
        digit2 = float(digit2)
        digit1 / digit2
    except (ValueError, ZeroDivisionError) as exc:
        if str(type(exc)) == "<type 'exceptions.ValueError'>":
            return render_template('message.html', message = "Please, input the digits!")
        else:
            return render_template('message.html', message = "You can't divide on zero!")

    # Calculation
    operation_kind = {'+': digit1 + digit2,
                      '-': digit1 - digit2,
                      '*': digit1 * digit2,
                      '/': digit1 / digit2}
    for n in operation_kind:
        if n == operation:
            summ = operation_kind[n]

    # Check wether the result is integer
    if summ - int(summ) == 0:
        message = "The result is: {}".format(int(summ))
    else:
        message = "The result is: {0:.3f}".format(summ)
    # Output
    return render_template('message.html', message = message)

if __name__ == '__main__':
    app.run()
