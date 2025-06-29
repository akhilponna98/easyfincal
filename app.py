from flask import Flask, render_template, request

app = Flask(__name__)

# --------------------------
# 📌 Format: Rs, Lakh, Cr
# --------------------------
def format_amount(amount):
    if amount >= 1e7:
        return f"{amount / 1e7:.1f} Cr"
    elif amount >= 1e5:
        return f"{amount / 1e5:.1f} Lakhs"
    else:
        return f"₹{amount:,.0f}"

def to_readable_amount(value):
    value = float(value)
    if value >= 1e7:
        return f"{value / 1e7:.1f} Cr"
    elif value >= 1e5:
        return f"{value / 1e5:.1f} Lakhs"
    else:
        return f"₹{value:,.0f}"

# --------------------------
# Home Page
# --------------------------
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
            "icon": "bi bi-piggy-bank"
        },
        {
            "title": "Target Corpus SIP Calculator",
            "desc": "Plan how much you need to invest monthly to reach a goal corpus.",
            "url": "/target-sip",
            "icon": "bi bi-bullseye"
        },
        {
            "title": "Retirement SIP Planner",
            "desc": "Estimate your retirement corpus and calculate the SIP needed to reach it.",
            "url": "/retirement-sip",
            "icon": "bi bi-people-fill"
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
        },
        {
            "title": "The Power of Compounding",
            "body": "Compounding helps your investments grow exponentially over time. Reinvesting returns and staying invested for decades is the secret to wealth creation."
        },
        {
            "title": "Why Staying Invested Matters",
            "body": "Market volatility is normal. Staying invested through ups and downs helps you benefit from market rebounds and long-term trends."
        },
        {
            "title": "Diversify for Long-Term Success",
            "body": "Don’t put all your eggs in one basket. Diversify across asset classes and geographies to reduce risk and maximize long-term returns."
        }
    ]

    return render_template("index.html", calculators=calculators, articles=articles)

# --------------------------
# Retirement Calculator
# --------------------------
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
        inflation_rate = float(form_data["inflation_rate"]) / 100

        years_to_retirement = retirement_age - current_age
        inflated_expense = monthly_expense * ((1 + inflation_rate) ** years_to_retirement)
        annual_expense = inflated_expense * 12

        safe_withdrawal_rate = 0.04
        corpus = annual_expense / safe_withdrawal_rate

        result = corpus
        formatted_result = format_amount(corpus)

    return render_template("retirement.html", result=result, formatted_result=formatted_result, form_data=form_data)

# --------------------------
# Investment Calculator
# --------------------------
@app.route("/investment", methods=["GET", "POST"])
def investment():
    result = None
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

        return render_template(
            "investment.html",
            result=result,
            formatted_result=format_amount(total_corpus),
            formatted_invested=format_amount(invested),
            formatted_returns=format_amount(estimated_returns),
            invested_amount=round(invested),
            estimated_returns=round(estimated_returns),
            form_data=form_data
        )

    return render_template("investment.html", result=None, form_data=form_data)

# --------------------------
# Target SIP Calculator
# --------------------------
@app.route("/target-sip", methods=["GET", "POST"])
def target_sip():
    required_sip = None
    formatted_goal_amount = None
    formatted_required_sip = None
    goal_amount = None
    years = None
    annual_return = None

    form_data = {}

    if request.method == "POST":
        form_data = {
            "goal_amount": request.form["goal_amount"],
            "return_rate": request.form["return_rate"],
            "years": request.form["years"],
            "step_up_rate": request.form["step_up_rate"]
        }

        goal_amount = float(form_data["goal_amount"])
        annual_return = float(form_data["return_rate"]) / 100
        years = int(form_data["years"])
        step_up_rate = float(form_data["step_up_rate"]) / 100

        months = years * 12
        monthly_return = (1 + annual_return) ** (1 / 12) - 1

        sip = goal_amount / months

        for _ in range(1000):
            fv = 0
            sip_guess = sip
            for year in range(years):
                for month in range(12):
                    fv = (fv + sip_guess) * (1 + monthly_return)
                sip_guess *= (1 + step_up_rate)
            if abs(fv - goal_amount) < 100:
                break
            sip *= goal_amount / fv

        required_sip = sip
        formatted_goal_amount = format_amount(goal_amount)
        formatted_required_sip = format_amount(required_sip)

    return render_template(
        "target_sip.html",
        required_sip=required_sip,
        formatted_required_sip=formatted_required_sip,
        formatted_goal_amount=formatted_goal_amount,
        goal_amount=goal_amount,
        years=years,
        return_rate=annual_return * 100 if annual_return else None,
        form_data=form_data,
        to_readable_amount=to_readable_amount
    )

# --------------------------
# ✅ NEW: Retirement SIP Planner
# --------------------------
@app.route("/retirement-sip", methods=["GET", "POST"])
def retirement_sip():
    corpus = None
    required_sip = None
    formatted_corpus = None
    formatted_sip = None
    form_data = {}

    if request.method == "POST":
        form_data = {
            "monthly_expense": request.form["monthly_expense"],
            "current_age": request.form["current_age"],
            "retirement_age": request.form["retirement_age"],
            "life_expectancy": request.form["life_expectancy"],
            "inflation_rate": request.form["inflation_rate"],
            "expected_return_rate": request.form["expected_return_rate"],
            "step_up_rate": request.form["step_up_rate"]
        }

        monthly_expense = float(form_data["monthly_expense"])
        current_age = int(form_data["current_age"])
        retirement_age = int(form_data["retirement_age"])
        inflation_rate = float(form_data["inflation_rate"]) / 100
        expected_return_rate = float(form_data["expected_return_rate"]) / 100
        step_up_rate = float(form_data["step_up_rate"]) / 100

        years_to_retirement = retirement_age - current_age
        inflated_expense = monthly_expense * ((1 + inflation_rate) ** years_to_retirement)
        annual_expense = inflated_expense * 12
        safe_withdrawal_rate = 0.04
        corpus = annual_expense / safe_withdrawal_rate

        months = years_to_retirement * 12
        monthly_return = (1 + expected_return_rate) ** (1 / 12) - 1

        sip = corpus / months
        for _ in range(1000):
            fv = 0
            sip_guess = sip
            for year in range(years_to_retirement):
                for month in range(12):
                    fv = (fv + sip_guess) * (1 + monthly_return)
                sip_guess *= (1 + step_up_rate)
            if abs(fv - corpus) < 100:
                break
            sip *= corpus / fv

        required_sip = sip
        formatted_corpus = format_amount(corpus)
        formatted_sip = format_amount(required_sip)

    return render_template(
        "retirement_sip.html",
        corpus=corpus,
        formatted_corpus=formatted_corpus,
        required_sip=required_sip,
        formatted_sip=formatted_sip,
        form_data=form_data,
        to_readable_amount=to_readable_amount
    )

if __name__ == "__main__":
    app.run(debug=True)
