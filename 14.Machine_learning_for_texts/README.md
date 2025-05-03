# Film Junky Union - Movie Review Classifier

## Project Overview

The **Film Junky Union** project focuses on creating a system to automatically filter and classify movie reviews as positive or negative. The dataset used for this project consists of labeled IMDB movie reviews, where each review is marked as either positive (1) or negative (0). The primary goal is to build a model that can accurately predict whether a review is positive or negative, with an F1 score of at least 0.85.

In this project, we will go through the steps of data preparation, model training, evaluation, and fine-tuning, as well as analyzing the results to ensure that the model performs robustly. The process includes handling class imbalance, trying multiple machine learning models, and evaluating their performance using different metrics.

---

## Steps of the Project

### 1. Data Loading and Preparation
The first step is to load the provided dataset, which consists of movie reviews. This data is stored in a tab-separated file (`imdb_reviews.tsv`). Once the data is loaded, we will perform several data preprocessing steps:
- **Text Cleaning**: We'll clean the text by removing unnecessary characters such as punctuation, digits, and converting text to lowercase.
- **Handling Missing Values**: If there are any missing or incomplete data entries, they will be addressed.
- **Feature Engineering**: We'll convert the text data into a suitable format for machine learning models. This might involve tokenization, stemming, and lemmatization.

### 2. Exploratory Data Analysis (EDA)
Before diving into model training, it's crucial to understand the data:
- We'll examine the class distribution (positive vs. negative reviews) to check for any imbalance.
- Visualize the data to gain insights into the review length, word frequency, and other useful patterns.
- This analysis will also help inform decisions about how to handle class imbalance if needed.

### 3. Data Preprocessing for Modeling
Once the data is prepared, we will:
- Tokenize the text data to break it down into smaller components (words or phrases).
- Use techniques like **TF-IDF** (Term Frequency-Inverse Document Frequency) to convert the text into numerical vectors, which are used as features in machine learning models.
- Standardize or normalize the features if required to ensure that the model performs optimally.

### 4. Model Training
With the preprocessed data, we will train at least three different models. These models could include, but are not limited to:
- **Logistic Regression**: A simple, yet effective, model for binary classification tasks.
- **Gradient Boosting Machines (GBM)**: A powerful ensemble method that often provides high accuracy.
- **Random Forest**: Another ensemble method that combines multiple decision trees to improve model performance.

Each model will be trained on the training dataset, and we will evaluate its performance using various metrics, including the **F1 score**, **accuracy**, and **AUC-ROC**.

### 5. Model Evaluation and Comparison
Once the models are trained, we will evaluate their performance using the test dataset. We will:
- Compare the F1 scores of each model to determine which one is performing the best.
- Calculate **AUC-ROC** scores to assess the model’s ability to discriminate between positive and negative reviews.
- Review the accuracy of the models to see how often they correctly classify the reviews.

### 6. Handling Class Imbalance
If the dataset shows significant class imbalance (more positive or negative reviews), we will address this issue using techniques such as:
- **Oversampling** the minority class.
- **Undersampling** the majority class.
- **Class weighting**: Adjusting the importance of each class during model training.

We will apply at least two different strategies to see how they affect the model's performance.

### 7. Fine-Tuning and Hyperparameter Optimization
Using techniques like **GridSearchCV** or **RandomizedSearchCV**, we will fine-tune the model’s hyperparameters to improve its performance. This involves trying different combinations of parameters (e.g., learning rates, regularization terms) to find the best set for our data.

### 8. Final Testing and Reporting
After fine-tuning, we will run the final evaluation on the test set. The final goal is to achieve an F1 score of at least 0.85. We will summarize our findings, including:
- The final model's performance on the test set.
- A comparison of the F1 score, accuracy, and AUC-ROC.
- An analysis of any potential model weaknesses or areas for improvement.

We will also provide a set of **sample reviews** to classify using the best-performing model and compare how different models handle the same data.

---

## Data Description

The dataset used for this project is stored in the file `imdb_reviews.tsv`. This dataset contains labeled movie reviews with the following fields:

- **review**: The text of the movie review.
- **pos**: The target label, where '0' indicates a negative review and '1' indicates a positive review.
- **ds_part**: Indicates whether the data belongs to the training or test set (`train`/`test`).

This dataset was provided by Andrew L. Maas et al., and it is a well-known benchmark for sentiment analysis.

---

## Libraries and Tools Used

- **pandas**: For loading and manipulating the data.
- **numpy**: For numerical operations and data transformations.
- **matplotlib & seaborn**: For creating visualizations to explore the data.
- **scikit-learn**: For machine learning models, metrics, and data processing (e.g., Logistic Regression, Random Forest, GridSearchCV).
- **nltk**: For text processing tasks such as tokenization and lemmatization.
- **imbalanced-learn**: For handling class imbalance (e.g., SMOTE for oversampling).

---

## Evaluation Criteria

The model's performance will be evaluated based on the following metrics:
- **F1 Score** (target is at least 0.85).
- **Accuracy**.
- **AUC-ROC** (Area Under the Receiver Operating Characteristic Curve).

Additionally, the project's success will be determined by the ability to handle class imbalance and the overall quality of the model comparison and evaluation.

Good luck with your project!