# Insurance Data Analysis with Machine Learning

## Project Overview
Sure Tomorrow, an insurance company, aims to leverage machine learning to address several tasks related to customer insights and prediction models. This project evaluates the feasibility of using machine learning for the following tasks:

### Task 1: Finding Similar Customers
Identifying customers similar to a given one can help the company's agents optimize marketing strategies and improve customer outreach.

### Task 2: Predicting Eligibility for Insurance Benefits
This task involves training a predictive model to determine whether a new customer is likely to receive an insurance benefit. A key question to address is: Can a trained model outperform a dummy model? If not, what could be the reasons?

### Task 3: Predicting the Number of Insurance Benefits
A linear regression model is used to predict the number of insurance benefits a new customer is likely to receive based on their demographic and financial attributes.

### Task 4: Data Protection and Privacy Preservation
The goal is to implement a data transformation algorithm that ensures personal data protection while maintaining the performance of machine learning models. This technique, known as data masking or data obfuscation, must prevent unauthorized access to sensitive information without compromising model accuracy.

## Project Instructions
1. **Load the dataset**: The dataset is stored in `insurance_us.csv`.
2. **Data validation**: Ensure data quality by checking for missing values, outliers, and inconsistencies.
3. **Task execution**: Implement solutions for each task and answer the relevant questions.
4. **Draw conclusions**: Summarize findings based on the project experience.

The project template includes some prewritten code and two appendices with useful information. You are encouraged to build upon the existing code and complete any unfinished sections before proceeding.

## Dataset Description
- **Features**:
  - `sex`: Gender of the insured person.
  - `age`: Age of the insured person.
  - `salary`: Annual income of the insured person.
  - `family_members`: Number of family members associated with the insured person.
- **Target Variable**:
  - `insurance_benefits`: Number of insurance benefits received in the past five years.