# In Search of the Next 200 Oil Wells

## Overview

This project is focused on selecting the best locations to open 200 new oil wells for **OilyGiant**, a leading oil extraction company. The goal is to use predictive modeling to determine which wells will provide the highest reserves, assess risks, and maximize profitability.

## Project Objectives

- **Data Analysis**: Work with provided data on existing oil wells, which includes information about crude quality and reserve volume.
- **Predictive Modeling**: Use **linear regression** to build a model that predicts the reserve volumes in potential new wells.
- **Selection of Wells**: Identify the wells with the highest estimated reserve volumes.
- **Profitability Assessment**: Calculate the total profit for each region based on the selected wells and choose the region with the highest profit.
- **Risk Evaluation**: Use **bootstrapping** techniques to assess the risks and potential benefits of the selected regions.

## Requirements

- **Python**: The programming language used for data analysis and modeling.
- **pandas**: For data manipulation and analysis.
- **NumPy**: For numerical calculations.
- **scikit-learn**: For linear regression modeling.
- **bootstrapping**: For evaluating the risks associated with each region.

## Conditions

- **Data**: 500 data points are provided, from which the best 200 are selected to calculate total profit.
- **Budget**: The total budget for the 200 wells is **100 million USD**.
- **Revenue**: Revenue per barrel is **4.5 USD**, and revenue per product unit is **4500 USD** (reserve volume is in thousands of barrels).
- **Risk Assessment**: Only regions with a risk of loss lower than 2.5% will be considered.
- **Selection Criteria**: The region with the highest average profit among the qualifying regions will be selected.
