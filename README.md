#  Sales Impact Predictor (ML)

A Python-based machine learning tool that uses \*\*Multiple Linear Regression\*\* to analyze how discounts and advertising spend affect historical sales.**



#  Project Overview

This project avoids high-level ML libraries like Scikit-Learn to demonstrate the underlying \*\*Linear Algebra\*\* of regression. It solves for "Weights" using the Least Squares method:**

**$$X^T Xw = X^T y$$**



#  Tech Stack

Language : Python 3.x

Data Management: Pandas, NumPy

Visualization: Matplotlib



# Features

Matrix Operations: Uses NumPy's `linalg.lstsq` for solving weights.

Bias Integration: Automatically adds a bias (intercept) column to the feature matrix.

Predictive Analysis: Includes a function to forecast sales for future marketing scenarios.

Visual Insights: Generates plots for Model Accuracy and Feature Importance.**



#  How to Run

1.Clone the repository:

&#x20;  ```bash

&#x20;  git clone \[https://github.com/aarushi0710/sales-prediction-ml.git](https://github.com/aarushi0710/sales-prediction-ml.git)**

Install dependencies:
Make sure you have Python installed, then run:
pip install pandas numpy matplotlib

Execute the script:
python main.py


---

 1. Pull the changes from GitHub to sync up
git pull origin main --rebase

 2. Now try pushing again
git push origin main


---

#Step 5: Connect to GitHub
1.  Go to GitHub and create a new public repository named `sales-prediction-ml`.
2.  Copy the URL.
3.  Run these in your terminal:
    ```bash
    git remote add origin YOUR_REPOSITORY_URL
    git branch -M main
    git push -u origin main
    ```

---


