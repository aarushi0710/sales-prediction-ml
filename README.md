**#  Sales Impact Predictor (ML)**

**A Python-based machine learning tool that uses \*\*Multiple Linear Regression\*\* to analyze how discounts and advertising spend affect historical sales.**



**##  Project Overview**

**This project avoids high-level ML libraries like Scikit-Learn to demonstrate the underlying \*\*Linear Algebra\*\* of regression. It solves for "Weights" using the Least Squares method:**

**$$X^T Xw = X^T y$$**



**##  Tech Stack**

**\* \*\*Language:\*\* Python 3.x**

**\* \*\*Data Management:\*\* Pandas, NumPy**

**\* \*\*Visualization:\*\* Matplotlib**



**##  Features**

**\* \*\*Matrix Operations:\*\* Uses NumPy's `linalg.lstsq` for solving weights.**

**\* \*\*Bias Integration:\*\* Automatically adds a bias (intercept) column to the feature matrix.**

**\* \*\*Predictive Analysis:\*\* Includes a function to forecast sales for future marketing scenarios.**

**\* \*\*Visual Insights:\*\* Generates plots for Model Accuracy and Feature Importance.**



**##  How to Run**

**1. \*\*Clone the repository:\*\***

&#x20;  **```bash**

&#x20;  **git clone \[https://github.com/aarushi0710/sales-prediction-ml.git](https://github.com/aarushi0710/sales-prediction-ml.git)**

Install dependencies:
Make sure you have Python installed, then run:
pip install pandas numpy matplotlib

Execute the script:
python main.py


---



### **Project Report: Sales Prediction using Linear Regression**

* **The Problem:** Businesses often struggle to know which factor (Ads vs. Discounts) actually drives sales. I chose this to see how much "weight" each variable carries.
* **The Approach:** I used a **Multiple Linear Regression** model. I added a "Bias" column (intercept) to the data matrix so the model could account for baseline sales. I chose NumPy for the math to understand the underlying linear algebra.
* **Key Decisions:** I chose to use `np.linalg.lstsq` because it is more numerically stable than manually calculating the inverse of the matrix.
* **Challenges Faced:** I initially struggled with the dimensions of the feature matrix $X$ when adding the bias column. I used `np.hstack` to fix this.
* **What I Learned:** I learned how raw data is converted into "Weights" that represent real-world importance. This is the foundation of most AI models.

---

## **Step 5: Connect to GitHub**
1.  Go to GitHub and create a new public repository named `sales-prediction-ml`.
2.  Copy the URL.
3.  Run these in your terminal:
    ```bash
    git remote add origin YOUR_REPOSITORY_URL
    git branch -M main
    git push -u origin main
    ```

---


## **Final Submission Check**
* **GitHub Link:** Copy your repo URL (e.g., `https://github.com/aarushi0710/sales-prediction-ml`).
* **Commits:** Click "Commits" on GitHub. It should show 3 separate updates (Code -> README -> Report).
* **README:** Make sure the "How to Run" section is clear.