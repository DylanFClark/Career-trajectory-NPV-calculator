import pandas as pd
import streamlit as st


dataset = pd.read_csv("../data/compiled_482_data.csv")

# skills
skillsColumns = "year,province,career_path_name,current_endevor,yrs_Programming & Software Development,yrs_Version Control (Git),yrs_System Design & Architecture,yrs_Agile & DevOps Practices,yrs_Network Security,yrs_Security Monitoring & SIEM,yrs_Incident Response,yrs_Threat Analysis & Intelligence,yrs_Vulnerability Assessment,yrs_IT Consulting & Client Engagement,yrs_Business Process Analysis,yrs_Project Management,yrs_Enterprise Systems & ERP,yrs_PLC & Control System Programming,yrs_Instrumentation Calibration & Maintenance,yrs_Process Control & SCADA,yrs_Electrical Systems & Wiring,yrs_Industrial Cybersecurity,yrs_OT/IT Network Integration,yrs_Risk Assessment & Compliance (OT)"
skillsColumns = skillsColumns.split(",")
skillsData = dataset[skillsColumns]


# datetime / ints
# st.slider()

# discrete variables
# st.select_slider()


#label = "Year"
#min_value = "2026-01-01"
#max_value = "2076-12-01"
#st.select_slider(label, min_value=min_value, max_value=max_value)


# FILTERS
   #Province
province = st.sidebar.selectbox("Province", skillsData["province"].unique())
skillsData = skillsData[skillsData["province"] == province]

   # Career path
career_path_name= st.sidebar.selectbox("career_path", skillsData["career_path_name"].unique())
skillsData = skillsData[skillsData["career_path_name"] == career_path_name]

   # Year range
year_range = st.sidebar.slider("Year Range", min_value=2026, max_value=2076, value=(2026, 2076))
skillsData = skillsData[skillsData["year"] >= year_range[0]]  # Set lower bound
skillsData = skillsData[skillsData["year"] <= year_range[1]]  # Set upper bound


# VISUALIZATION
   #DATAFRAME
st.title("Career Trajectory - SKILL LEDGER")
st.dataframe(skillsData)

   #VISUALS
    # Skill growth within <period>
lineChartDataColumns = "year,yrs_Programming & Software Development,yrs_Version Control (Git),yrs_System Design & Architecture,yrs_Agile & DevOps Practices,yrs_Network Security,yrs_Security Monitoring & SIEM,yrs_Incident Response,yrs_Threat Analysis & Intelligence,yrs_Vulnerability Assessment,yrs_IT Consulting & Client Engagement,yrs_Business Process Analysis,yrs_Project Management,yrs_Enterprise Systems & ERP,yrs_PLC & Control System Programming,yrs_Instrumentation Calibration & Maintenance,yrs_Process Control & SCADA,yrs_Electrical Systems & Wiring,yrs_Industrial Cybersecurity,yrs_OT/IT Network Integration,yrs_Risk Assessment & Compliance (OT)"
lineChartDataColumns = lineChartDataColumns.split(",")
lineChartData = skillsData[lineChartDataColumns]

st.markdown(
"""
## Line Chart: Years experience with skills
"""
)

st.line_chart(lineChartData, 
              x="year", 
              y=lineChartDataColumns[5:],
              x_label="Year",
              y_label="years of experience"
              )

st.markdown(
"""
## Bar Chart: Years experience with skills
"""
)

st.bar_chart(lineChartData, 
              x="year", 
              y=lineChartDataColumns[5:],
              x_label="Year",
              y_label="years of experience"
              )



