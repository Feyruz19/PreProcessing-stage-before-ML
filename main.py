# import pandas as pd
# import numpy as np
# from scipy.stats import zscore

# df = pd.read_csv("Preview__houses_day1__first_20_rows_.csv")


# #region 1. Sürətli baxış
# # print(df.head(5))
# # print(df.tail(5))
# # print(df.sample(3))

# # #Sual: Səncə hansı 3 sətir “maraqlı” görünür və niyə? -> Floor/Rooms/Price_AZN
# #endregion

# #region 2. Struktur yoxlaması
# # print("\nINFO")
# # df.info()

# # print("\nBoş dəyərlər:")
# # print(df.isnull().sum())

# # print("\nDtypes:")
# # print(df.dtypes)
# #endregion

# #region 3. Statistik icmal
# # print(df[["Area_m2", "Price_AZN"]].describe())

# # print("Area mean:", df["Area_m2"].mean())
# # print("Area median:", df["Area_m2"].median())
# # print("Area std:", df["Area_m2"].std())

# # print("Price mean:", pd.to_numeric(df["Price_AZN"], errors="coerce").mean())
# # print("Price median:", pd.to_numeric(df["Price_AZN"], errors="coerce").median())
# # print("Price std:", pd.to_numeric(df["Price_AZN"], errors="coerce").std())

# #endregion

# #region 4. Tip düzəlişi
# # print("Evvel:")
# # print(df["Price_AZN"].dtype)

# # df["Price_AZN"] = pd.to_numeric(df["Price_AZN"], errors="coerce")

# # print("Sonra:")
# # print(df["Price_AZN"].dtype)
# #endregion

# #region 5. Qiymət outlier-ləri
# # print(df.sort_values("Price_AZN", ascending=False).head(10))
# #Yuxaridaki boyuk qiymetler outlier a tesir edir
# #endregion

# #region 6. Kateqorik balans
# # print(df["District"].value_counts())
# #Chox temsil olunan Nasimi / az temsil olunan Khatai. Imbalance esasen cox temsil olunan rayonlara yonele biler.
# #endregion

# #region 7. Rooms distribusiyası
# # print(df["Rooms"].value_counts().sort_index())
# #Paylanmada esas en cox 2 otaqlidi sonra 3 otaqli sonra 1 otaqli
# #endregion

# #region 8. Mean vs Median Price
# # print("Mean:", df["Price_AZN"].mean())
# # print("Median:", df["Price_AZN"].median())
# #Mean median dan cox yuksek oldugu ucun yuksek qiymetler outlier a tesir edir
# #endregion

# #region 9. Mode və yayılma ölçüləri
# # print("Rooms mode:", df["Rooms"].mode())

# # print("Price variance:", df["Price_AZN"].var())
# # print("Price std:", df["Price_AZN"].std())

# #endregion

# #region 10. Filter + seçim
# # subset = df[(df["Rooms"] >= 3) & (df["Area_m2"] >= 100)]
# # print(subset)
# # print("Orta qiymet:", subset["Price_AZN"].mean())
# #endregion

# #region 11. District üzrə mərkəz ölçüləri
# # district_stats = df.groupby("District")["Price_AZN"].agg(["mean", "median", "count"])
# # print(district_stats)
# #en chox ferq sebail dedir
# #endregion

# #region 14. Top 10 ən bahalı və ən ucuz evlər
# # print("Ən bahalı 10:")
# # print(df.sort_values("Price_AZN", ascending=False).head(10))

# # print("Ən ucuz 10:")
# # print(df.sort_values("Price_AZN", ascending=True).head(10))
# #endregion

# #region 15. Room effect
# # print(df.groupby("Rooms")["Price_AZN"].median())
# #cunki median outlierden mean qeder tesirlenmir
# #endregion

# #region 16. Price per m2
# # df["ppm"] = df["Price_AZN"] / df["Area_m2"]
# # print(df.sort_values("ppm", ascending=False).head(10))
# #Sebayil
# #endregion

# #region 17. District map
# # region_map = {
# #     "Sabayil": "Prime",
# #     "Yasamal": "Central",
# #     "Nizami": "Central",
# #     "Nasimi": "Central",
# #     "Nerimanov": "Central",
# #     "Khatai": "Outer",
# #     "Binagadi": "Outer"
# # }

# # df["region"] = df["District"].map(region_map)

# # print(df.groupby("region")["Price_AZN"].median())
# #endregion

# #region 18. Boş qiymətlər
# # missing_price = df[df["Price_AZN"].isnull()]
# # print(missing_price)
# # print(missing_price[["District", "Rooms", "Area_m2"]])
# #median mean e nisbeten daha az tesirlenir outlierdan
# #endregion

# #region 20. Mini-profil hesabatı
# print("Shape:")
# print(df.shape)

# print("Nulls per column:")
# print(df.isnull().sum())

# print("Numeric describe:")
# print(df.describe())

# print("District count:")
# print(df["District"].value_counts())

# print("Mean Price:", df["Price_AZN"].mean())
# print("Median Price:", df["Price_AZN"].median())

# print("Top ppm 5 rows:")
# print(df.sort_values("ppm", ascending=False).head(5))
# #endregion