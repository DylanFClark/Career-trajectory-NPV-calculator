import pandas as pd
import streamlit as st


st.markdown(
"""
# Decision Support 

This framework is intended to support career decisions, via forecasting future financial data (cash flows & investment position) as well as skill growth over time for alternative career routes


## Cash Flows

This page is used to forecast incomes, costs, and investment positions over time.
The  parameters on the left are adjustable (province, career_path, and a range of years)


## Skills Ledger

This page is used to forecast skill growth over time. 
The  parameters on the left are adjustable (province, career_path, and a range of years)

Note: Since career paths don't vary by province, all provinces will have the same skill growth over time 

"""
)

