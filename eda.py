import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# LOAD CLEANED DATASET
# ==========================================

df = pd.read_excel("cleaned_dataset.xlsx")

# Ensure Date column is datetime format
df["Date"] = pd.to_datetime(df["Date"])

print("=" * 60)
print("E-COMMERCE SALES DATA ANALYSIS")
print("=" * 60)

# ==========================================
# STATISTICAL SUMMARY
# ==========================================

print("\n===== Statistical Summary =====")
print(df.describe())

print("\nAverage Quantity:", round(df["Quantity"].mean(), 2))
print("Median Quantity:", df["Quantity"].median())

print("\nAverage Unit Price:", round(df["UnitPrice"].mean(), 2))
print("Median Unit Price:", df["UnitPrice"].median())

print("\nAverage Total Price:", round(df["TotalPrice"].mean(), 2))
print("Median Total Price:", df["TotalPrice"].median())

# ==========================================
# PRODUCT ANALYSIS
# ==========================================

print("\n===== Top Products =====")
print(df["Product"].value_counts())

# ==========================================
# PAYMENT METHOD ANALYSIS
# ==========================================

print("\n===== Payment Methods =====")
print(df["PaymentMethod"].value_counts())

# ==========================================
# ORDER STATUS ANALYSIS
# ==========================================

print("\n===== Order Status =====")
print(df["OrderStatus"].value_counts())

# ==========================================
# REFERRAL SOURCE ANALYSIS
# ==========================================

print("\n===== Referral Sources =====")
print(df["ReferralSource"].value_counts())

# ==========================================
# REVENUE ANALYSIS
# ==========================================

print("\n===== Revenue Analysis =====")

print(
    "Total Revenue:",
    round(df["TotalPrice"].sum(), 2)
)

print(
    "Highest Order Value:",
    round(df["TotalPrice"].max(), 2)
)

print(
    "Lowest Order Value:",
    round(df["TotalPrice"].min(), 2)
)

# ==========================================
# MONTHLY SALES TREND
# ==========================================

df["Month"] = df["Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["TotalPrice"].sum()

print("\n===== Monthly Sales =====")
print(monthly_sales)

# ==========================================
# OUTLIER DETECTION (IQR METHOD)
# ==========================================

Q1 = df["TotalPrice"].quantile(0.25)
Q3 = df["TotalPrice"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - (1.5 * IQR)
upper = Q3 + (1.5 * IQR)

outliers = df[
    (df["TotalPrice"] < lower) |
    (df["TotalPrice"] > upper)
]

print("\nOutliers Found:", len(outliers))

# ==========================================
# VISUALIZATION 1
# PRODUCT ORDERS
# ==========================================

plt.figure(figsize=(8, 5))

df["Product"].value_counts().plot(kind="bar")

plt.title("Orders by Product")
plt.xlabel("Product")
plt.ylabel("Number of Orders")

plt.tight_layout()

plt.savefig(
    "graphs/product_orders.png",
    dpi=300
)

plt.show()

# ==========================================
# VISUALIZATION 2
# PAYMENT METHODS
# ==========================================

plt.figure(figsize=(6, 6))

df["PaymentMethod"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Payment Method Distribution")
plt.ylabel("")

plt.tight_layout()

plt.savefig(
    "graphs/payment_methods.png",
    dpi=300
)

plt.show()

# ==========================================
# VISUALIZATION 3
# MONTHLY REVENUE TREND
# ==========================================

plt.figure(figsize=(10, 5))

monthly_sales.plot(
    kind="line",
    marker="o",
    linewidth=2
)

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "graphs/monthly_revenue.png",
    dpi=300
)

plt.show()

# ==========================================
# VISUALIZATION 4
# REVENUE DISTRIBUTION
# ==========================================

plt.figure(figsize=(8, 5))

plt.hist(
    df["TotalPrice"],
    bins=20
)

plt.title("Revenue Distribution")
plt.xlabel("Total Price")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig(
    "graphs/revenue_distribution.png",
    dpi=300
)

plt.show()

# ==========================================
# COMPLETION MESSAGE
# ==========================================

print("\nAnalysis Completed Successfully!")
print("Charts saved inside the 'graphs' folder.")