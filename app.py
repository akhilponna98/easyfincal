from flask import Flask, render_template, request

app = Flask(__name__)

# Format amount to Lakhs/Cr
def format_amount(amount):
    if amount >= 1e7:
        return f"{amount / 1e7:.1f} Cr"
    elif amount >= 1e5:
        return f"{amount / 1e5:.1f} Lakhs"
    else:
        return f"₹{amount:,.0f}"

# Home Page
@app.route("/")
def home():
    calculators = [
        {
            "title": "Investment Calculator",
            "desc": "Estimate the growth of your monthly SIP investments over time.",
            "url": "/investment",
            "icon": "bi bi-graph-up-arrow"
        },
        {
            "title": "Retirement Calculator",
            "desc": "Calculate the corpus you need to retire and live comfortably.",
            "url": "/retirement",
            "icon": "bi bi-piggy-bank"  # ✅ Updated icon here
        }
    ]

    articles = [
        {
            "title": "Why Start Investing Early?",
            "body": "Starting early gives your money more time to grow due to compounding. Even small amounts invested early can beat large amounts invested later."
        },
        {
            "title": "How Much Should I Save for Retirement?",
            "body": "A good rule is to save 25x your annual expenses. Use our Retirement Calculator to find your target corpus."
        }
    ]

    return render_template("index.html", calculators=calculators, articles=articles)

# Retirement Calculator
@app.route("/retirement", methods=["GET", "POST"])
def retirement():
    result = None
    formatted_result = None
    form_data = {}

    if request.method == "POST":
        form_data = {
            "monthly_expense": request.form["monthly_expense"],
            "current_age": request.form["current_age"],
            "retirement_age": request.form["retirement_age"],
            "life_expectancy": request.form["life_expectancy"],
            "inflation_rate": request.form["inflation_rate"],
            "expected_return_rate": request.form["expected_return_rate"]
        }

        monthly_expense = float(form_data["monthly_expense"])
        current_age = int(form_data["current_age"])
        retirement_age = int(form_data["retirement_age"])
        life_expectancy = int(form_data["life_expectancy"])
        inflation_rate = float(form_data["inflation_rate"]) / 100
        expected_return_rate = float(form_data["expected_return_rate"]) / 100

        years_to_retirement = retirement_age - current_age
        inflated_monthly_expense = monthly_expense * ((1 + inflation_rate) ** years_to_retirement)
        annual_expense_at_retirement = inflated_monthly_expense * 12

        safe_withdrawal_rate = 0.04
        retirement_corpus = annual_expense_at_retirement / safe_withdrawal_rate

        result = retirement_corpus
        formatted_result = format_amount(retirement_corpus)

    return render_template("retirement.html", result=result, formatted_result=formatted_result, form_data=form_data)

# Investment Calculator
@app.route("/investment", methods=["GET", "POST"])
def investment():
    result = None
    formatted_result = None
    invested_amount = 0
    estimated_returns = 0
    form_data = {}

    if request.method == "POST":
        form_data = {
            "monthly_investment": request.form["monthly_investment"],
            "expected_return": request.form["expected_return"],
            "investment_period": request.form["investment_period"],
            "step_up_rate": request.form["step_up_rate"]
        }

        monthly_investment = float(form_data["monthly_investment"])
        expected_return = float(form_data["expected_return"]) / 100
        investment_period = int(form_data["investment_period"])
        step_up_rate = float(form_data["step_up_rate"]) / 100

        months = investment_period * 12
        monthly_return = (1 + expected_return) ** (1 / 12) - 1

        total_corpus = 0
        invested = 0
        sip = monthly_investment

        for year in range(investment_period):
            for month in range(12):
                total_corpus = (total_corpus + sip) * (1 + monthly_return)
                invested += sip
            sip *= (1 + step_up_rate)

        estimated_returns = total_corpus - invested

        result = total_corpus
        formatted_result = format_amount(total_corpus)
        formatted_invested = format_amount(invested)
        formatted_returns = format_amount(estimated_returns)

        return render_template(
            "investment.html",
            result=result,
            formatted_result=formatted_result,
            formatted_invested=formatted_invested,
            formatted_returns=formatted_returns,
            invested_amount=round(invested),
            estimated_returns=round(estimated_returns),
            form_data=form_data
        )

    return render_template("investment.html", result=None, form_data=form_data)

if __name__ == "__main__":
    app.run(debug=True)
