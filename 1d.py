import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import statsmodels.api as sm

# Read data
df_full = pd.read_csv("Trips_Full Data.csv")
df_full.dropna(inplace= True)
df = pd.read_csv("Trips_By_Distance.csv")
df.dropna(inplace= True)

# Select columns
x_col_full = 'Trips 1-25 Miles'  
x_col = 'Number of Trips 5-10'    
y_col = 'Number of Trips 10-25'   

# Extract values
x_full = df_full[x_col_full].values.reshape(-1, 1)
x = df[x_col].values.reshape(-1, 1)
y = df[y_col].values

# Split data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Linear Regression
model = LinearRegression()
model.fit(x_train, y_train)
r_sq = model.score(x_test, y_test)
print("Linear Regression:")
print("R^2:", r_sq)
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)
print()

# Polynomial Regression
poly = PolynomialFeatures(degree=2, include_bias=False)
x_poly = poly.fit_transform(x_train)
model_poly = LinearRegression()
model_poly.fit(x_poly, y_train)
r_sq_poly = model_poly.score(poly.transform(x_test), y_test)
print("Polynomial Regression:")
print("R^2:", r_sq_poly)
print("Intercept:", model_poly.intercept_)
print("Coefficients:", model_poly.coef_)
print()

# Advanced Linear Regression
x_sm = sm.add_constant(x_train)
model_sm = sm.OLS(y_train, x_sm)
results = model_sm.fit()
print("Advanced Linear Regression:")
print(results.summary()) 
