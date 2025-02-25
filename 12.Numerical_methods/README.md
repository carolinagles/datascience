# Used Car Price Prediction with Machine Learning

## Project Overview
Rusty Bargain, a second-hand car sales service, is developing an app to attract new customers. This app allows users to quickly determine the market value of their cars by providing access to historical data, technical specifications, equipment versions, and pricing information. The goal of this project is to build a model that accurately predicts the market value of a car.

Rusty Bargain is interested in:
- **Prediction quality**
- **Prediction speed**
- **Training time**

## Project Instructions
1. **Download and examine the dataset**: The dataset is stored in `car_data.csv`.
2. **Train multiple models with different hyperparameters**:
   - Train at least two different models (more is preferred).
   - Compare gradient boosting methods with random forests, decision trees, and linear regression.
3. **Analyze model speed and quality**.

### Key Considerations:
- Use **Root Mean Squared Error (RMSE)** as the evaluation metric.
- **Linear regression** serves as a sanity check. If gradient boosting performs worse, something is wrong.
- Learn about **LightGBM** and its gradient boosting tools.
- The project should include:
  - **Linear regression** for a baseline sanity check.
  - **A tree-based algorithm** with hyperparameter tuning (preferably a random forest).
  - **LightGBM** with hyperparameter tuning (test multiple parameter sets).
  - **Optional**: Implement **CatBoost** and **XGBoost** with hyperparameter tuning.
- Consider how categorical features are encoded:
  - LightGBM and CatBoost handle them natively.
  - XGBoost requires One-Hot Encoding (OHE).
- Use a special Jupyter Notebook command to measure execution time.
- Given that gradient boosting training can be slow, modify only a few parameters to optimize performance.
- If Jupyter Notebook crashes, free up memory using:
  ```python
  del features_train
  ```

## Dataset Description

**Features:**
- `DateCrawled` — Date when the profile was downloaded from the database.
- `VehicleType` — Type of car body.
- `RegistrationYear` — Vehicle registration year.
- `Gearbox` — Type of transmission.
- `Power` — Horsepower (HP).
- `Model` — Vehicle model.
- `Mileage` — Mileage (in km, based on regional dataset specifications).
- `RegistrationMonth` — Month of vehicle registration.
- `FuelType` — Type of fuel.
- `Brand` — Vehicle brand.
- `NotRepaired` — Indicates if the vehicle has been repaired or not.
- `DateCreated` — Date when the profile was created.
- `NumberOfPictures` — Number of vehicle photos.
- `PostalCode` — Postal code of the profile owner.
- `LastSeen` — Date when the user was last active.

**Target Variable:**
- `Price` — Price of the vehicle (in euros).

This project aims to build a robust machine learning model that effectively estimates used car prices while balancing prediction quality, speed, and training efficiency.

