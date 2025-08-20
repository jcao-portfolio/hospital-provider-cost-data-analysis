# 🏥 Hospital Provider Cost Report Data Analysis
## Exploratory Data Analysis on Hospital Provider Cost Data

## General Overview
This project analyzes **Medicare Hospital Provider Cost Report** data to uncover insights into healthcare provider expenses, utilization patterns, and geographic disparities. The goal is to clean, validate, and visualize hospital cost data for meaningful healthcare analytics.

## Background
The Hospital Provider Cost Report dataset, published by CMS, contains annual self-reported financial and utilization data from U.S. hospitals participating in Medicare. It includes information on hospital costs, revenues, ownership types, and patient statistics, making it a key resource for analyzing healthcare expenses, efficiency, and regional disparities.

## Key Insights
- State-Level Trends: Certain states consistently report higher hospital costs, highlighting regional disparities in healthcare expenses.
- Ownership Differences: Nonprofit hospitals generally report different cost structures compared to proprietary and government-owned facilities.
- Service Utilization: Inpatient vs. outpatient service costs reveal variations in how hospitals allocate resources.
- Time-Based Patterns: Year-over-year analysis shows shifts in hospital expenditures, potentially linked to policy changes or economic factors.
- Data Quality Observations: Missing values and outliers are common in self-reported data, requiring robust cleaning and validation for accurate insights.
### Business Questions
1. Which states/regions have the highest number of hospital beds?
2. How does hospital size (beds, employees) relate to net income?
3. What is the cost-to-charge ratio across hospitals?
4. How much uncompensated care is provided, and where is it concentrated?
5. How do Medicaid and Medicare utilization differ across hospitals?
6. Which hospitals/states have the highest DSH adjustments?
7. Do urban vs. rural hospitals perform differently in net income/revenue?
8. What is the inpatient vs. outpatient revenue mix?
9. Which hospitals show financial distress (negative net income)?
10. How does teaching hospital status affect finances?

## Objectives
The objective of this study is to develop and showcase strong data analysis skills through a meaningful project addressing real-world healthcare data challenges. The insights derived from the analysis are intended to assist stakeholders in making informed decisions regarding hospital resource allocation, cost management, and regulatory oversight.

- Data Cleaning & Preparation: Handle missing values, duplicates, and formatting issues to ensure reliable analysis.
- Data Quality Checks: Identify outliers, validate data types, and confirm consistency across reporting periods.
- Cost Trend Analysis: Explore hospital cost patterns across years, states, and provider types.
- Ownership Comparisons: Compare expenses and performance between nonprofit, government, and proprietary hospitals.
- Geographic Insights: Highlight state and regional differences in provider costs and utilization.
- Visualization & Reporting: Create charts, dashboards, and summaries to communicate key findings effectively.
- Portfolio Demonstration: Showcase practical skills in Python, SQL, and visualization tools for healthcare analytics.

## Tools & Technologies
- Python: Data cleaning, transformation, and analysis (Pandas, NumPy)
- Visualization: Matplotlib, Seaborn for charts and trend analysis
- Jupyter Notebook: Interactive analysis and documentation
- Microsoft Excel: Data exploration, validation, and quick summaries
- Power BI / Tableau (optional): Interactive dashboards for stakeholders
- Git & GitHub: Version control and project collaboration
- CMS Medicare Cost Report Data: Public dataset used for analysis

## Data Source
This report provides an in-depth analysis of hospital provider enrollment and cost data obtained from the Provider Enrollment, Chain, and Ownership System (PECOS). Following the July 17, 2023 data refresh, the dataset was expanded to include additional provider types such as Critical Access Hospitals (CAH) and Rural Emergency Hospitals (REH), broadening the scope of the analysis.

The Hospital Provider Cost Report dataset provides select measures from the hospital annual cost report. This data includes provider information such as facility characteristics, utilization data, cost and charges by cost center (in total and for Medicare), Medicare settlement data, and financial statement data organized by CMS Certification Number.

The data is publicly available from the Centers for Medicare & Medicaid Services [CMS](https://data.cms.gov/provider-compliance/cost-report/hospital-provider-cost-report).

## Folder Structure:
- /data/raw – untouched downloads
- /data/interim – cleaned subsets
- /data/processed – ready for analysis
- /notebooks – Jupyter files
- /scripts – Python scripts

## Getting Started
Follow these steps to set up and run the project locally:  

### 1. Clone the repository  
```bash
git clone https://github.com/jcao-portfolio/hospital-provider-cost-data-analysis.git
```

## Contact Information
- LinkedIn: www.linkedin.com/in/jason-cao30
- Email: jcao3030@gmail.com
