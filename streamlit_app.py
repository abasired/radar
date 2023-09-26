# import streamlit

import streamlit as st
import pandas as pd
import numpy as np
import random

st.title('Drive through analytics')



# Page 1
def Customer_count():
    st.title("number of customers")
    # Create a bar chart on this page
    chart_data = pd.DataFrame(np.random.randint(low = 0, high = 100, size =(12, 1), dtype =int), columns=["# Customers"])
    st.bar_chart(chart_data)

# Page 2
def Ordertime_statistics():
    st.title("Order time")
    # Create a different bar chart on this page
    chart_data = pd.DataFrame(np.random.randint(low = 0, high = 100, size =(12, 1), dtype =int), columns=["Order time"])
    st.bar_chart(chart_data)

# Page 3
def pickup_time_statistics():
    st.title("Waiting time")
    # Create another bar chart on this page
    chart_data = pd.DataFrame(np.random.randint(low = 0, high = 100, size =(12, 1), dtype =int), columns=["Waiting time"])
    st.bar_chart(chart_data)

# Create navigation menu
pages = {
    "Customer count": Customer_count,
    "Ordertime statistics": Ordertime_statistics,
    "pickup time statistics": pickup_time_statistics
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Display the selected page
page = pages[selection]
page()
