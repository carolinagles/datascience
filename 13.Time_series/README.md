# Taxi Demand Prediction with Machine Learning

## Project Overview
Sweet Lift Taxi has collected historical data on taxi orders at airports. To attract more drivers during peak hours, the company needs to predict the number of taxi orders for the next hour. This project focuses on building a predictive model for taxi demand.

The model must ensure that the **Root Mean Squared Error (RMSE) on the test set does not exceed 48**.

## Project Instructions
1. **Download and preprocess the dataset**:
   - The dataset is stored in `taxi.csv`.
   - Resample the data so that each data point falls within one-hour intervals.
2. **Analyze the data**:
   - Identify patterns, trends, and any data anomalies.
3. **Train multiple models with different hyperparameters**:
   - Use at least two different models (more is better).
   - Split the dataset, keeping **10% as the test sample**.
4. **Evaluate model performance**:
   - Assess predictions on the test set.
   - Provide conclusions based on results.

### Key Considerations:
- Use **Root Mean Squared Error (RMSE)** to evaluate model performance.
- Experiment with different machine learning models and compare their effectiveness.
- Optimize model performance while maintaining a balance between speed and accuracy.
- If necessary, adjust feature engineering techniques to improve predictions.

## Dataset Description

**Feature:**
- `num_orders` — Number of taxi orders.

This project aims to develop a reliable machine learning model to predict taxi demand efficiently, ensuring that it remains useful for real-world applications.

