# Analysis on Watershed Projects in India

## Overview

This project analyzes watershed development projects across India to evaluate beneficiary outcomes, fund flow efficiency, and the estimated cost per hectare. Using government data, the study examines how project budgets and expenditures relate to employment generation and farmer benefits, identifies variations in fund utilization across states, and applies machine learning to support cost estimation.

The project was completed as part of the M.Sc. Computer Science (Data Analytics) program at Rajagiri College of Social Sciences (Autonomous), during 2023–2025.

## Objectives

### 1. Beneficiary Assessment of Watershed Projects
Analyze project budgets, execution, mandays generated, and farmers benefited to understand the financial and socio-economic outcomes of watershed projects across states.

### 2. Fund Flow Efficiency Analysis
Evaluate the movement of funds from sanctioned budgets through treasury releases to expenditure. Calculate fund release, expenditure, and overall utilization efficiency, and use clustering to identify differences in state-level performance.

### 3. Cost per Hectare Prediction
Develop a Random Forest Regression model to estimate the cost per hectare of watershed projects using investment, funding contributions, project area, and location-related features.

## Dataset

The study uses data from the Watershed Development Component of PMKSY 2.0 Management Information System, under the Department of Land Resources, Ministry of Rural Development, Government of India.

The datasets cover:

- **Sanctioned Projects:** State, district, financial year, project details, sanctioned area, total cost, central share, and state share.
- **Farmers Benefited and Mandays Generated:** Employment generation and beneficiary categories, including SC, ST, female, small, marginal, landless, and BPL farmers.
- **Total Expenditure:** Expenditure recorded at district, block, gram panchayat, and village levels.
- **Treasury Receipts:** State and central fund releases through the state treasury.

## Tools and Technologies

- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
- **Data Analysis:** Data Cleaning, Data Preprocessing, Exploratory Data Analysis (EDA), Correlation Analysis
- **Machine Learning:** K-Means Clustering, Random Forest Regression
- **Visualization:** Power BI
- **Environment:** VS Code, Google Colab

## Methodology

1. **Data Preprocessing:** Combined state-wise Excel files, converted data types, calculated expenditure and beneficiary totals, and aggregated datasets.
2. **Exploratory Data Analysis:** Examined project budgets, project counts, employment generation, farmer benefits, and expenditure patterns.
3. **Beneficiary Assessment:** Used statistical analysis, correlation analysis, charts, and geographical maps to study project outcomes.
4. **Fund Flow Analysis:** Calculated release efficiency, expenditure efficiency, and overall utilization, then applied K-Means clustering to group states by performance.
5. **Predictive Modeling:** Engineered funding ratios and location-related features and trained a Random Forest Regressor to estimate cost per hectare.
6. **Visualization:** Created analytical charts and geographical visualizations to communicate findings.

## Key Findings

- **Project Cost and Project Count:** A strong positive correlation of approximately 0.96 was observed between total project cost and the number of projects.
- **Cost and Employment:** Total project cost and mandays generated showed a moderate positive correlation of approximately 0.51.
- **Cost and Farmer Benefits:** The correlation between total project cost and farmers benefited was approximately 0.29, indicating that higher spending did not necessarily correspond to proportionately higher beneficiary counts.
- **State-Level Fund Efficiency:** K-Means clustering grouped states into three performance categories:
  - Inefficient Spenders
  - Slow Receivers, Efficient Spenders
  - High Performers
- **Cost Prediction:** The Random Forest Regression model achieved an R² score of approximately 0.88 for the cost-per-hectare prediction task.

## Repository Structure

- `README.md` — Project overview, objectives, methodology, and findings.
- `Watershed Project Presentation.pdf` — Project presentation and report.
- `Graphs and Images/` — Charts, graphs, maps, and other project visualizations.
- `Datasets/` — Relevant datasets and scripts used in the analysis.

## Limitations and Future Scope

The analysis relies on historical data, and variations in data availability and consistency across states may affect comparisons. Future improvements could incorporate updated datasets, satellite imagery, climate information, more granular district-level analysis, and an interactive dashboard for decision-makers.

## Academic Context

**Project Title:** Analysis on Watershed Projects in India  
**Program:** M.Sc. Computer Science (Data Analytics)  
**Institution:** Rajagiri College of Social Sciences (Autonomous)  
**Project Year:** 2025

