import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
df = pd.read_excel("car_sales_1000.xlsx")


#region 1. Dataset oxuma ve ilkin analiz
# print(df.head())
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())

# for col in df.columns:
#     print(f"{col}: {df[col].dtype} - {'Kategoriyal' if df[col].dtype == 'object' else 'Raqemsal'}")

#endregion

#region 2. Preprocessing 

# num_cols = ['ModelYear', 'EngineSize_L', 'Mileage_km', 'Seats']
# cat_cols = ['Brand', 'FuelType', 'Transmission']

# numeric_transformer = Pipeline(steps=[
#     ('imputer', SimpleImputer(strategy='median')),
#     ('scaler', StandardScaler())
# ])

# categorical_transformer = Pipeline(steps=[
#     ('imputer', SimpleImputer(strategy='most_frequent')),
#     ('encoder', OneHotEncoder(handle_unknown='ignore'))
# ])

# preprocessor = ColumnTransformer(transformers=[
#     ('num', numeric_transformer, num_cols),
#     ('cat', categorical_transformer, cat_cols)
# ])

#endregion 

#region 3. Multi-variable regression model
# X = df.drop('Price_AZN', axis=1)
# y = df['Price_AZN']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model = Pipeline(steps=[
#     ('preprocessor', preprocessor),
#     ('regressor', LinearRegression())
# ])

# model.fit(X_train, y_train)

# print(f"X_train shape: {X_train.shape}")
# print(f"X_test shape: {X_test.shape}")
#endregion

#region 4. Modeli oyret ve netice cixart
# pred = model.predict(X_test)

# mae = mean_absolute_error(y_test, pred)
# mse = mean_squared_error(y_test, pred)
# r2 = r2_score(y_test, pred)

# print(f"MAE: {mae} AZN")
# print(f"MSE: {mse}")
# print(f"R²: {r2}")

#endregion

#region 5. Feature Importance analizi
# encoder = model.named_steps['preprocessor'].named_transformers_['cat'].named_steps['encoder']
# encoded_features = encoder.get_feature_names_out(cat_cols)
# feature_names = num_cols + list(encoded_features)

# coefficients = model.named_steps['regressor'].coef_
# importance = pd.Series(coefficients, index=feature_names).sort_values(ascending=False)

# print(importance.head(10))

#endregion

#region 6. Mini Console Tətbiqi
# brand = input("Marka (Toyota, BMW, Kia...): ")
# year = int(input("Buraxılış ili: "))
# engine = float(input("Mühərrik həcmi (L): "))
# fuel = input("Yanacaq növü (Petrol, Diesel, Hybrid, Electric): ")
# trans = input("Transmissiya (Automatic, Manual): ")
# mileage = int(input("Yürüş (km): "))
# seats = int(input("Oturacaq sayı: "))

# new_data = pd.DataFrame({
#     'Brand': [brand],
#     'ModelYear': [year],
#     'EngineSize_L': [engine],
#     'FuelType': [fuel],
#     'Transmission': [trans],
#     'Mileage_km': [mileage],
#     'Seats': [seats]
# })

# pred_price = model.predict(new_data)[0]
# print(f"Texmin edilen satis qiymeti: {pred_price} AZN")

#endregion

#region 7. Mini Report sualları:
# print("""1. Hansi faktor qiymete en cox tesir edir?
#    En cox tesir eden faktorlar marka (Brand), muherrik olcusu (EngineSize_L)
#    ve yurusdur (Mileage_km). Xususile BMW, Toyota kimi markalar ve boyuk
#    muherrikli masinlar daha bahali qiymetlendirilir.

# 2. Muherrik olcusu ve yurus arasinda elaqe varmi?
#    Birbasa elaqe yoxdur, lakin her ikisi qiymete ters istiqametde tesir edir:
#    muherrik boyukle dusa qiymet artir, yurus artdiqca qiymet azalir.

# 3. R² neticesi modelin keyfiyyetini nece gosterir?
#    R² ne qeder 1-e yaxindirsa, model bir o qeder yaxsidir. 0.7+ yaxsi,
#    0.9+ ela model sayilir. Bu modelde elde olunan R² real bazar
#    melumatlarinda qenaetbexsdir.

# 4. Hansi preprocessing addimi en vacib idi ve niye?
#    OneHotEncoder en vacib addimdir, cunki kateqoriya sutunlari (Brand,
#    FuelType) reqemsal formata cevrilmese, Linear Regression onlari
#    isleye bilmez. SimpleImputer da vacibdir, cunki bos deyerler
#    modelin xetasini artirar.

# 5. Bu modeli gelecekde nece inkisaf etdirmek olar?
#    - Random Forest ve ya XGBoost kimi daha murekkeb modeller sinamaq
#    - Feature engineering (masinin yasi, yeni/passat kimi yeni deyiskenler)
#    - Hiperparametr optimizasiyasi (GridSearchCV)
#    - Cross-validation ile modelin dayanigliligini yoxlamaq
#    - Daha cox ve daha keyfiyyetli melumat toplamaq
# """)
#endregion
