                                             
Project Overview:
This project predicts future sales using Machine Learning based on factors like advertising spend and discounts. It helps businesses make better decisions about inventory, marketing, and planning.


-How to Run the Project

1. Prerequisites
Ensure you have Python installed. You will also need the following libraries:
* Pandas: For data manipulation.
* NumPy: For numerical calculations.
* Matplotlib: For data visualization.

Install them all at once using:
```bash
pip install pandas numpy matplotlib
```

Features
•	To predict future sales using past data 
•	Uses Linear Regression 
•	Analyse business trends of real world 
•	Understand machine learning Concepts

 Technologies Use
•	Python
•	Pandas
•	NumPy 
•	Matplotlib
•	VS Code- Framework/Python IDLE

 Installation & Setup
Clone the Repository
git clone https://github.com/your-username/sales-prediction-ml.git
cd sales-prediction-ml
You can use VS Code (free, powerful, cross-platform code editor developed by Microsoft)/Python IDLE as environment setup
 
 Install Required Libraries
Make sure Python is installed, then run:

python -m pip install numpy
python -m pip install pandas
 python -m pip install matplotlib
or in one go
python -m pip install numpy pandas matplotlib
 
How to Run the Project
Run the main Python file:
python Main.py


Your sales data  should  be  like 
Season, Discount ,Advertising ,Sales
 Season-   [1, 1, 1.5] 
 Discount-  [0, 0.1,0.2]
 Ad_Spend- [50, 50, 100]
  Actual_Sales-[100, 105,30]


 How It Works
1.	Load dataset using Pandas
2.	Split data into training and testing sets
3.	Train model using Linear Regression
4.	Predict sales based on input features

Example Output
Predicted Sales: [250.5, 310.2, 420.7]


