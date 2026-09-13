<div align="center">

# Workforce Insights Dashboard for Employee Skill and Analytics

**Predict Employee Skills • Analyze Workforce Trends • Empower HR Decisions with Data Analytics**

</div>

---

## Project Objective

Develop a Workforce Insights Dashboard to analyze employee skills, workforce performance, diversity, engagement, attrition risk, and HR metrics through interactive visualizations, enabling organizations to make informed, data-driven decisions.

---

# Project Overview

The Workforce Insights Dashboard is an analytics solution designed to provide a centralized view of workforce data and transform employee information into meaningful business insights.

The project combines data preparation, machine learning, workforce analytics, diversity analytics, engagement analytics, interactive visualizations, and Power BI reporting to support data-driven HR and workforce decisions.

The system analyzes employee information, workforce trends, attrition patterns, employee engagement, diversity metrics, workforce health indicators, and predictive insights.

---

# Key Features

- Workforce overview and KPI analysis
- Employee workforce analytics
- Department-wise workforce analysis
- Employee skill and workforce analysis
- Attrition analysis
- Machine learning-based predictive analytics
- Employee attrition risk analysis
- Workforce health score analysis
- Diversity analytics
- Employee engagement analytics
- Tenure-based workforce analysis
- Overtime and engagement analysis
- Interactive dashboard visualizations
- Power BI workforce intelligence dashboard
- ML model evaluation and insights
- Workforce trend analysis
- Comprehensive project documentation

---

# Project Architecture

The project follows a layered workforce analytics architecture:

```text
Data Sources
      ↓
Data Ingestion
      ↓
Data Validation
      ↓
Data Cleansing
      ↓
Data Transformation
      ↓
Workforce Data Repository
      ↓
Machine Learning & Analytics
      ↓
Power BI / Web Dashboard

Repository Structure

Workforce-Insights-Dashboard/
│
├── data/
│   ├── raw/
│   │   └── workforce_dataset.xlsx
│   │
│   ├── processed/
│   │   └── workforce_data_transformation.xlsx
│   │
│   └── ml_ready/
│       ├── ml_ready_dataset.csv
│       ├── X_train.csv
│       ├── X_test.csv
│       ├── y_train.csv
│       └── y_test.csv
│
├── frontend/
│   └── index.html
│
├── ml/
│   └── Model_Evaluation_and_Insights.ipynb
│
├── analytics/
│   ├── diversity/
│   │   ├── diversity_analytics.py
│   │   ├── diversity_analytics_outputs.xlsx
│   │   ├── clean_workforce_dataset.xlsx
│   │   └── charts/
│   │
│   └── engagement/
│       └── charts/
│
├── powerbi/
│   ├── Workforce_Intelligence_Dashboard.pbix
│   ├── workflow_transformations.pbix
│   └── Workforce_Intelligence_Dashboard_preview.pdf
│
├── docs/
│   ├── milestone1/
│   ├── milestone2/
│   ├── milestone3/
│   ├── project_description.docx
│   └── feature_classification.xlsx
│
├── reports/
│   ├── workforce_health_score_validation_report.docx
│   └── workforce_intelligence_dashboard_preview.pdf
│
├── tests/
│   └── milestone3_testing.xlsx
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE

Milestone 1: Workforce Data Requirements & Architecture
Workforce Data Requirements

The workforce analytics system collects and analyzes information from multiple HR domains.

Employee Information
Employee ID
Employee Name
Gender
Age
Department
Job Role
Location
Hire Date
Employment Status
Attendance
Payroll Data
Salary
Bonus
Incentives
Stock Options
Performance Data
Performance Rating
Manager Rating
Self Rating
Promotion History
Attrition Data
Exit Date
Exit Reason
Attrition Status
Years at Company
Learning Data
Skills
Training Hours
Certifications
Education

These data requirements support workforce planning, employee engagement analysis, and AI-based workforce insights.

System Analytics Specifications

The dashboard provides analytics through KPIs, reports, visualizations, and workforce insights.

Key Performance Indicators
Total Employees
Attrition Rate
Promotion Rate
Average Salary
Attendance Percentage
Job Satisfaction Score
Workforce Health Score
Training Completion
High Attrition Employees
Data Processing Workflow

The workforce data follows an ETL-oriented processing workflow:

ETL Pipeline
     ↓
Data Validation
     ↓
Data Cleansing
     ↓
Data Transformation
     ↓
Workforce Data Repository
     ↓
Dashboard & AI Analytics

The data integration process involves extracting data from available sources, transforming and cleaning the data, and preparing it for analytics and visualization.

Repository Architecture

The repository follows a layered architecture:

Data Sources
      ↓
Data Ingestion Layer
      ↓
Data Processing Layer
      ↓
Central Workforce Repository
      ↓
Machine Learning Models
      ↓
Analytics Dashboard

This architecture supports data ingestion, preprocessing, centralized storage, machine learning analysis, and workforce visualization.

Workforce Database Design

The documented workforce data architecture contains interconnected entities for storing and analyzing workforce information.

Major entities include:

Organization
Department
Employee
Job Position
Performance Review
Performance Goal
Attrition Record
Engagement Survey
Skills
Learning Records
Recruitment
Candidate
Data Source
Data Ingestion Log
Workforce Metrics
System User

Primary keys, foreign keys, and relationships are used to maintain data integrity and support workforce analytics.

Milestone 2: AI Analytics & Predictive Intelligence

Milestone 2 focuses on preparing workforce data for machine learning, predictive analytics, validation, and workforce intelligence.

Machine Learning Workflow
Workforce Dataset
       ↓
Data Preparation
       ↓
Feature Processing
       ↓
Train / Test Split
       ↓
Machine Learning Model
       ↓
Prediction
       ↓
Model Evaluation
       ↓
Workforce Insights
ML-Ready Dataset

The repository contains the following machine learning datasets:

data/ml_ready/

Files include:

ml_ready_dataset.csv
X_train.csv
X_test.csv
y_train.csv
y_test.csv

These datasets support model training, testing, evaluation, and predictive workforce analysis.

Model Evaluation

The machine learning model evaluation and insights are documented in:

ml/Model_Evaluation_and_Insights.ipynb

The notebook contains the machine learning analysis and evaluation workflow.

Analytics Engine Integration

The Analytics Engine Integration documentation describes how workforce analytics and attrition-prediction outputs can be connected to the dashboard.

Important model outputs include:

Predicted Class
Attrition Probability
Risk Category
Feature Importance
Model Evaluation Metrics

The documented integration architecture identifies the required connection points between attrition model outputs and the dashboard access layer.

Validation

Validation activities are included in the project documentation and testing materials.

The validation process focuses on ensuring that analytics outputs, workforce metrics, model outputs, and dashboard information remain consistent.

Milestone 3: Workforce Intelligence Analytics

Milestone 3 contains multiple workforce analytics modules including diversity analytics, engagement analytics, workforce health analysis, dashboard integration, and validation.

Diversity Analytics

The Diversity Analytics module provides insights into workforce demographics and employee characteristics.

Diversity Analysis Includes
Gender distribution
Age distribution
Department distribution
Education distribution
Job role distribution
Workforce demographic analysis

The implementation is available under:

analytics/diversity/
Diversity Analytics Files
analytics/diversity/
│
├── diversity_analytics.py
├── diversity_analytics_outputs.xlsx
├── clean_workforce_dataset.xlsx
└── charts/

The charts folder contains the generated diversity analytics visualizations.

Engagement Analytics

The Engagement Analytics module analyzes employee engagement and related workforce factors.

Engagement Analysis Includes
Employees by employee band
Attrition by employee band
Employee driver scores
Engagement by department
Engagement by tenure
Attrition by tenure
Engagement by overtime
Attrition by overtime

The engagement analytics visualizations are available under:

analytics/engagement/charts/
Workforce Health Score

The project includes workforce health score analysis as part of workforce intelligence.

The Workforce Health Score provides an aggregated indicator for analyzing workforce conditions and employee-related metrics.

Validation documentation is available under:

reports/
Power BI Workforce Intelligence Dashboard

The project includes an interactive Power BI dashboard for workforce analytics and visualization.

Power BI files are available under:

powerbi/

Main dashboard:

Workforce_Intelligence_Dashboard.pbix

A PDF preview is also included:

Workforce_Intelligence_Dashboard_preview.pdf
Dashboard Features

The Power BI dashboard provides:

Workforce overview
Employee analysis
Department analysis
Job role analysis
Attrition analysis
Diversity analytics
Engagement analytics
Workforce health indicators
KPI-based workforce insights
Interactive workforce visualizations
Workforce trend analysis
Workforce Dashboard Overview

The dashboard is designed to provide an executive-level view of workforce metrics.

Key workforce indicators include:

Total Employees
Active Employees
Attrition Rate
Promotion Rate
Workforce Health Score
Average Tenure

The dashboard also provides workforce visualizations and interactive analytics for different employee groups.

Frontend Workforce Dashboard

The project includes a web-based workforce dashboard interface.

The frontend is available at:

frontend/index.html

The interface provides interactive workforce analytics, navigation, KPI cards, and dashboard visualizations.

Frontend Capabilities
Workforce overview
Workforce KPI visualization
Employee analytics
Department analysis
Attrition analysis
Workforce health analysis
Interactive dashboard interface
Workforce insights visualization
Running the Project
Step 1: Install Python

Make sure Python 3.x is installed.

Check the installed Python version:

python --version
Step 2: Clone the Repository

Clone the repository using:

git clone <your-github-repository-url>

Move into the project directory:

cd Workforce-Insights-Dashboard
Step 3: Install Python Dependencies

Install the required libraries using:

pip install -r requirements.txt

The project uses Python libraries including:

Pandas
NumPy
Scikit-learn
OpenPyXL
Jupyter
Matplotlib
Running the Machine Learning Notebook

Start Jupyter Notebook:

jupyter notebook

Open:

ml/Model_Evaluation_and_Insights.ipynb

Run the notebook cells to review the machine learning workflow, model evaluation, and workforce insights.

Running the Diversity Analytics

The diversity analytics implementation is available at:

analytics/diversity/diversity_analytics.py

The script can be used to perform the documented diversity analytics workflow and generate analytical outputs.

Viewing the Frontend Dashboard

Open the following file in a modern web browser:

frontend/index.html

The HTML dashboard provides an interactive workforce analytics interface.

Viewing the Power BI Dashboard

Install Microsoft Power BI Desktop and open:

powerbi/Workforce_Intelligence_Dashboard.pbix

The included PDF preview can be used to review the dashboard without opening the Power BI file.

Project Documentation

All major project documentation is available under:

docs/

The documentation contains material related to:

Workforce data requirements
Repository architecture
Data workflows
Database architecture
AI workflow
Validation
Analytics Engine Integration
Diversity Analytics
Engagement Analytics
Dashboard development
Workforce health score
SAP connectivity design
Role-based collaboration
Project milestones
Reports

Project reports and validation documents are available under:

reports/

These include:

Workforce Health Score Validation Report
Workforce Intelligence Dashboard Preview
Testing

Testing and validation material is available under:

tests/

The repository contains:

tests/milestone3_testing.xlsx

This supports the documented Milestone 3 testing and validation activities.

Data & Analytics Workflow

The overall project workflow can be represented as:

Workforce Data
      ↓
Data Cleaning
      ↓
Data Transformation
      ↓
ML-Ready Dataset
      ↓
Machine Learning
      ↓
Diversity Analytics
      ↓
Engagement Analytics
      ↓
Workforce Health Analysis
      ↓
Power BI / Web Dashboard
      ↓
Workforce Insights
Technology Stack
Data Analytics
Python
Pandas
NumPy
OpenPyXL
Matplotlib
Machine Learning
Scikit-learn
Jupyter Notebook
Machine Learning Models
Model Evaluation
Dashboard & Visualization
HTML
CSS
JavaScript
Chart.js
Microsoft Power BI
Data Formats
CSV
Excel
PBIX
PDF
Jupyter Notebook
Enterprise Connectivity Architecture

The project documentation includes secure connectivity designs for enterprise HR systems such as SAP SuccessFactors and Workday.

The documented SAP connectivity architecture uses:

REST APIs
OAuth 2.0 authentication
HTTPS encryption
JSON data exchange
Incremental data synchronization

The architecture is designed to securely retrieve and synchronize workforce information for analytics.

User
  ↓
Dashboard
  ↓
Integration Service
  ↓
OAuth Authentication
  ↓
Enterprise HR API
  ↓
Employee Database
  ↓
Dashboard Reports

These connectivity components are documented as architecture/design and should not be interpreted as confirmed live enterprise integrations.

AI & RAG Preparation

The project documentation also includes preparation for future conversational workforce intelligence.

Potential use cases include:

HR policy questions
Workforce analytics questions
Employee-related insights
Workforce data querying

The documented Analytics Engine Integration material identifies RAG chatbot preparation as future work where implementation is dependent on the required data, ownership, and integration.

Security & Data Governance

The workforce analytics architecture considers data security and governance requirements.

Important principles include:

Protection of personally identifiable information
Role-Based Access Control
Secure API communication
Data access restrictions
Protection of sensitive workforce information
Secure AI and vector-store access
Regulatory compliance considerations

The documented architecture emphasizes protecting confidential employee and workforce information.

Project Outcomes

The Workforce Insights Dashboard provides a centralized analytics solution for understanding workforce data and generating actionable insights.

The project supports analysis of:

Workforce composition
Employee skills
Employee demographics
Department trends
Employee engagement
Attrition patterns
Diversity metrics
Workforce health
Machine learning predictions
Workforce performance
Workforce trends

These insights can support HR teams and organizational decision-makers in data-driven workforce planning and analysis.
