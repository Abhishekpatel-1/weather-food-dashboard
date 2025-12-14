🌦️ Weather vs Food Orders
The Data Weaver
📌 Project Overview
The Data Weaver.
The goal is to combine two unrelated datasets—weather data and online food order data—and visualize them together to uncover meaningful insights.

The dashboard demonstrates how external factors like temperature and rainfall can influence online food ordering behavior.

🎯 Problem Statement

Online food delivery platforms experience varying order volumes.
This project explores the question:

Does weather have an impact on online food ordering trends?

📊 Datasets Used

Two unrelated datasets are used and merged using a common date field:

Weather Dataset

Temperature

Rainfall

Date

Food Orders Dataset

Daily food order count

Date

🛠️ Tech Stack

Python

Pandas – Data processing

Streamlit – Dashboard creation

Kiro – AI-assisted development

GitHub – Version control

🤖 How Kiro Was Used

Kiro was used throughout the project to:

Generate and refine Pandas code for loading and merging datasets

Suggest appropriate visualizations for comparing datasets

Improve Streamlit dashboard layout and readability

Assist in deriving clear insights from combined data

This significantly reduced development time and improved overall code quality.

📈 Dashboard Features

Line chart: Temperature vs Food Orders

Bar chart: Rainfall vs Food Orders

Clear insight section summarizing observed patterns

🧠 Key Insights

Food orders tend to increase on rainy days

Lower temperatures often correlate with higher food delivery demand

Weather conditions can influence consumer behavior

🚀 How to Run the Project Locally
1️⃣ Clone the Repository
git clone https://github.com/Abhishekpatel-1/weather-food-dashboard.git
cd weather-food-dashboard

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Dashboard

python -m streamlit run app.py

The dashboard will open in your browser at:

http://localhost:8501

📁 Project Structure
weather-food-dashboard/
├── .kiro/
│   └── prompts.md
├── data/
│   ├── weather.csv
│   └── food_orders.csv
├── screenshots/
│   ├── dashboard.png
│   └── kiro_usage.png
├── app.py
├── requirements.txt
└── README.md
🔗 Resources

GitHub Repository:
https://github.com/Abhishekpatel-1/weather-food-dashboard

AWS Builder Center Blog:
https://builder.aws.com/content/36ocZgFAr86VWxVRlvOiuPP2uCD/the-data-weaver-connecting-weather-and-food-ordering-trends

🏁 Conclusion

This project highlights the power of AI-assisted development using Kiro to weave together unrelated datasets and generate meaningful insights through data visualization.

