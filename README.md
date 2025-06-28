# 🧮 EasyFinCalc – Smart Financial Calculators

## 📌 Project Overview
**EasyFinCalc** is a lightweight, web-based financial tool designed to simplify essential investment planning. It provides:

- 📈 **SIP Calculator** – Visualize long-term investment growth with step-up SIP support.  
- 👴 **Retirement Calculator** – Calculate how much you need to retire, adjusting for inflation and expenses.

---

## 🧰 Tech Stack & Tools

| Tool/Service            | Purpose                                |
|------------------------|----------------------------------------|
| Flask (Python)         | Backend framework                      |
| HTML, CSS, Bootstrap   | Frontend and responsive UI             |
| JavaScript             | Interactive elements & dark mode       |
| Git & GitHub           | Version control                        |
| Render                 | Deployment platform (free tier used)   |
| PowerShell             | Local terminal for development         |
| VS Code                | Code editor                            |
| Notion                 | Documentation                          |
| Custom Domain          | Connected via Render + DNS             |

---

## 🗂️ Folder Structure

```
retirement_calculator/
├── static/
│   ├── style.css              # Global styles
│   └── script.js              # Theme toggle & calculator logic
├── templates/
│   ├── index.html             # Homepage with calculator cards + articles
│   ├── investment.html        # SIP calculator UI
│   └── retirement.html        # Retirement calculator UI
├── app.py                     # Flask routes + business logic
├── requirements.txt           # Project dependencies
├── .gitignore                 # Ignore venv, __pycache__, etc.
└── README.md                  # GitHub documentation
```

---

## 🚀 Setup & Deployment

### ✅ 1. Setup Virtual Environment

```bash
python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass  # (Windows)
.\venv\Scripts\Activate
```

### ✅ 2. Install Flask & Dependencies

```bash
pip install flask
pip freeze > requirements.txt
```

### ✅ 3. Flask App Structure

- `/` → Homepage  
- `/investment` → SIP Calculator  
- `/retirement` → Retirement Calculator  
- Each route handles POST requests and passes calculated results to templates.

### ✅ 4. Git & GitHub Workflow

```bash
git init
git remote add origin https://github.com/akhilponna98/easyfincal.git
git checkout -b dev
git add .
git commit -m "Initial project setup with Flask & calculators"
git push -u origin dev
```

**📌 Tip**: Always work on a branch like `dev` and merge via Pull Requests to `main` to avoid merge conflicts.

### ✅ 5. Deployment via Render

- Go to [https://render.com](https://render.com)
- Create **New Web Service**
  - Runtime: **Python**
  - Build Command: `pip install -r requirements.txt`
  - Start Command: `python app.py`
- Connect GitHub repo  
- App auto-deploys on push.

### ✅ 6. Custom Domain Setup

- Bought domain: **easyfincal.com**
- Linked it in Render → **Custom Domains**
- Updated DNS (A and CNAME records) on provider like GoDaddy/Namecheap
- Result: ✅ Live at `https://easyfincal.com`

---

## 💡 Calculator Logic

### 📊 SIP Calculator:
- Monthly SIP with annual **step-up percentage**
- Uses **compound interest** compounded monthly
- Calculates:
  - Total Invested
  - Estimated Returns
  - Final Corpus

### 👵 Retirement Calculator:
- Inflation-adjusted monthly expenses
- Calculates future retirement corpus required
- Uses current age, retirement age, expected life expectancy, inflation, and return rates

---

## 🎨 Features Implemented

- ✅ Responsive UI with **Bootstrap 5**
- ✅ Dark mode toggle (remembers preference via `localStorage`)
- ✅ Clear financial summaries and logic breakdown
- ✅ Theme toggle icon switches (🌙/☀️)
- ✅ Developer credit on homepage
- ✅ SEO-friendly meta tags and clean layout

---

## 📌 Git Best Practices

1. Always create and work on a **feature branch**:
   ```bash
   git checkout -b feature/ui-update
   ```
2. After changes:
   ```bash
   git add .
   git commit -m "Updated homepage layout with responsive grid"
   git push origin feature/ui-update
   ```
3. Go to GitHub and create a **Pull Request → `main`**
4. Once merged, Render auto-deploys latest version.

---

## 📝 Future Improvements

- 📄 Generate downloadable PDF report for results
- 📊 Visual charts using Chart.js / Plotly
- 🧮 Add calculators: EMI, FD, RD, NPS, Tax planning
- 🔐 User authentication and dashboard (Flask-Login)
- 🌐 PWA (Progressive Web App) with offline support

---

## 📚 Commands Cheat Sheet

```bash
# Virtual Env
python -m venv venv
.env\Scriptsctivate

# Flask Dev Run
python app.py

# Git Workflow
git checkout -b dev
git add .
git commit -m "Commit message"
git push origin dev
```

---

## 🔗 Live App & Repo

- 🌐 Website: [https://easyfincal.com](https://easyfincal.com)
- 🧑‍💻 GitHub Repo: [github.com/akhilponna98/easyfincal](https://github.com/akhilponna98/easyfincal)
