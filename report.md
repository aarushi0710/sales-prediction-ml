                      Project Report

Project Title- Sales Prediction using Machine Learning

   Student Name- Aarushi Srivastava
   
   Course - B-Tech (AIML)

 Introduction-Sales prediction is the process of estimating future sales using past
 data. It helps businesses in planning stock, marketing, and improving profit.

Objective of the Project- 
•	To predict future sales using past data 
•	To understand machine learning concepts 
•	To analyse business trends 

Problem Statement-Businesses often face difficulty in deciding how much stock to
keep. This project aims to predict future sales based on factors like advertising
and discounts.


Technologies Used
•	Python 
•	Pandas 
•	NumPy 
•	Matplotlib
•	VS Code- Framework/IDLE

Methodology Of Project-

•	 Data Acquisition and Pre-processing (Pandas)
 We utilized Pandas DataFrames to manage four primary independent variables
 (Features):
Dynamic Data: The sequential day of operation.
Seasonality: A categorical weight (e.g., 1.0 for Weekdays, 1.5 for Weekends) to
account for cyclic consumer behavior.
Discount Multiplier: Numerical representation of promotional activities.
Marketing Attribution: Quantitative data on advertising spend.


•	Mathematical Modeling (NumPy)
Rather than using high-level libraries, this project implements Multiple Linear
Regression from scratch using NumPy's Linear Algebra module. The goal is to solve
the linear equation:
y = w0 + w1x1 + w2x2 + w3x3 + epsilon
Where:
-y is the predicted Sales.
-w0 is the Intercept (Base Sales).
-w1, w2, w3 are the calculated weights (importance) of each feature.
We implemented the Ordinary Least Squares (OLS) method using np.linalg.lstsq. This
mathematical approach minimizes the sum of the squares of the vertical deviations 
between each data point and the line, ensuring the most accurate prediction 
possible.  


•	Predictive Logic and Constraint Satisfaction
Once the model is trained (weights are calculated), the system transitions into the
next phase.
Scaling Logic: Using NumPy vectorization, the model scales the requirements by the 
number of predicted customers.
Inventory Exhaustion Algorithm: The system runs a recursive loop that subtracts 
predicted daily sales from the current inventory. It identifies the "Critical Point"
to provide a lead-time warning to the user.


•	Data Visualization and Insights (Matplotlib)
The final stage converts numerical predictions into a Decision Support System (DSS).
Trend Analysis: A scatter-and-line plot compares historical actuals against the
model’s "Line of Best Fit."
Feature Impact Chart: A bar graph visualizes the weights ($w_n$) calculated by 
NumPy. This allows a business owner to see which factor (e.g., Ads vs. Discounts)
has the highest correlation with sales growth.
 

•	Advantages

  -Helps in business decision making 

  -Reduces loss 

  -Improves planning





•	Limitations

-Depends on data quality 

-Accuracy needs to be checked 





•	Future Scope

-We can  Add more features (festival, weather, Situation like War) 

-We can Use advanced models 

-We can Integrate with web app or mobile app and can be made
 more responsive.               



 • Challenges Faced

 -It was difficult to create the critical threshold part which calculates and
 reminds the developer of the finishing stock in advance.

 -Instead of using high level libraries I tried to work it out with normal usable
 libraries like numpy to implement linear regression logic. This required a better
 understanding of the language and library.


 • What I learned
 
  -I learnt to actually implement the libraries and language properly for creating
 the project.
 
  -Actually understood how to use the libraries for their purpose and had a deeper
 understanding of the language and library now that I used them a lot I will
 remember what commands are used for what purpose.









