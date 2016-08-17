from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def shit_o_lator():
    return render_template('shit-o-lator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get the form data
    dig1 = request.form['dig1']
    dig2 = request.form['dig2']
    oper = request.form['oper']

    # check whether digits
    try:
        float(dig1)
        float(dig2)
    except (ValueError):
        return render_template('shit-o-lator.html', message = "Please, input the digits!")
    # Check dividing on zero
    try:
        float(dig1) / float(dig2)
    except (ZeroDivisionError):
        return render_template('shit-o-lator.html', message = "You can't divide on zero!")

    # Calculation
    oper_kind = {'+': float(dig1) + float(dig2),
                 '-': float(dig1) - float(dig2),
                 '*': float(dig1) * float(dig2),
                 '/': float(dig1) / float(dig2)}
    for n in oper_kind:
        if n == oper:
            summ = oper_kind[n]

    if summ - int(summ) == 0:
        message = "The result is: {}".format(int(summ))
    else:
        message = "The result is: {0:.2f}".format(summ)
    # Output
    return render_template('shit-o-lator.html', message = message)

if __name__ == '__main__':
    app.run()
