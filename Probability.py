import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score



df = pd.read_excel("youtube_data.xlsx")

#region 1. Dataset
# print(df.head())
#endregion

#region 2. Data Analizi
# print(df.describe())
# print(df.corr())
#endregion

#region 3. Regression (Scikit-Learn)

X = df[["Likes", "Comments"]]
y = df["Views"]

model = LinearRegression()
model.fit(X, y)

print(model.coef_)
print(model.intercept_)
#endregion

#region 4. Gradient Descent

# X = np.array(df["Likes"])
# Y = np.array(df["Views"])

# m = 0
# b = 0

# L = 0.0001
# epochs = 1000

# n = len(X)

# errors = []

# for i in range(epochs):

#     Y_pred = m * X + b

#     error = np.mean((Y - Y_pred) ** 2)
#     errors.append(error)

#     D_m = (-2 / n) * sum(X * (Y - Y_pred))
#     D_b = (-2 / n) * sum(Y - Y_pred)

#     m = m - L * D_m
#     b = b - L * D_b

#     if i % 100 == 0:
#         print("Iteration:", i, "Error:", error)

# print("Final m =", m)
# print("Final b =", b)
#endregion

#region 5. Error Qrafiki

# plt.plot(errors)
# plt.title("Gradient Descent Error")
# plt.xlabel("Iteration")
# plt.ylabel("Error")
# plt.show()
#endregion


#region 6. Təxmin et

like = int(input("Like sayini daxil et: "))
comment = int(input("Comment sayini daxil et: "))

prediction = model.predict([[like, comment]])

print("Texmin edilen Views:", prediction[0])
#endregion

#region 7. Metriklər
pred = model.predict(X=df[["Likes", "Comments"]])

mae = mean_absolute_error(y, pred)
mse = mean_squared_error(y, pred)
r2 = r2_score(y, pred)

print("MAE:", mae)
print("MSE:", mse)
print("R2 Score:", r2)
#endregion