"""
Explore and compute all empirical values for Task 4
"""
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, r2_score, mean_absolute_error, mean_squared_error
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose

# 1. Load Data
df = pd.read_csv('data/ecommerce_transactions.csv')
print(f"Data shape: {df.shape}")

# Preprocessing
df['Transaction_Date'] = pd.to_datetime(df['Transaction_Date'])

# A. Descriptive Statistics
age_desc = {
    'mean': df['Age'].mean(),
    'median': df['Age'].median(),
    'mode': df['Age'].mode()[0],
    'std': df['Age'].std(),
    'min': df['Age'].min(),
    'max': df['Age'].max(),
    'skew': df['Age'].skew()
}

purchase_desc = {
    'mean': df['Purchase_Amount'].mean(),
    'median': df['Purchase_Amount'].median(),
    'mode': df['Purchase_Amount'].mode()[0],
    'std': df['Purchase_Amount'].std(),
    'min': df['Purchase_Amount'].min(),
    'max': df['Purchase_Amount'].max(),
    'skew': df['Purchase_Amount'].skew()
}
print("\n--- Descriptive Statistics ---")
print("Age:", age_desc)
print("Purchase Amount:", purchase_desc)

# B. Independent Samples T-Test (UPI vs COD)
upi_purchases = df[df['Payment_Method'] == 'UPI']['Purchase_Amount']
cod_purchases = df[df['Payment_Method'] == 'COD']['Purchase_Amount']

levene_stat, levene_p = stats.levene(upi_purchases, cod_purchases)
t_stat, t_p = stats.ttest_ind(upi_purchases, cod_purchases, equal_var=False) # Welch's t-test
t_stat_stud, t_p_stud = stats.ttest_ind(upi_purchases, cod_purchases, equal_var=True)

print("\n--- T-Test (UPI vs COD) ---")
print(f"UPI N={len(upi_purchases)}, Mean={upi_purchases.mean():.4f}, Std={upi_purchases.std():.4f}")
print(f"COD N={len(cod_purchases)}, Mean={cod_purchases.mean():.4f}, Std={cod_purchases.std():.4f}")
print(f"Levene test: stat={levene_stat:.4f}, p={levene_p:.4f}")
print(f"Welch's t-test: t={t_stat:.4f}, p={t_p:.4f}")
print(f"Student's t-test: t={t_stat_stud:.4f}, p={t_p_stud:.4f}")

# C. Chi-Square Test of Independence (Product_Category vs Payment_Method)
contingency_table = pd.crosstab(df['Product_Category'], df['Payment_Method'])
chi2_stat, chi2_p, dof, expected = stats.chi2_contingency(contingency_table)
print("\n--- Chi-Square Test ---")
print("Contingency Table shape:", contingency_table.shape)
print(f"Chi2 Stat={chi2_stat:.4f}, p-value={chi2_p:.4f}, dof={dof}")
print(f"Min expected frequency: {expected.min():.2f}")

# D. Confidence Intervals for Mean Purchase_Amount
mean_pa = df['Purchase_Amount'].mean()
std_pa = df['Purchase_Amount'].std()
n_pa = len(df['Purchase_Amount'])
sem_pa = stats.sem(df['Purchase_Amount'])
ci_95 = stats.t.interval(0.95, df=n_pa-1, loc=mean_pa, scale=sem_pa)
print("\n--- 95% Confidence Interval for Mean Purchase Amount ---")
print(f"Mean: {mean_pa:.4f}, SEM: {sem_pa:.4f}")
print(f"95% CI: [{ci_95[0]:.4f}, {ci_95[1]:.4f}]")

# 2. Time-Series Analysis
monthly_df = df.set_index('Transaction_Date').resample('ME').agg(
    total_revenue=('Purchase_Amount', 'sum'),
    transaction_count=('Transaction_ID', 'count'),
    average_purchase=('Purchase_Amount', 'mean')
)
print("\n--- Monthly Resampling ---")
print(f"Total months: {len(monthly_df)}")
print(monthly_df.head())
print(monthly_df.tail())

# Check full months vs partial month (March 2025 has only 8 days)
print("\nMarch 2025 transactions count and date range:")
m2025 = df[df['Transaction_Date'] >= '2025-03-01']
print(f"Count: {len(m2025)}, min date: {m2025['Transaction_Date'].min()}, max date: {m2025['Transaction_Date'].max()}")

# 3. Customer Segmentation (by User_Name)
user_agg = df.groupby('User_Name').agg(
    total_spend=('Purchase_Amount', 'sum'),
    transaction_count=('Transaction_ID', 'count'),
    average_purchase=('Purchase_Amount', 'mean'),
    average_age=('Age', 'mean')
).reset_index()

print("\n--- User Aggregation ---")
print(f"Number of distinct users: {len(user_agg)}")
print(user_agg.describe())

# Scaling features
features = ['total_spend', 'transaction_count', 'average_purchase', 'average_age']
scaler = StandardScaler()
scaled_features = scaler.fit_transform(user_agg[features])

# Elbow & Silhouette
inertias = []
silhouettes = []
k_range = range(2, 11)
for k in k_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = km.fit_predict(scaled_features)
    inertias.append(km.inertia_)
    silhouettes.append(silhouette_score(scaled_features, labels))

for k, inr, sil in zip(k_range, inertias, silhouettes):
    print(f"K={k}: Inertia={inr:.2f}, Silhouette={sil:.4f}")

# Fit optimal K (e.g. K=3 or K=4)
optimal_k = 3
km_opt = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
user_agg['cluster'] = km_opt.fit_predict(scaled_features)
print("\n--- Cluster Profile (K=3) ---")
profile = user_agg.groupby('cluster').agg(
    user_count=('User_Name', 'count'),
    avg_total_spend=('total_spend', 'mean'),
    avg_transaction_count=('transaction_count', 'mean'),
    avg_purchase_amount=('average_purchase', 'mean'),
    avg_age=('average_age', 'mean')
)
print(profile)

# Also check K=4
km_4 = KMeans(n_clusters=4, random_state=42, n_init=10)
user_agg['cluster_4'] = km_4.fit_predict(scaled_features)
print("\n--- Cluster Profile (K=4) ---")
profile_4 = user_agg.groupby('cluster_4').agg(
    user_count=('User_Name', 'count'),
    avg_total_spend=('total_spend', 'mean'),
    avg_transaction_count=('transaction_count', 'mean'),
    avg_purchase_amount=('average_purchase', 'mean'),
    avg_age=('average_age', 'mean')
)
print(profile_4)

# 4. Predictive Modeling: Linear Regression
X = df[['Age', 'Country', 'Product_Category', 'Payment_Method']]
y = df['Purchase_Amount']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

numeric_features = ['Age']
categorical_features = ['Country', 'Product_Category', 'Payment_Method']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore'), categorical_features)
    ]
)

pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("\n--- Linear Regression Performance ---")
print(f"R2 Score: {r2:.6f}")
print(f"MAE: {mae:.4f}")
print(f"RMSE: {rmse:.4f}")

# Feature Importance
ohe_names = pipeline.named_steps['preprocessor'].named_transformers_['cat'].get_feature_names_out(categorical_features)
feature_names = numeric_features + list(ohe_names)
coefficients = pipeline.named_steps['regressor'].coef_
intercept = pipeline.named_steps['regressor'].intercept_

feat_imp = pd.DataFrame({
    'Feature': feature_names,
    'Coefficient': coefficients,
    'Abs_Coefficient': np.abs(coefficients)
}).sort_values(by='Abs_Coefficient', ascending=False)

print("\n--- Top Features by Absolute Coefficient ---")
print(feat_imp.head(10))
print(f"Intercept: {intercept:.4f}")
