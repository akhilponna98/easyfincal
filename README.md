🧮 EasyFinCal – Smart Financial Calculators
EasyFinCal is a modern, web-based suite of financial calculators designed to help users plan investments and retirement with ease. Built with Flask, Bootstrap, and Chart.js, it’s mobile-friendly, fast, and visually engaging.
🚀 Live Demo
•	Website: https://easyfincal.com
✨ Features
•	SIP Calculator:
Calculate the future value of monthly investments (SIP) with annual step-up support and visual breakdown.
•	Retirement Calculator:
Estimate the retirement corpus you’ll need, factoring in inflation, life expectancy, and expected returns (uses the 4% rule).
•	Retirement SIP Planner:
Find out how much you need to invest monthly (with step-up) to reach your retirement goal.
•	Target SIP Calculator:
Calculate the required SIP to reach a specific financial goal in a set time frame.
•	Dark/Light Mode:
Toggleable theme with user preference saved.
•	Responsive Design:
Works beautifully on desktop and mobile.
•	Visual Charts:
Donut charts for investment breakdowns (powered by Chart.js).
•	SEO & Accessibility:
Optimized for search engines and accessible for all users.
🗂️ Folder Structure
EasyFinCal/
├── app.py                  # Flask backend: routes, calculator logic
├── templates/
│   ├── index.html          # Homepage with calculator cards + articles
│   ├── investment.html     # Monthly SIP Investment Calculator
│   ├── retirement.html     # Retirement Corpus + SIP Planner
│   ├── target_sip.html     # Target Corpus SIP Planner
│   └── retirement_sip.html # Retirement SIP Planner
├── static/
│   ├── style.css           # Global styles: layout, dark mode, cards, forms
│   ├── script.js           # Shared JS: charts, sliders, theme, interactivity
│   └── logo.png            # (If applicable) Site logo
└── requirements.txt        # Python dependencies (Flask, etc.)

File/Folder Descriptions
File/Folder	Purpose
app.py	Main Flask application. Handles all routes, form submissions, and calculator logic.
templates/	Jinja2 HTML templates rendered by Flask.
index.html	Homepage: lists all calculators with icons, descriptions, and financial tips/articles.
investment.html	SIP Investment Calculator: calculates future corpus for monthly SIP with step-up option.
retirement.html	Retirement Corpus Calculator & SIP Planner: estimates required corpus and monthly SIP.
target_sip.html	Target SIP Calculator: figures out the SIP needed to reach a specific goal in given time.
retirement_sip.html	Retirement SIP Planner: combines corpus and SIP planning for retirement.
static/	Static assets (CSS, JS, images, etc).
style.css	Global custom styles: layout, dark mode, cards, forms, responsiveness.
script.js	JavaScript for charts (Chart.js), slider syncing, theme toggle, and interactivity.
requirements.txt	Python dependencies (Flask, gunicorn, etc.) for running the app locally or on deployment.

🛠️ Getting Started
1. Clone the Repository
git clone https://github.com/yourusername/easyfincal.git
cd easyfincal

2. Set Up a Virtual Environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Run the App Locally
python app.py

Visit http://localhost:5000 in your browser.
🌐 Deployment
•	Free Hosting: Render.com (recommended)
•	Steps:
o	Connect your GitHub repo
o	Set build command: pip install -r requirements.txt
o	Set start command: python app.py
o	Add custom domain if needed
🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.
•	Use feature branches (feature/your-feature-name)
•	Follow PEP8 for Python and standard HTML/CSS/JS best practices
•	Keep code and documentation clean and readable
📄 License
This project is licensed under the MIT License.
🙏 Credits
•	Bootstrap
•	Chart.js
•	Flask
•	Built and maintained by Akhil Ponna
📬 Contact
•	Email: your.email@example.com
•	LinkedIn (add your link)
•	GitHub
Happy Planning! 🚀
“Growing wealth is a long-term game. With patience, discipline, and consistent effort, anyone can build it.”
— Akhil Ponna
You can personalize the contact info, add more calculators, or update deployment instructions as your project grows!
