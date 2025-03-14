import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

# Streamlit App Configuration
st.set_page_config(page_title="Telesales Performance Dashboard", layout="wide")
st.title("\U0001F4DE Telesales Performance Prediction")

# Instructions Section
if "dataset_uploaded" not in st.session_state:
    st.session_state.dataset_uploaded = False

if not st.session_state.dataset_uploaded:
    st.info("""
    ### How to Use This Tool:
    1. **Upload a CSV Dataset** with the following columns:
       - `Year`: Year of the record.
       - `Month`: Month of the record.
       - `Total Incoming Calls`: Number of total incoming calls.
       - `Calls Answered`: Number of answered calls.
       - `Calls Answered Rate`: Percentage of calls answered.
       - `Total Wait Time (min)`: Total waiting time in minutes.
       - `Avg Time to Answer (s)`: Average response time in seconds.
    2. **Once uploaded, the dashboard will display key insights and predictions.**
    3. **Use the sidebar** to filter results by year.
    4. **If necessary alter the dataset column by this in below github link for better peocessing** 
    5. **GIT Repository**: [Telesales Performance Prediction](https://github.com/ranjithsurineni/Telesales-Performance-Prediction.git)
    6. **Author**: [Ranjith Kumar](https://www.linkedin.com/in/ranjith-kumar-surineni-b73b981b6/)
    
    """)

# File Uploader
uploaded_file = st.file_uploader("Upload your dataset (CSV format)", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.session_state.dataset_uploaded = True  # Hide instructions after upload
    
    # Load Models
    weekly_model = joblib.load('./model/telesales_model_Week.pkl')
    monthly_model = joblib.load('./model/telesales_model_Month.pkl')
    yearly_model = joblib.load('./model/telesales_model_Year.pkl')

    # Sidebar filters
    st.sidebar.header("Filter Options")
    selected_year = st.sidebar.selectbox("Select Year", data['Year'].unique())
    filtered_data = data[data['Year'] == selected_year]

    #--------------------------------- KPI Section ---------------------------------#


    # KPI Metrics
    st.subheader(f"Performance Metrics for Year {selected_year}")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Calls", filtered_data['Total Incoming Calls'].sum())
    col2.metric("Answered Calls", filtered_data['Calls Answered'].sum())
    col3.metric("Answer Rate", f"{round(filtered_data['Calls Answered Rate'].mean() * 100, 2)}%")

    #---------------------------------Trend Chart Section ---------------------------------#


    # Trend Chart
    st.subheader("\U0001F4C8 Call Answering Trend")
    fig = px.line(filtered_data, x='Month', y=['Total Incoming Calls', 'Calls Answered'],
                  title='Total Calls vs Answered Calls')
    st.plotly_chart(fig)


    #--------------------------------- Pie Section ---------------------------------#

    # Insightful Percentage Breakdown
    unanswered_calls = filtered_data['Total Incoming Calls'].sum() - filtered_data['Calls Answered'].sum()
    answered_percentage = round((filtered_data['Calls Answered'].sum() / filtered_data['Total Incoming Calls'].sum()) * 100, 2)
    unanswered_percentage = round((unanswered_calls / filtered_data['Total Incoming Calls'].sum()) * 100, 2)

    st.subheader("📊 Answered vs Unanswered Calls")
    fig_pie = px.pie(names=["Answered Calls", "Unanswered Calls"],
                    values=[answered_percentage, unanswered_percentage],
                    color_discrete_sequence=['#2ECC71', '#E74C3C'])
    st.plotly_chart(fig_pie)




    #--------------------------------- Prediction Section ---------------------------------#
    st.markdown("---")

    # Prediction Section
    st.subheader("\U0001F4CA Predict Future Performance")
    pred_option = st.selectbox("Select Prediction", ['Weekly', 'Monthly', 'Yearly'])
    input_features = filtered_data[['Total Incoming Calls', 'Total Wait Time (min)', 'Avg Time to Answer (s)']].values[-1:].reshape(1, -1)

    if pred_option == 'Weekly':
        prediction = weekly_model.predict(input_features)
        st.write(f"### 📅 Predicted Answered Calls for Next Week: {int(prediction[0])}")
    elif pred_option == 'Monthly':
        prediction = monthly_model.predict(input_features)
        st.write(f"### 🗓️ Predicted Answered Calls for Next Month: {int(prediction[0])}")
    else:
        prediction = yearly_model.predict(input_features)
        st.write(f"### 📅 Predicted Answered Calls for Next Year: {int(prediction[0])}")


#--------------------------------- Performance Analysis Section ---------------------------------#

    # Performance Analysis
    st.subheader("📊 Performance Analysis")
    fig2 = px.bar(filtered_data, x='Month', y='Calls Answered Rate', color='Calls Answered Rate',
                  title='Monthly Answer Rate')
    st.plotly_chart(fig2)

    # Insight Analysis
    st.subheader("📜 Insights")
    avg_time = filtered_data['Avg Time to Answer (s)'].mean()
    if avg_time > 60:
        st.warning("⚠️ Average response time is high. Consider improving team efficiency.")
    else:
        st.success("✅ Average response time is within a good range.")

    if filtered_data['Calls Answered Rate'].mean() < 50:
        st.warning("⚠️ Answer rate is significantly low. Potential customer dissatisfaction.")
    else:
        st.success("✅ Answer rate is stable.")

# Footer
st.markdown("---")
st.markdown("📊 Developed by Ranjith Kumar")
