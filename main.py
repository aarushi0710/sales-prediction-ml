import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = {
    'Day': np.arange(1, 11),
    'Season': [1, 1, 1, 1, 1, 1.5, 1.5, 1, 1, 1], 
    'Discount': [0, 0, 0.1, 0, 0, 0.2, 0.2, 0, 0, 0.1],
    'Ad_Spend': [50, 50, 100, 50, 50, 200, 200, 50, 50, 150],
    'Actual_Sales': [100, 105, 140, 108, 110, 250, 260, 115, 118, 180]
}
df = pd.DataFrame(data)


# Using NumPy's Least Squares to find the 'Weights' of each
X = df[['Season', 'Discount', 'Ad_Spend']].values
X = np.hstack([np.ones((X.shape[0], 1)), X]) 
y = df['Actual_Sales'].values

# Calculate weights
weights, residuals, rank, s = np.linalg.lstsq(X, y, rcond=None)

# PREDICTION code
def predict_sales(season, discount, ads):
    input_data = np.array([1, season, discount, ads])
    return np.dot(input_data, weights)

# Future Scenario: Upcoming Weekend Sale
future_weekend_sale = predict_sales(1.5, 0.3,300)

#  VISUALIZATION to see it in a graphical form
plt.figure(figsize=(12, 5))

# Subplot to see Actual vs Predicted
plt.subplot(1, 2, 1)
df['Predicted_Sales'] = np.dot(X, weights)
plt.plot(df['Day'], df['Actual_Sales'], 'ro-', label='Actual')
plt.plot(df['Day'], df['Predicted_Sales'], 'b--', label='Model Fit')
plt.title("Model Accuracy (Historical Fit)")
plt.legend()

# Subplot to check Impact Analysis
plt.subplot(1, 2, 2)
features = ['Bias', 'Season', 'Discount', 'Ad_Spend']
plt.bar(features[1:], weights[1:], color='teal')
plt.title("Feature Importance (Weight of Each Factor)")
plt.ylabel("Impact on Sales")

plt.tight_layout()
plt.show()

print(f". MODEL INSIGHTS .")
print(f"Predicted Sales for upcoming Big Sale Day: {future_weekend_sale:.2f} units")
print(f"Insight: A 1% increase in Discount adds approx {weights[2]/100:.2f} units to sales.")
