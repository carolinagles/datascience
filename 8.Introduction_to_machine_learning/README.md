# Classification Model for Megaline Plans

## **Project Description**  
Megaline seeks to optimize the allocation of phone plans for its customers. The objective is to develop a classification model that analyzes customers' monthly behavior and recommends one of the two new plans: **Smart** or **Ultra**. This model will help identify patterns in call usage, text messages, and mobile data consumption to maximize customer satisfaction and operational efficiency.

---

## **Project Structure**

### **1. Data Exploration**  
- **Input File:** `datasets/users_behavior.csv`  
- **Column Descriptions:**  
  - `calls`: Total number of calls made during the month.  
  - `minutes`: Total duration of calls in minutes.  
  - `messages`: Number of messages sent.  
  - `mb_used`: Total mobile data usage in MB.  
  - `is_ultra`: Binary label for the current plan:  
    - **1:** Ultra.  
    - **0:** Smart.  

### **2. Data Segmentation**  
- Dataset split into:  
  - **Training (60%)**: To train the model.  
  - **Validation (20%)**: For hyperparameter tuning.  
  - **Test (20%)**: To evaluate the final model quality.  

### **3. Model Development**  
- **Task:** Create a supervised classification model to predict the plan (`is_ultra`).  
- **Algorithms Evaluated:**  
  - Decision Trees.  
  - Random Forests.  
  - Logistic Regression.  
- **Hyperparameter Optimization:**  
  - Tree depth.  
  - Number of estimators.  
  - Regularization parameters.  

### **4. Model Evaluation**  
- **Performance Metric:** Accuracy.  
- **Minimum Threshold:** 0.75 on the test set.  
- Conduct sanity checks to ensure model reliability on real-world data.  

---
