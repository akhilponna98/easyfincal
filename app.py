from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Retirement Calculator
@app.route("/retirement", methods=["GET", "POST"])
def retirement():
    result = None
    if request.method == "POST":
        monthly_expense = float(request.form["monthly_expense"])
        current_age = int(request.form["current_age"])
        retirement_age = int(request.form["retirement_age"])
        life_expectancy = int(request.form["life_expectancy"])
        inflation_rate = float(request.form["inflation_rate"])
        expected_return_rate = float(request.form["expected_return_rate"])
        step_up_rate = float(request.form["step_up_rate"])

        years_to_retirement = retirement_age - current_age
        years_after_retirement = life_expectancy - retirement_age

        inflated_expense = monthly_expense * ((1 + inflation_rate) ** years_to_retirement)
        annual_expense = inflated_expense * 12
        retirement_corpus = 0

        for year in range(years_after_retirement):
            retirement_corpus += annual_expense / ((1 + expected_return_rate) ** (year + 1))

        result = retirement_corpus

    return render_template("retirement.html", result=result)

# Investment Calculator
@app.route("/investment", methods=["GET", "POST"])
def investment():
    result = None
    if request.method == "POST":
        monthly_investment = float(request.form["monthly_investment"])
        expected_return = float(request.form["expected_return"])
        investment_period = int(request.form["investment_period"])
        step_up_rate = float(request.form["step_up_rate"])

        months = investment_period * 12
        monthly_return = (1 + expected_return) ** (1/12) - 1

        total_corpus = 0
        sip = monthly_investment

        for year in range(investment_period):
            for month in range(12):
                total_corpus = (total_corpus + sip) * (1 + monthly_return)
            sip *= (1 + step_up_rate)

        result = total_corpus

    return render_template("investment.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
