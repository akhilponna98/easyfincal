
# 📊 EasyFinCal — Smart Financial Calculators

**EasyFinCal** is a free, simple, user-friendly web app with practical calculators for smart financial planning.

> 💡 Plan your SIPs, retirement, and financial goals with clear calculators, charts, and a clean UI.

---

## 🚀 Features

✅ SIP Investment Calculator  
✅ Retirement Corpus & SIP Planner  
✅ Target Corpus SIP Calculator  
✅ Clean, responsive UI with dark mode  
✅ Sliders + number inputs for easy control  
✅ Donut charts for visual breakdowns  
✅ Financial tips & articles on the homepage

---

## 📁 Project Structure

```plaintext
EasyFinCal/
├── app.py                  # Flask backend with all calculator routes & logic
├── templates/
│   ├── index.html          # Homepage with calculators & articles
│   ├── investment.html     # SIP Investment Calculator page
│   ├── retirement.html     # Retirement Corpus & SIP Planner page
│   ├── target_sip.html     # Target Corpus SIP Calculator page
├── static/
│   ├── style.css           # Custom CSS: layout, dark mode, form styling
│   ├── script.js           # Shared JS: sliders, donut charts (Chart.js)
├── requirements.txt        # Python dependencies for deployment
├── Procfile                # For deployment on Render or Heroku
└── README.md               # Project documentation (this file)
```

---

## ⚙️ How it Works

- **Backend:** Flask handles form submissions, runs finance math, and returns results to HTML templates.
- **Frontend:** Bootstrap for responsive layout, Chart.js for donut charts, custom JS for syncing sliders & inputs.
- **Deployment:** Works perfectly on Render, Heroku, or any Flask-friendly host.

---

## 🧩 Calculator Logic

- **Investment Calculator:** Compounds SIP monthly, supports annual step-up.
- **Retirement Calculator:** Estimates future expenses with inflation, calculates required corpus, then computes SIP needed.
- **Target SIP Calculator:** Computes monthly SIP needed to reach a target corpus in a fixed timeframe.

---

## ✅ Getting Started

1️⃣ **Clone the project**
```bash
git clone https://github.com/YOUR_USERNAME/EasyFinCal.git
cd EasyFinCal
```

2️⃣ **Create & activate virtual environment**
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

3️⃣ **Install dependencies**
```bash
pip install -r requirements.txt
```

4️⃣ **Run locally**
```bash
python app.py
```
Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 🌐 Deployment

EasyFinCal runs smoothly on **Render**, **Heroku**, or any Python server.

**✔️ `requirements.txt`**

```txt
Flask==2.3.2
gunicorn==21.2.0
```

**✔️ `Procfile`**

```txt
web: gunicorn app:app
```

---

## 📸 Screenshots

| Homepage | SIP Calculator | Retirement Planner |
|----------|----------------|---------------------|
| *(Add screenshots here, e.g., `/screenshots/home.png`)* |

---

## ✨ Roadmap

✅ Add EMI & other calculators  
✅ Add export as PDF  
✅ Add user scenario saving (DB)  
✅ Make it PWA for offline use  
✅ Improve SEO for organic reach

---

## 🙌 Made with ❤️ by Akhil Ponna

> *Smart investing is simple — plan well and start early!*

---

🌐 Live Website
🔗 EasyFinCal → https://www.easyfincal.com
Your all-in-one platform for free, simple financial calculators to plan SIPs, retirement, and wealth goals.

## 📜 License

MIT License — Free to use, improve, and share!

---

## 🔗 Connect

If you like this project — ⭐ star it, fork it, and share it!  
Questions? Feedback? Let’s connect!
