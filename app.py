from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None

    if request.method == "POST":
        try:
            x = float(request.form.get("x"))
            y = request.form.get("y")
            operation = request.form.get("operation")

            if y:
                y = float(y)

            if operation == "add":
                result = x + y
            elif operation == "sub":
                result = x - y
            elif operation == "mul":
                result = x * y
            elif operation == "div":
                result = x / y
            elif operation == "power":
                result = x ** y
            elif operation == "percent":
                result = (x / y) * 100
            elif operation == "sqrt":
                result = math.sqrt(x)
            elif operation == "log":
                result = math.log10(x)
            elif operation == "sin":
                result = math.sin(math.radians(x))
            elif operation == "cos":
                result = math.cos(math.radians(x))
            elif operation == "tan":
                result = math.tan(math.radians(x))

        except:
            result = "Invalid Input"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

    
