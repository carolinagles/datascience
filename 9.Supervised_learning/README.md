# Customer Churn Prediction for Beta Bank


## Project Description

Beta Bank is facing a growing issue where customers are leaving the bank every month. Bankers have discovered that retaining existing customers is more cost-effective than acquiring new ones.

Our goal is to predict whether a customer is likely to leave the bank in the near future. We have data on past customer behavior and contract termination with the bank.

We aim to build a model that achieves the highest possible F1 score. To pass the project review, the F1 score must be at least 0.59. The F1 score will be validated on the test set.

Additionally, the AUC-ROC metric will be calculated and compared with the F1 score.

---

## Project Instructions

### 1. Data Preparation
- Download and prepare the dataset.
- Provide a detailed explanation of the data preparation steps, including handling missing values, encoding categorical variables, and scaling features.

### 2. Examine Class Imbalance
- Analyze the class distribution in the dataset to determine if there is an imbalance.
- Train an initial model without addressing the class imbalance.
- Briefly summarize the findings, focusing on how the imbalance affects the model's performance.

### 3. Improve Model Quality
- Enhance the model's performance by addressing the class imbalance using at least **two different approaches** (e.g., oversampling, undersampling, or class weighting).
- Use separate training and validation sets to identify the best model and parameter combination.
- Train different models on the training and validation sets.
- Select the best-performing model based on validation results.
- Provide a concise summary of the methods used and findings.

### 4. Final Testing
- Perform the final evaluation on the test set.
- Compare the F1 score and AUC-ROC metric, discussing their implications.

---


## Libraries and Their Usage

### General-Purpose Libraries
- **pandas**: For handling and manipulating datasets, such as loading, cleaning, and analyzing data.
- **numpy**: Provides support for mathematical operations and efficient handling of arrays and numerical data.
- **re**: For working with regular expressions, used for text cleaning or pattern matching.
- **matplotlib.pyplot**: For creating visualizations such as plots, charts, and graphs to analyze data.
- **warnings**: Used to suppress warning messages to keep the notebook clean and focused.

### Machine Learning Libraries (scikit-learn)
- **DecisionTreeClassifier**: A tree-based model used for classification tasks.
- **RandomForestClassifier**: An ensemble method combining multiple decision trees for better accuracy and robustness.
- **LogisticRegression**: A linear model used for binary classification problems.
- **train_test_split**: Splits data into training and testing sets for model evaluation.
- **GridSearchCV**: Performs hyperparameter tuning to find the best model configuration.
- **StandardScaler**: Scales features to have a mean of 0 and a standard deviation of 1, improving model performance on some algorithms.
- **shuffle**: Shuffles data to avoid bias during splitting or processing.
- **recall_score, precision_score, f1_score**: Metrics for evaluating the performance of classification models.
- **roc_auc_score, roc_curve**: Metrics and tools for assessing model performance with ROC curves and AUC scores.

### Imbalanced-Learn Library
- **SMOTE**: Synthetic Minority Oversampling Technique; used to address class imbalance by generating synthetic samples for the minority class.

---

