# Data Analytics Projects

A collection of data analytics projects focused on data cleaning, exploratory data analysis (EDA), data visualization, and business intelligence reporting.

---

## E-Commerce Data Cleaning & Sales Analytics Dashboard

### Project Overview

This project demonstrates the complete data analytics workflow, from cleaning raw data to building an interactive Power BI dashboard.

The objective was to transform a raw e-commerce dataset into a clean, reliable, and analysis-ready dataset while generating meaningful business insights through visualization and reporting.

---

## Project Workflow

Raw Dataset
⬇
Data Cleaning & Validation
⬇
Exploratory Data Analysis (EDA)
⬇
Data Visualization
⬇
Power BI Dashboard
⬇
Business Insights

---

## Dataset Information

The dataset contains e-commerce transaction records including:

* Order ID
* Customer Information
* Product Details
* Quantity Purchased
* Unit Price
* Payment Method
* Order Status
* Marketing Channel
* Revenue Information

**Dataset Size**

* Records: 1,200
* Columns: 14

---

## Data Cleaning Tasks

### Missing Value Handling

* Identified missing values across all columns.
* Replaced missing values in `CouponCode` with `"No Coupon"`.

### Duplicate Detection

* Checked duplicate rows.
* Verified duplicate Order IDs.
* Verified duplicate Tracking Numbers.

### Data Validation

Validated business rules:

* Quantity > 0
* UnitPrice > 0
* TotalPrice > 0
* ItemsInCart > 0

### Data Consistency Checks

Verified:

```python
TotalPrice = Quantity * UnitPrice
```

and corrected inconsistencies where required.

---

## Exploratory Data Analysis (EDA)

Performed analysis on:

* Revenue Distribution
* Monthly Revenue Trends
* Product Performance
* Payment Method Distribution
* Customer Behavior
* Marketing Channel Performance

---

## Power BI Dashboard

The cleaned dataset was imported into Power BI to create an interactive sales analytics dashboard.

### Dashboard Highlights

#### KPI Metrics

* Total Revenue
* Total Orders
* Total Customers
* Average Order Value
* Quantity Sold
* Revenue per Customer

#### Visualizations

* Monthly Revenue Trend Analysis
* Top Products by Revenue
* Revenue by Marketing Channel
* Revenue by Payment Method
* Interactive Filters for Order Status
* Interactive Filters for Payment Method

### Skills Demonstrated

* Power BI Dashboard Development
* Data Cleaning & Data Modeling
* DAX Measures & Calculations
* KPI Design and Business Metrics
* Interactive Slicers and Filters
* Data Visualization Best Practices
* Business Intelligence Reporting
* Dashboard Layout & Design

---

## Technologies Used

* Python
* Pandas
* Microsoft Excel
* Power BI
* Visual Studio Code

---

## Repository Structure

```text
Data-Analytics-Projects
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── ECommerce_Data_Cleaning
│   ├── raw_dataset.xlsx
│   ├── cleaned_dataset.xlsx
│   ├── data_cleaning.py
│   ├── exploratory_data_analysis.py
│   ├── dashboard_visualizations.py
│   ├── Data_Cleaning_Report.docx
│   │
│   ├── PowerBI_Dashboard
│   │   ├── ECommerce_Sales_Dashboard.pbix
│   │   └── ECommerce_Sales_Dashboard.jpg
│   │
│   └── Visualizations
│       ├── monthly_revenue_trend.png
│       ├── payment_method_distribution.png
│       ├── product_sales_analysis.png
│       ├── revenue_distribution.png
│       └── dashboard_preview.png
```

---

## Key Skills

* Data Cleaning
* Data Validation
* Data Transformation
* Exploratory Data Analysis (EDA)
* Data Visualization
* Business Intelligence
* Dashboard Development
* KPI Reporting
* Power BI
* Python Programming

---

## Author

**Anjali Neelam**

Data Analytics Enthusiast | Python | Power BI | Data Visualization
