# =============================================================
# SECTION: STATISTICAL INFERENCE & MACHINE LEARNING
# Add this to your existing E-Commerce Sales Analysis notebook
# =============================================================

import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, classification_report

# -------------------------------------------------------------
# 1. FEATURE ENGINEERING (assumes df already loaded & cleaned)
# -------------------------------------------------------------
df['Profit_Margin'] = df['Profit'] / df['Sales']
df['Order Month'] = pd.to_datetime(df['Order Date']).dt.month
df['Is_Profitable'] = (df['Profit'] > 0).astype(int)
df['High_Discount'] = (df['Discount'] >= 0.20).astype(int)

# -------------------------------------------------------------
# 2. HYPOTHESIS TESTING
# Question: Do high-discount orders (>=20%) have significantly
# lower profit than low-discount orders?
# -------------------------------------------------------------
high_discount_profit = df[df['High_Discount'] == 1]['Profit']
low_discount_profit  = df[df['High_Discount'] == 0]['Profit']

t_stat, p_value = stats.ttest_ind(high_discount_profit, low_discount_profit, equal_var=False)

print("=== Hypothesis Test: Discount vs Profit ===")
print(f"Mean profit (high discount): ${high_discount_profit.mean():.2f}")
print(f"Mean profit (low discount):  ${low_discount_profit.mean():.2f}")
print(f"T-statistic: {t_stat:.3f}")
print(f"P-value: {p_value:.5f}")

if p_value < 0.05:
    print("Result: Statistically significant difference (p < 0.05).")
    print("Conclusion: High discounting is a measurable driver of profit loss, not random noise.")
else:
    print("Result: No statistically significant difference.")

# -------------------------------------------------------------
# 3. CORRELATION ANALYSIS
# -------------------------------------------------------------
corr_cols = ['Sales', 'Profit', 'Discount', 'Quantity']
corr_matrix = df[corr_cols].corr()

print("\n=== Correlation Matrix ===")
print(corr_matrix.round(2))

plt.figure(figsize=(6, 4))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, fmt=".2f")
plt.title("Correlation Heatmap: Sales, Profit, Discount, Quantity")
plt.tight_layout()
plt.show()

# -------------------------------------------------------------
# 4. CONFIDENCE INTERVAL ON CATEGORY PROFIT MARGIN
# -------------------------------------------------------------
print("\n=== 95% Confidence Intervals on Profit Margin by Category ===")
for category in df['Category'].unique():
    sample = df[df['Category'] == category]['Profit_Margin'].dropna()
    mean = sample.mean()
    sem = stats.sem(sample)
    ci = stats.t.interval(0.95, len(sample) - 1, loc=mean, scale=sem)
    print(f"{category:12s} mean margin = {mean:.3f}, 95% CI = ({ci[0]:.3f}, {ci[1]:.3f})")

# -------------------------------------------------------------
# 5. MACHINE LEARNING: PREDICT ORDER PROFITABILITY
# Logistic Regression Classification
# -------------------------------------------------------------
features = ['Sales', 'Quantity', 'Discount', 'Order Month']
categorical_features = ['Category', 'Segment', 'Region']

ml_df = df[features + categorical_features + ['Is_Profitable']].dropna()

# Encode categorical variables
le_dict = {}
for col in categorical_features:
    le = LabelEncoder()
    ml_df[col] = le.fit_transform(ml_df[col])
    le_dict[col] = le

X = ml_df[features + categorical_features]
y = ml_df['Is_Profitable']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

print("\n=== Model Performance: Profitability Prediction ===")
print(f"Accuracy:  {accuracy_score(y_test, y_pred):.3f}")
print(f"Precision: {precision_score(y_test, y_pred):.3f}")
print(f"Recall:    {recall_score(y_test, y_pred):.3f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Loss', 'Profit'], yticklabels=['Loss', 'Profit'])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix: Order Profitability")
plt.tight_layout()
plt.show()

# -------------------------------------------------------------
# 6. FEATURE IMPORTANCE (Logistic Regression Coefficients)
# -------------------------------------------------------------
coef_df = pd.DataFrame({
    'Feature': features + categorical_features,
    'Coefficient': model.coef_[0]
}).sort_values('Coefficient')

print("\n=== Feature Influence on Profitability ===")
print(coef_df)
print("\nNegative coefficient = increases risk of loss")
print("Positive coefficient = increases likelihood of profit")

plt.figure(figsize=(7, 4))
sns.barplot(data=coef_df, x='Coefficient', y='Feature', palette='coolwarm')
plt.title("Feature Impact on Order Profitability")
plt.axvline(0, color='black', linewidth=0.8)
plt.tight_layout()
plt.show()
