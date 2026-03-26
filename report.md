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