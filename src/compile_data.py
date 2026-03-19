import pandas as pd

#DATA IMPORTS
# -----------------------------------------------------------------------------------------------------------------
#costs
tax_brackets = pd.read_csv("../data/tax_brackets.csv")  #,Province,tax_bracket,tax_rate

education = pd.read_csv("../data/education.csv") #educationID,educationName,years,expectedCost,expectedEarnings

cpi = pd.read_csv("../data/cpi.csv") #costOfLivingID,costArea,baselineCost,expectedYearlyIncrease,province

# wealth growth --> Mostly calculated fields
investment_mechanism = pd.read_csv("../data/investment_mechanism.csv") #,invesmentMechanismID,investmentMechanismName,avgYearlyReturn


#skills 
skillsLedger = pd.read_csv("../data/skillsLedger.csv") #skillID,skillName

educationSkills = pd.read_csv("../data/educationSkills.csv")  #educationSkillID,educationID,skillID

jobSkills = pd.read_csv("../data/job_skills.csv") # jobSkillID,jobID,skillID

skillsExperrience = pd.read_csv("../data/skillsExperience.csv")


#metadata
jobs = pd.read_csv("../data/jobs.csv")     #jobID,jobName

jobData = pd.read_csv("../data/jobData.csv") #jobDataID,jobID,jobName,province,avgWage,avgYearlyWageIncrease,avgHoursWorkedWeekly

educationData = pd.read_csv("../data/educationData.csv") #educationDataID,educationID,province,expectedCost,expectedEarnings,years

#comparison
careerPaths = pd.read_csv("../data/careerPaths.csv") #careerPathID,pathName

employmentHistory = pd.read_csv("../data/employmentHistory.csv") # empID,careerPathID,jobDataID,startDate,endDate
employmentHistory['startDate'] = pd.to_datetime(employmentHistory['startDate'])
employmentHistory['endDate'] = pd.to_datetime(employmentHistory['endDate'])

educationHistory = pd.read_csv("../data/educationHistory.csv") # edHistoryID,careerPathID,edID,startDate,endDate
educationHistory['startDate'] = pd.to_datetime(educationHistory['startDate'])
educationHistory['endDate'] = pd.to_datetime(educationHistory['endDate'])

# -----------------------------------------------------------------------------------------------------------------

def calcTax(currecntTaxStructure, earnedIncome):
    tax_amt = 0
    for i in range(6):
        try:
            if earnedIncome < currecntTaxStructure["tax_bracket"].iloc[i]:
                if i==0: #first bracket
                    tax_amt += earnedIncome * currecntTaxStructure["tax_rate"].iloc[i]
                else:
                    tax_amt += (earnedIncome-currecntTaxStructure["tax_bracket"].iloc[i-1]) * currecntTaxStructure["tax_rate"].iloc[i]
                break

            elif earnedIncome > currecntTaxStructure["tax_bracket"].iloc[i]:
                if i ==0:
                    tax_amt += currecntTaxStructure["tax_bracket"].iloc[i] * currecntTaxStructure["tax_rate"].iloc[i]
                else:
                    taxable_amt = currecntTaxStructure["tax_bracket"].iloc[i] - currecntTaxStructure["tax_bracket"].iloc[i-1]
                    tax_amt += taxable_amt * currecntTaxStructure["tax_rate"].iloc[i]
        except:
            a = 0

    return tax_amt



# meta data
provinces = ["Saskatchewan", "Manitoba", "British Columbia", "Alberta", "Prince Edward Island", "Ontario", "Quebec", "Newfoundland and Labrador", "Nova Scoatia"]

allDfs = pd.DataFrame()
#preprocessing
for career_path_id in careerPaths["careerPathID"].unique():
    

    career_path_name = careerPaths[careerPaths["careerPathID"] == career_path_id]
    career_path_name = career_path_name["pathName"].iloc[0]

    careerDf = pd.DataFrame()

    #get career specific df's
    careerEmpHistory = employmentHistory[employmentHistory["careerPathID"] == career_path_id] #reference for timeline
    careerEdHistory = educationHistory[educationHistory["careerPathID"] == career_path_id] #reference for timeline    

    

    for year_adj in range(50):
        yearDf = pd.DataFrame()

        # Get Needed metadata
        # year
        year = 2026 + year_adj

        print(f"year: {year} & cur_career_path: {career_path_name}")
        try: #IF HAVE JOB
            #identify which job we're at 
            currentJobData = careerEmpHistory[(careerEmpHistory['startDate'].dt.year <= year) & (careerEmpHistory['endDate'].dt.year >= year)]
            currentJobID = currentJobData["jobDataID"].iloc[0] #assumes a single job
            currentJobData = jobData[jobData["jobDataID"] == currentJobID]

            current_endevor = currentJobData["jobName"].iloc[0]

            # identify which province we're in
            province = currentJobData["province"].iloc[0]

            # REVENUES
            wage = currentJobData["avgWage"].iloc[0]
            rate = 1 + currentJobData["avgYearlyWageIncrease"].iloc[0]
            wage_multiplier = 1.02
            rate = rate*wage_multiplier  #Added amplifier

            if year_adj != 0:
                earnedIncome = wage * (rate**year_adj)   
            else:
                earnedIncome = wage * (rate**year_adj)  

            print(f"year: {year_adj}")
            print(f"earned income: {earnedIncome}")

            # convert jobDataID to jobID
            trueJobID = currentJobData["jobID"].iloc[0]

            #skills ledger
            #jobSkillID,jobID,skillID
            skillsDevelopedThisYear = jobSkills[jobSkills["jobID"] == trueJobID]
            print(f"Employment Skills: ")

            #job, no educ
            expectedEducCost = 0

        except : #NO JOB --> EDUCATION
            #identify which education we're at
            currentEducationData = careerEdHistory[(careerEdHistory['startDate'].dt.year <= year) & (careerEdHistory['endDate'].dt.year >= year)]
            educationDataID = currentEducationData["educationDataID"].iloc[0]
            currentEdData = educationData[educationData["educationDataID"] == educationDataID]
            
            # identify which province we're in
            province = currentEdData["province"].iloc[0]

            #REVENUES 
            earnedIncome = currentEdData["expectedEarnings"].iloc[0] / currentEdData["years"].iloc[0] 
            print(f"earned ------- year_adj: {year_adj}")
            print(earnedIncome)


            #convert jobID to TrueJobID
            trueEdID = currentEdData["educationID"].iloc[0]       
            
            
            curEducation = education[education["educationID"]==trueEdID]
            current_endevor = curEducation["educationName"].iloc[0]
         

            #educ cost
            expectedEducCost = currentEdData["expectedCost"].iloc[0] / currentEdData["years"].iloc[0] 
            print(f"expected_educ_cost: {expectedEducCost}")

            #skills ledger
            #jobSkillID,edID,skillID
            skillsDevelopedThisYear = educationSkills[educationSkills["educationID"] == trueEdID]

            print(f"Education Skills: ")

            print("currentEdData")
            print(curEducation)


        # Skills / Capabilities Management
        print("Skills")
        skillIds = skillsDevelopedThisYear["skillID"].to_list()
        #print(f"skillIds")
        #print(skillIds)
        skillsDevelopedThisYear = skillsLedger[skillsLedger["skillID"].isin(skillIds)]
        print(f"developed this year")
        print(skillsDevelopedThisYear)

        skillsDevelopedThisYear = skillsDevelopedThisYear["skillName"].to_list()

        print(f"year: {year_adj} & cur_end: {current_endevor}")
        print(skillsDevelopedThisYear)

        
        

        #add every skill, increment experience, and level when hitting threshold
        skillData = {}
        allSkills = skillsLedger["skillName"].to_list()


        if year_adj > 0:
            previousSkillData = careerDf.iloc[len(careerDf)-1] #get last years data

            for skill_idx, skill in enumerate(allSkills):
                skillData[f"yrs_{skill}"] = previousSkillData[f"yrs_{skill}"]
            
        else: #year 0
            for skill_idx, skill in enumerate(allSkills):
                skillData[f"yrs_{skill}"] = 0


        #increment skills developed this year
        for skill_idx, skill in enumerate(allSkills):
            if skill in skillsDevelopedThisYear:
                skillData[f"yrs_{skill}"] += 1

        

        # tax calcs
        print(f"current tax structure: {province} and Fededral")

        # calculate tax - provincial
        currecntTaxStructure = tax_brackets[tax_brackets["province"] == province]
        currecntTaxStructure = currecntTaxStructure.sort_values("tax_bracket")
        prov_tax_amt = calcTax(currecntTaxStructure, earnedIncome)
        print(f"prov_tax_amt: {prov_tax_amt}")    

        currecntTaxStructure = tax_brackets[tax_brackets["province"] == "Federal"]
        currecntTaxStructure = currecntTaxStructure.sort_values("tax_bracket")
        fed_tax_amt = calcTax(currecntTaxStructure, earnedIncome)
        print(f"fed_tax_amt: {fed_tax_amt}")

        tax_amt = prov_tax_amt + fed_tax_amt
        print(f"tax_amt: {tax_amt}")


        #costs
        currentCpi = cpi[cpi["province"] == province]
        costs = {}
        for cost in currentCpi["costArea"].unique():
            currentCostCpi = currentCpi[currentCpi["costArea"] == cost]
            costAmt = currentCostCpi["baselineCost"].iloc[0] * ((1 + currentCostCpi["expectedYearlyIncrease"].iloc[0])**year_adj)
            costs[cost] = float(costAmt) * 12 #multiply monthly costs

        costs["educationCost"] = expectedEducCost

        costs["totalLivingCosts"] = sum(costVal for costVal in costs.values())    
    
        
        

        #compute other values
        expenditureBias = 0
        afterTaxIncome = earnedIncome - tax_amt
        netIncome = earnedIncome - tax_amt - costs["totalLivingCosts"] - expenditureBias
        amtSavedThisYear = netIncome


        #Investment Mechanism
        mechanisms = investment_mechanism["investmentMechanismName"]
        returns = investment_mechanism["avgYearlyReturn"]
        
        contributions = amtSavedThisYear

        investmentsAsOfThisYear = {}
        investmentsAsOfThisYear["contributions"] = contributions
        if year_adj > 0:
            previousYearData = careerDf.iloc[len(careerDf)-1] #get last years data

            for mech, return_ in zip(mechanisms, returns):
                amtFromLastYear = previousYearData[f"investment_{mech}"] * (1+return_)

                if amtSavedThisYear < 0:
                    amtSavedThisYear = 0 #Dont compound into the negatives

                investmentsAsOfThisYear[f"investment_{mech}"] = amtSavedThisYear + amtFromLastYear

        else:
            for mech, return_ in zip(mechanisms, returns):
                if amtSavedThisYear < 0:
                    amtSavedThisYear = 0 #Dont compound into the negatives
                    
                investmentsAsOfThisYear[f"investment_{mech}"] = amtSavedThisYear


        yearValues = {
                "year":year,
                "province":province,
                "career_path_name":career_path_name,
                "earnedIncome":float(earnedIncome),
                "prov_tax_amt":prov_tax_amt,
                "fed_tax_amt":fed_tax_amt,
                "tax_amt": float(tax_amt),
                "current_endevor": current_endevor,
                "afterTaxIncome": float(afterTaxIncome),
                "afterTaxAndCostsIncome": float(netIncome),
                "amtSavedThisYear":float(amtSavedThisYear),
                "expenditureBias": float(expenditureBias)
            }
        
        yearValues = {**yearValues, **costs, **investmentsAsOfThisYear, **skillData}

        print(f"year values: ")
        yearValues = pd.DataFrame([yearValues])
        print(yearValues)

        careerDf = pd.concat([careerDf, yearValues], axis=0)
        
    allDfs = pd.concat([allDfs, careerDf], axis=0)

print(allDfs)

allDfs.to_csv("../data/compiled_482_data.csv", index=False) 


#streamlit script in another document