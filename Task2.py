# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# students = pd.read_excel("students_performance.xlsx")


# #region 1. Sürətli baxış
# # print(students.head(5))
# # print(students.tail(5))
# # print(students.sample(3))

# #Department maraqli gorunur
# #endregion 

# #region 2. Struktur yoxlaması
# # print(students.info())
# # print(students.isnull().sum())
# # print(students.dtypes)


# #Ededi: 'StudentID', 'Age', 'GPA', 'MathScore', 'ReadingScore', 'WritingScore','AttendanceRate'
# #Kategorik: 'Gender', 'Department'
# #Boolean: 'HasScholarship'


# #endregion

# #region 3. Statistik icmal
# # print(students.describe())

# # print("GPA mean:", students["GPA"].mean())
# # print("GPA median:", students["GPA"].median())
# # print("GPA std:", students["GPA"].std())

# # print("MathScore mean:", students["MathScore"].mean())
# # print("MathScore median:", students["MathScore"].median())
# # print("MathScore std:", students["MathScore"].std())

# #endregion

# #region 4. Tip düzəlişi

# # students["HasScholarship"] = students["HasScholarship"].astype(bool)
# # students["AttendanceRate"] = pd.to_numeric(students["AttendanceRate"], errors="coerce")

# #endregion

# #region 5. Boş Dəyərləri Analiz Et

# # print(students.isnull().sum())
# # students["GPA"] = students["GPA"].fillna(students["GPA"].median())
# # students["Department"] = students["Department"].fillna(students["Department"].mode()[0])

# #endregion

# #region 6. Departament Üzrə Tələbə Sayı

# # print(students["Department"].value_counts())

# #endregion

# #region 7. Mean vs Median: MathScore

# # print(students["MathScore"].mean())
# # print(students["MathScore"].median())

# #endregion

# #region 8. Scholarship Təsiri

# # print(students[students["HasScholarship"] == True]["GPA"].median())
# # print(students[students["HasScholarship"] == False]["GPA"].median())

# #endregion

# #region 9. Korelyasiya

# # corr_cols = ["GPA", "MathScore", "ReadingScore", "WritingScore", "AttendanceRate"]

# # corr_matrix = students[corr_cols].corr()
# # print(corr_matrix)

# # sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
# # plt.title("Correlation Matrix")
# # plt.show()

# #endregion

# #region 10. Outlier: IQR Metodu

# # q1 = students["MathScore"].quantile(0.25)
# # q3 = students["MathScore"].quantile(0.75)

# # iqr = q3 - q1

# # lower_band = q1 - 1.5 * iqr
# # upper_band = q3 + 1.5 * iqr


# # outliers = students[
# #     (students["MathScore"] < lower_band) |
# #     (students["MathScore"] > upper_band)
# # ]

# # print(outliers)

# #endregion

# #region 11. Outlier: Z-Score Metodu

# # students["MathScore_z"] = (
# #     students["MathScore"] - students["MathScore"].mean()) / students["MathScore"].std()

# # students["GPA_z"] = (
# #     students["GPA"] - students["GPA"].mean()) / students["GPA"].std()

# #endregion

# #region 12. Departament Üzrə GPA Müqayisəsi

# # print(students.groupby("Department")["GPA"].agg(["mean", "median", "count"]))

# #endregion

# #region 13. Gender Fərqləri

# #print(students.groupby("Gender")[["GPA", "MathScore"]].median())

# #endregion

# #region 14. Vizual Analiz

# #Histogram 
# # plt.hist(students["GPA"], bins=20)
# # plt.title("GPA Distribution")
# # plt.xlabel("GPA")
# # plt.ylabel("Count")
# # plt.show()

# # plt.hist(students["MathScore"], bins=20)
# # plt.title("MathScore Distribution")
# # plt.xlabel("MathScore")
# # plt.ylabel("Count")
# # plt.show()
# ###############################################3
# #Boxplot
# # sns.boxplot(data=students, x="Department", y="GPA")
# # plt.title("GPA by Department")
# # plt.xticks(rotation=45)
# # plt.show()
# #####################################################
# #scatterplot
# # sns.scatterplot(
# #     data=students,
# #     x="AttendanceRate",
# #     y="GPA",
# #     hue="HasScholarship"
# # )

# # plt.title("AttendanceRate vs GPA")
# # plt.show()

# #endregion

# #region 15. Mini Nəticə Hesabatı
# #bu task Ai ile yazildi....
# # print("""Dataset 120 setir ve 10 sutundan ibaretdir. Sutunlar StudentID, Gender, Age, Department, GPA, MathScore, ReadingScore, WritingScore, AttendanceRate ve HasScholarship-dir.

# # Datasetde Department sutununda 1, GPA sutununda 2, MathScore sutununda 1 ve AttendanceRate sutununda 1 bos deyer var. GPA bos deyerleri median ile, Department bos deyeri ise en cox rast gelinen deyerle doldurula biler.

# # GPA ucun mean 3.008, median 3.000, std 0.401-dir. Mean ve median bir-birine cox yaxin oldugu ucun GPA paylanmasi texminen simmetrikdir.

# # MathScore ucun mean 68.765, median 71.000, std 12.925-dir. Median mean-den bir az yuksekdir, bu da asagi neticelerin ortalamani bir az asagi cekdiyini gosterir.

# # IQR metoduna gore MathScore ucun Q1 59, Q3 77, IQR 18-dir. Lower band 32, upper band 104 alindi. Datasetde MathScore uzre outlier yoxdur. Z-score metodunda da |z| > 3 olan deyer tapilmadi.

# # Korelyasiya neticelerine gore GPA ile en guclu elaqe AttendanceRate arasindadir: 0.687. GPA ile WritingScore arasinda 0.660, GPA ile MathScore arasinda ise 0.647 elaqe var. En guclu umumi elaqe MathScore ve WritingScore arasindadir: 0.720.

# # Department uzre en yuksek GPA ortalamasi Economics fakultesindedir: 3.137. En asagi GPA ortalamasi Biology fakultesindedir: 2.917. IT fakultesinde en cox telebe var: 34 telebe.

# # Teqaud alan telebelerin GPA ortalamasi 3.115, teqaud almayanlarin GPA ortalamasi ise 2.981-dir. Teqaud alanlarin neticesi bir az yuksekdir, amma bu, teqaudun birbasa sebeb oldugunu subut etmir.

# # Netice olaraq, telebe performansina en cox tesir eden amiller AttendanceRate, WritingScore ve MathScore kimi gorunur. Xususile derse davamiyyet GPA ile daha guclu elaqeye malikdir.""")

# #endregion











