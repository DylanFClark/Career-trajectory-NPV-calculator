import pandas as pd
import streamlit as st


dataset = pd.read_csv("../data/compiled_482_data.csv")


#cash flows
cashflowColumns = "year,province,career_path_name,earnedIncome,fed_tax_amt,prov_tax_amt,tax_amt,current_endevor,afterTaxIncome,afterTaxAndCostsIncome,amtSavedThisYear,expenditureBias,Housing,Food,Transportation,educationCost,totalLivingCosts,contributions,investment_low,investment_avg,investment_high,investment_developTradingBot"
cashflowColumns = cashflowColumns.split(",")
cashflowsData = dataset[cashflowColumns]


# FILTERS

   # province
province = st.sidebar.selectbox("Province", cashflowsData["province"].unique())
cashflowsData = cashflowsData[cashflowsData["province"] == province]

   # career path
career_path_name= st.sidebar.selectbox("career_path", cashflowsData["career_path_name"].unique())
cashflowsData = cashflowsData[cashflowsData["career_path_name"] == career_path_name]

   # Year range
year_range = st.sidebar.slider("Year Range", min_value=2026, max_value=2076, value=(2026, 2076))
cashflowsData = cashflowsData[cashflowsData["year"] >= year_range[0]]  # Set lower bound
cashflowsData = cashflowsData[cashflowsData["year"] <= year_range[1]]  # Set upper bound


# VISUALIZATION
   #DATAFRAME
st.title("Career trajectory - CASH FLOWS")
st.dataframe(cashflowsData)

   #VISUALS
# Income Over Time
st.markdown(
"""
## Income Over Time (Per Year Basis)
"""
)

lineChartDataColumns = "year,earnedIncome,fed_tax_amt,prov_tax_amt,tax_amt,afterTaxIncome,afterTaxAndCostsIncome,amtSavedThisYear,expenditureBias,Housing,Food,Transportation,educationCost,totalLivingCosts,contributions,investment_low,investment_avg,investment_high,investment_developTradingBot"
lineChartDataColumns = lineChartDataColumns.split(",")
lineChartData = cashflowsData[lineChartDataColumns]

possible_selections = ["earnedIncome","afterTaxIncome","afterTaxAndCostsIncome"]

with st.expander("Filter for income metrics", expanded=False):
    income_selections = st.multiselect(
        label="Filter for income metrics",
        options=possible_selections,
        default=possible_selections,
        key=possible_selections
    )

st.line_chart(
    lineChartData, 
    x="year", 
    y=income_selections,
    x_label="Year",
    y_label="Amount ($)"
)


   # Investments over time


# Costs Over Time
st.markdown(
"""
## Costs Over Time (Per Year Basis)
"""
)

possible_selections = ["expenditureBias","Housing","Food","Transportation","totalLivingCosts","educationCost","tax_amt", "prov_tax_amt", "fed_tax_amt"]

with st.expander("Filter for income metrics", expanded=False):
    income_selections = st.multiselect(
        label="Filter for income metrics",
        options=possible_selections,
        default=possible_selections,
        key=possible_selections
    )

st.line_chart(
    lineChartData, 
    x="year", 
    y=income_selections,
    x_label="Year",
    y_label="Amount ($)"
)


# Assets Over Time
st.markdown(
"""
## Assets Over Time (Aggregate Basis)
"""
)

possible_selections = ["contributions","investment_low","investment_avg","investment_high","investment_developTradingBot"]

with st.expander("Filter for income metrics", expanded=False):
    income_selections = st.multiselect(
        label="Filter for income metrics",
        options=possible_selections,
        default=possible_selections,
        key=possible_selections
    )

st.line_chart(
    lineChartData, 
    x="year", 
    y=income_selections,
    x_label="Year",
    y_label="Amount ($)"
)


# Cash Flow Statement for period
st.markdown(
"""
## Cash Flow Statement
"""
)

# Aggregate values for insertion
earnedIncome = sum(lineChartData["earnedIncome"].to_list())
tax_amt = sum(lineChartData["tax_amt"].to_list())
afterTaxIncome = sum(lineChartData["afterTaxIncome"].to_list())
afterTaxAndCostsIncome = sum(lineChartData["afterTaxAndCostsIncome"].to_list())
amtSavedThisYear = sum(lineChartData["amtSavedThisYear"].to_list())
Housing = sum(lineChartData["Housing"].to_list())
Transportation = sum(lineChartData["Transportation"].to_list())
Food = sum(lineChartData["Food"].to_list())
expenditureBias = sum(lineChartData["expenditureBias"].to_list())
totalLivingCosts = sum(lineChartData["totalLivingCosts"].to_list())
contributions = sum(lineChartData["contributions"].to_list())
fed_tax_amt = sum(lineChartData["fed_tax_amt"].to_list())
prov_tax_amt = sum(lineChartData["prov_tax_amt"].to_list())
educationCost = sum(lineChartData["educationCost"].to_list())




st.markdown(f"## For period starting: {year_range[0]} & ending: {year_range[1]}")

items = ["Gross Income", "Federal Tax","Provincial Tax","Total Tax", "Income (after tax)", "Housing Cost", "Transportation Cost", "Food Cost", "expenditureBias", "educationCost","Total Living Costs", "Net Income", "Amt Saved In This Period"]
revenues = [earnedIncome, 0,            0,            0,             afterTaxIncome,       0,               0,                    0,             0,                 0,             0,                   afterTaxAndCostsIncome,   amtSavedThisYear]
costs = [0,              fed_tax_amt,  prov_tax_amt,    tax_amt,      0,                    Housing,        Transportation,        Food,        expenditureBias,  educationCost,   totalLivingCosts,    0,                         0              ]


cashFlow = pd.DataFrame({
    "Item":items,
    "Revenues":revenues,
    "Costs":costs
})
st.table(cashFlow)

