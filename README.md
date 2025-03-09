📞 **Telesales Performance Prediction Dashboard**

This project is a professional and detailed **Telesales Performance Prediction Dashboard** built using **Streamlit**, **Plotly**, and **Machine Learning Models (Joblib)**. It provides **insightful visualizations, predictions, and analysis** for telesales performance based on incoming and answered calls data.

## 📊 Folder Structure

```
Telesales-Performance-Prediction
│
├── datasets
│   ├── MTA_NYCT_Customer_Engagement_Statistics__2017-2022.csv
│
├── models
│   ├── telesales_model_Week.pkl
│   ├── telesales_model_Month.pkl
│   ├── telesales_model_Year.pkl
│
├── notebooks
│   ├── Data_Analysis.ipynb
│   ├── Model_Training.ipynb
│
├── app.py
│
├── requirements.txt
│
├── README.md
```

---

## 🚀 Features

### ✅ **Performance Metrics (KPI)**
- Provides total incoming calls, answered calls, and answer rate percentage.
- Allows filtering by year to compare metrics for different periods.

### ✅ **Trend Chart (Line Chart)**
- Displays a detailed line chart comparing total incoming calls vs answered calls.
- Provides year-wise comparison with smooth visualization.

### ✅ **Answered vs Unanswered Calls (Pie Chart)**
- Generates a percentage-based pie chart to show answered vs unanswered calls.
- This helps to visually analyze the gap in call handling.

### ✅ **Future Performance Prediction**
- Predicts answered calls based on:
  - **Weekly Prediction**
  - **Monthly Prediction**
  - **Yearly Prediction**
- Provides insight on future performance trends.

### ✅ **Performance Analysis (Bar Chart)**
- Visualizes monthly call answered rates with color-coded bar charts.
- Highlights high and low-performing months.

### ✅ **Insight Alerts (Dynamic Alerts)**
- If the average response time exceeds the threshold, an alert is triggered.
- Shows alerts if the call answer rate is low, highlighting potential dissatisfaction.

---

## 💻 How to Run the Project

1. **Clone the Repository:**
```bash
git clone https://github.com/ranjithsurineni/Telesales-Performance-Prediction.git
cd Telesales-Performance-Prediction
```

2. **Create a Virtual Environment:**
```bash
python -m venv venv
source venv/bin/activate # For MacOS/Linux
venv\Scripts\activate # For Windows
```

3. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the Streamlit App:**
```bash
streamlit run app.py
```

5. **Access the Dashboard:**
- Open your browser and navigate to:  
  **http://localhost:8501**

---

## 📊 Dataset Description
The dataset contains:
- **Total Incoming Calls**: Total number of incoming calls.
- **Calls Answered**: Number of calls answered by the team.
- **Total Wait Time (min)**: Total waiting time for the calls.
- **Avg Time to Answer (s)**: Average time taken to answer calls.
- **Year** and **Month**: Timeline of call data.

---

## 🤖 Machine Learning Models
The following machine learning models have been trained and used:

| Model Name | Type            | Prediction Period |
|------------|-----------------|-------------------|
| **telesales_model_Week.pkl**   | Random Forest Regressor | Weekly Prediction    |
| **telesales_model_Month.pkl**  | Random Forest Regressor | Monthly Prediction   |
| **telesales_model_Year.pkl**   | Random Forest Regressor | Yearly Prediction    |

The models have been trained using the `RandomForestRegressor` with optimized hyperparameters to achieve high prediction accuracy.

---

## 📜 Requirements
All dependencies are listed in the `requirements.txt` file. Install them using:
```bash
pip install -r requirements.txt
```

Main Libraries Used:
- **Streamlit** - Web application framework
- **Pandas** - Data analysis and manipulation
- **Plotly** - Interactive visualizations
- **Joblib** - Loading and saving trained models

---

## 📊 Dashboard Screenshots
### 📊 KPI Metrics
- Displays incoming calls, answered calls, and call answer rate.
- Year-wise performance filtering.

### 📈 Call Answering Trend
- Shows the trend of answered vs unanswered calls month-wise.

### 📊 Future Performance Prediction
- Predicts future performance based on weekly, monthly, or yearly data.

### 📊 Answered vs Unanswered Calls
- Pie chart representation of call answering percentage.

### 📜 Performance Insights
- Automatic insights based on call response time and answer rates.

---

## 💡 Future Enhancements
✅ Add a login system to secure data.  
✅ Implement a database (PostgreSQL/MongoDB) for dynamic data storage.  
✅ Real-time data fetching and model training.  
✅ Deploy on cloud platforms (AWS, Heroku, HuggingFace).

---

## 📝 Author
👨‍💻 **Ranjith Kumar**  
- GitHub: [@RanjithKumar](https://github.com/ranjithsurineni)  
- LinkedIn: [@RanjithKumar](https://www.linkedin.com/in/ranjith-kumar-surineni-b73b981b6/)

---

## 📊 License
This project is licensed under the **MIT License**.

✅ **Star ⭐ this repository if you find it helpful!**
