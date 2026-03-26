### **Project Report: Sales Prediction using Linear Regression**

* **The Problem:** Businesses often struggle to know which factor (Ads vs. Discounts) actually drives sales. I chose this to see how much "weight" each variable carries.
* **The Approach:** I used a **Multiple Linear Regression** model. I added a "Bias" column (intercept) to the data matrix so the model could account for baseline sales. I chose NumPy for the math to understand the underlying linear algebra.
* **Key Decisions:** I chose to use `np.linalg.lstsq` because it is more numerically stable than manually calculating the inverse of the matrix.
* **Challenges Faced:** I initially struggled with the dimensions of the feature matrix $X$ when adding the bias column. I used `np.hstack` to fix this.
* **What I Learned:** I learned how raw data is converted into "Weights" that represent real-world importance. This is the foundation of most AI models.



