import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Load cleaned dataset
df = pd.read_excel("cleaned_dataset.xlsx")

# Ensure Date column is datetime format
df["Date"] = pd.to_datetime(df["Date"])

# ---------------- KPI CALCULATIONS ----------------

total_revenue = df["TotalPrice"].sum()
total_orders = len(df)
avg_order = df["TotalPrice"].mean()
top_product = df["Product"].value_counts().idxmax()

# ---------------- MONTHLY SALES ----------------

df["Month"] = df["Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["TotalPrice"].sum()

# ---------------- PRODUCT SALES ----------------

product_counts = df["Product"].value_counts()

# ---------------- PAYMENT METHODS ----------------

payment_counts = df["PaymentMethod"].value_counts()

# ---------------- DASHBOARD DESIGN ----------------

plt.style.use("dark_background")

fig = plt.figure(figsize=(18, 10))

gs = GridSpec(
    6,
    12,
    figure=fig
)

fig.suptitle(
    "E-Commerce Analytics Dashboard",
    fontsize=26,
    fontweight="bold",
    y=0.98
)

# ==================================================
# KPI CARDS
# ==================================================

card1 = fig.add_subplot(gs[0:2, 0:3])
card2 = fig.add_subplot(gs[0:2, 3:6])
card3 = fig.add_subplot(gs[0:2, 6:9])
card4 = fig.add_subplot(gs[0:2, 9:12])

cards = [card1, card2, card3, card4]

for card in cards:
    card.set_xticks([])
    card.set_yticks([])
    card.set_frame_on(False)
    card.set_facecolor("#1f2937")

# Total Revenue Card
card1.text(
    0.5, 0.65,
    "Total Revenue",
    ha="center",
    fontsize=14
)

card1.text(
    0.5, 0.35,
    f"₹{total_revenue:,.0f}",
    ha="center",
    fontsize=24,
    fontweight="bold"
)

# Total Orders Card
card2.text(
    0.5, 0.65,
    "Total Orders",
    ha="center",
    fontsize=14
)

card2.text(
    0.5, 0.35,
    f"{total_orders}",
    ha="center",
    fontsize=24,
    fontweight="bold"
)

# Average Order Value Card
card3.text(
    0.5, 0.65,
    "Avg Order Value",
    ha="center",
    fontsize=14
)

card3.text(
    0.5, 0.35,
    f"₹{avg_order:.0f}",
    ha="center",
    fontsize=24,
    fontweight="bold"
)

# Top Product Card
card4.text(
    0.5, 0.65,
    "Top Product",
    ha="center",
    fontsize=14
)

card4.text(
    0.5, 0.35,
    top_product,
    ha="center",
    fontsize=24,
    fontweight="bold"
)

# ==================================================
# MONTHLY REVENUE TREND
# ==================================================

ax1 = fig.add_subplot(gs[2:6, 0:7])

monthly_sales.plot(
    ax=ax1,
    marker="o",
    linewidth=3
)

ax1.set_title(
    "Monthly Revenue Trend",
    fontsize=16,
    pad=15
)

ax1.set_xlabel("Month")
ax1.set_ylabel("Revenue")

ax1.grid(True, alpha=0.3)

# ==================================================
# PRODUCT SALES
# ==================================================

ax2 = fig.add_subplot(gs[2:4, 7:12])

product_counts.sort_values().plot(
    kind="barh",
    ax=ax2
)

ax2.set_title(
    "Orders by Product",
    fontsize=16
)

ax2.set_xlabel("Orders")

# ==================================================
# PAYMENT METHOD DISTRIBUTION
# ==================================================

ax3 = fig.add_subplot(gs[4:6, 7:12])

ax3.pie(
    payment_counts,
    labels=payment_counts.index,
    autopct="%1.1f%%",
    wedgeprops=dict(width=0.4)
)

ax3.set_title(
    "Payment Method Distribution",
    fontsize=16
)

# ==================================================
# SAVE DASHBOARD
# ==================================================

plt.tight_layout()

plt.savefig(
    "graphs/pro_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()