from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('workslist.html', result=result)

@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/areaOfcirle', methods=['GET', 'POST'])
def areaOfCircle():
    result = None
    if request.method == 'POST':
        input_radius = request.form.get('inputRadius', '')
        
        if input_radius.isdigit():
            result = 3.14*(int(input_radius)** 2)
        else:
            result = "PLEASE ENTER A VALID INTEGER"
    return render_template('areaofcircle.html', result=result)

@app.route('/areaOfTriangle', methods=['GET', 'POST'])
def areaOfTriangle():
    result = None
    if request.method == 'POST':
        input_base = request.form.get('inputBase', '')
        input_height = request.form.get('inputHeight', '')

        if input_base.isdigit() and input_height.isdigit():
            result = ((int(input_height) * int(input_base)))/2

        else:
            result = "PLEASE ENTER A VALID INTEGER"
    return render_template('areaoftriangle.html', result=result)


@app.route('/contact')
def contact():
    return render_template('contact.html')

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []

    def is_operand(ch):
        return ch.isalnum()

    for ch in expression:
        if ch == ' ':
            continue
        if is_operand(ch):
            output.append(ch)
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while (stack and stack[-1] != '(' and
                   precedence.get(ch, 0) <= precedence.get(stack[-1], 0)):
                output.append(stack.pop())
            stack.append(ch)
    while stack:
        output.append(stack.pop())
    return ' '.join(output)

@app.route('/stackPostFix', methods=['GET', 'POST'])
def stackPostFix():
    result = None
    if request.method == 'POST':
        infix_expr = request.form.get('inputString')
        if infix_expr:
            result = infix_to_postfix(infix_expr)
    return render_template('stackPostFix.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
