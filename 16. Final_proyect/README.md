# Interconnect Insights: Customer Churn Prediction


## Project Overview

This project aims to build a binary classification model to predict customer churn for **Interconnect**, a telecommunications operator. The goal is to help the company proactively retain customers by identifying those most likely to cancel their service. The target variable is **Churn** (Yes/No), and the main evaluation metric is **AUC-ROC**, with a minimum threshold of **0.85**. Additionally, we use **F1-score** (threshold: 0.75) and **accuracy** for model evaluation.


The dataset includes customer information regarding:

* **Personal details**
* **Contract information**
* **Internet and phone services subscribed**

## Data Sources

The data is split across four files:

* `contract.csv` – Contract-related details
* `personal.csv` – Customer personal information
* `internet.csv` – Internet service subscriptions
* `phone.csv` – Phone service subscriptions

All files share the unique identifier `customerID`. The contract data is valid from **February 1, 2020**.

##  Libraries Used

###  Data Handling

* `pandas` – Data manipulation and analysis
* `numpy` – Numerical operations
* `re` – Regex for text processing

###  Visualization

* `matplotlib.pyplot` – Plotting charts and graphs

###  Utilities

* `time` – Model timing
* `warnings` – Suppress warning messages

###  Machine Learning & Metrics

* `sklearn`:

  * `train_test_split` – Data splitting
  * `StandardScaler` – Feature scaling
  * `roc_auc_score`, `f1_score`, `accuracy_score` – Evaluation metrics
  * `DummyClassifier` – Baseline model
  * `LogisticRegression` – Simple classification model
  * `GridSearchCV`, `RandomizedSearchCV` – Hyperparameter tuning
  * `confusion_matrix`, `roc_curve`, `auc` – Performance visualization

* `imblearn.over_sampling.SMOTE` – Oversampling for class imbalance

###  Advanced Models

* `lightgbm.LGBMClassifier` – Gradient boosting model (fast & efficient)
* `xgboost.XGBClassifier` – eXtreme Gradient Boosting
* `catboost.CatBoostClassifier` – Gradient boosting optimized for categorical features

--- 

### This project was developed as the final capstone for the TripleTen Data Science Bootcamp. I completed the entire process from scratch, including data preprocessing, exploratory analysis, model training, evaluation, and optimization, to demonstrate my ability to apply data science techniques to real world business problems. The goal was to showcase my end to end proficiency in building predictive models and deriving actionable insights.

