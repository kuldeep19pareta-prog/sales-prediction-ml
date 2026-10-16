# Sales Prediction Using Machine Learning

## Project Overview
This project predicts product sales based on advertising budgets spent on TV, Radio, and Newspaper using Machine Learning.

The project uses Python for data analysis, Scikit-learn for model training, SQL for storing prediction history, and Gradio for creating a user-friendly prediction interface.

## Technologies Used
- Python
- Pandas and NumPy
- Matplotlib
- Scikit-learn
- SQL / SQLite
- Gradio
- Jupyter Notebook / Google Colab

## Dataset
The project uses the Advertising dataset containing 200 observations and three advertising features:
- TV
- Radio
- Newspaper

**Target variable:** Sales

## Machine Learning Workflow
1. Load and inspect the dataset.
2. Clean the data and check for data quality issues.
3. Perform exploratory data analysis and visualize relationships.
4. Split the data into training and testing sets.
5. Train and evaluate Linear Regression and Random Forest models.
6. Compare models using MAE, RMSE, and R².
7. Save the trained model for predictions.

## Model Performance
Random Forest achieved the following results on the current test split:

| Metric | Score |
|---|---:|
| MAE | 0.6287 |
| RMSE | 0.7572 |
| R² | 0.9818 |

These are results from the current experiment and may vary with a different data split or setup.

## Project Status
- [x] Data analysis and visualization
- [x] Model training and evaluation
- [x] Model saved using Joblib
- [ ] Prediction interface
- [ ] SQL prediction history integration
- [ ] Final testing and documentation

## How to Run
The notebook can be opened in Google Colab to reproduce the analysis and model training. Additional setup instructions for the prediction application will be added when the app is ready.

## Disclaimer
This is an educational machine learning project. Predictions are estimates based on the supplied dataset and should not be treated as guaranteed business outcomes.
