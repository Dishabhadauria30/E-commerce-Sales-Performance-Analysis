<div align="center">

<!-- HEADER BANNER -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:667eea,100:764ba2&height=200&section=header&text=E-Commerce%20Sales%20Intelligence&fontSize=36&fontColor=ffffff&fontAlignY=38&desc=Turning%209%2C994%20Transactions%20Into%20₹1.2M%20Worth%20of%20Insight&descAlignY=58&descSize=16" width="100%"/>

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Viz-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org)
[![Status](https://img.shields.io/badge/Status-Complete-28a745?style=for-the-badge)](.)

<br/>

> **"Data without insight is just noise. Insight without action is just trivia."**  
> This project delivers both — and quantifies a $1.2M profit recovery opportunity.

</div>

---

##  The Business Problem

A US-based e-commerce company was generating **$19.3M in revenue** but walking away with only **$686K in profit** — a razor-thin **3.6% margin**. The question was: *where is the money going, and how do we get it back?*

This analysis digs into **9,994 transactions across 2020–2023** to answer exactly that.

---

##  Top 5 Findings (The Punchy Version)

|  Finding | Impact |
|---------|--------|
|  **Furniture loses $498K/year** despite $4.55M in sales | Biggest profit leak in the business |
|  **50.6% of orders carry ≥20% discounts** | Responsible for $700K in lost profit |
|  **Copiers alone generate $1.19M profit** | Single highest-margin product |
|  **monthly profit analysis generates 77% more revenue than monthly sales analysis** | Massive seasonal opportunity untapped |
|  **Corporate customers are 24% more profitable** than Consumer per dollar of sales | Segment strategy is misaligned |

---

## Project Architecture

```
📁 E-Commerce Sales Intelligence
│
├──  Data Preprocessing
│   ├── Null value check (0 missing values found)
│   ├── Duplicate detection
│   ├── Date parsing & feature engineering
│   └── Derived columns: Order Month, Year, Day of Week
│
├──  Sales Analysis (4 dimensions)
│   ├── Monthly Sales Trend
│   ├── Sales by Category
│   ├── Sales by Sub-Category
│   └── Customer Segment Sales
│
├──  Profit Analysis (4 dimensions)
│   ├── Monthly Profit Trend
│   ├── Profit by Category
│   ├── Profit by Sub-Category
│   └── Sales-to-Profit Ratio by Segment
│
└──  Business Recommendations (6 action items)
```

---

##  Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| **Python** | 3.10+ | Core programming language |
| **Pandas** | 2.x | Data manipulation, groupby aggregations, feature engineering |
| **Plotly Express** | 5.x | Interactive line, bar, pie/donut charts |
| **Plotly Graph Objects** | 5.x | Multi-trace grouped bar charts |
| **Jupyter Notebook** | Latest | Development & storytelling environment |

>  **Why Plotly over Matplotlib?** Plotly charts are interactive you can hover, zoom, and filter directly in the notebook. This makes exploratory analysis faster and presentations more compelling.

---

## The Statistics Behind the Story

Here's a quick stats explainer for the key numbers no jargon, just intuition:

### 📌 What is a "Profit Margin"?
> If you sell a chair for $100 and it costs you $95 to source, ship, and discount you keep $5. That's a 5% margin.  
> This business's overall margin is **3.6%** meaning for every $100 earned, only $3.60 is kept. That's dangerously thin.

### 📌 What does "Sales-to-Profit Ratio" mean?
> Corporate customers need **$25.5 in sales** to generate $1 in profit.  
> Consumer customers need **$31.5 in sales** for the same $1.  
> **Lower = better.** The 24% gap is statistically meaningful and drives the "focus on Corporate" recommendation.

### 📌 Why does Furniture look successful but isn't?
> Furniture has $4.55M in sales (looks great!) but $498K in profit (disaster).  
> This disconnect  high revenue, negative profit  is a classic case of **margin erosion through discounting.**  
> Statistical signal: Tables alone show $2.23M in sales with $305K profit. Every table sold *costs* the business money.

### 📌 Seasonal Pattern (October–December spike)
> Profit analysis revenue: $6.18M vs monthly sales analysis revenue: $3.50M  
> That's a **77% increase** a statistically strong seasonal effect.  
> In data terms, this is called **time-series seasonality** It repeats predictably year over year, making it plannable.

---

## A Pinch of Machine Learning (Plain English)

Here's what ML could add:

###  Predict Which Orders Will Be Profitable
> **Algorithm: Logistic Regression / Decision Tree**  
> Train a model on: discount %, category, segment, order month → predict if an order will be profitable or loss-making *before it ships.*  
> **Business value:** Sales reps get a real-time "profit risk score" when creating a deal.

### Forecast monthly profit analysis Inventory Needs
> **Algorithm: Time Series Forecasting (Prophet / Moving Average)**  
> Use 4 years of monthly sales data to predict next October–December demand per sub-category.  
> **Business value:** No stockouts on Copiers (your profit engine). No overstock on Tables (your loss-maker).

### Customer Clustering
**Algorithm: K-Means Clustering**  
Group customers by: purchase frequency, average order size, discount sensitivity → discover hidden customer personas beyond the 3 official segments.  
**Business value:** Hyper-targeted promotions instead of one-size-fits-all discounting.

---

##  6 Business Recommendations

```

1: Cap discounts at 15%                  
  Impact: Recover up to $700K in annual profit               
  Difficulty: Low (policy change)                            
---
2: Furniture Pricing Review important     
  Impact: Recover $498K annually                             
  Difficulty: Medium (supplier negotiation / price hike)     
---
3: Double down on Copiers                
  Impact: Scale $1.19M profit engine further                 
  Difficulty: Low (marketing & inventory investment)         
---
4: profit analysis Demand Planning                    
  Impact: Avoid stockouts during 77% revenue surge           
  Difficulty: Medium (supply chain coordination)             
---
5: Grow Corporate Segment                
  Impact: Shift mix toward 24% more profitable customers     
  Difficulty: Medium (B2B sales strategy)                   
---
6: Geo-focus on CA, NY, TX               
  Impact: These 3 states = 37% of revenue                    
 Difficulty: Low (regional marketing campaigns)             
```

---

## 📁 Dataset

 **Source** : Sample Superstore (Kaggle) 
 **Records** : 9,994 transactions 
 **Time Period** :  2020 – 2023 
 **Geography** : United States 
 **Features** : Order Date, Ship Date, Category, Sub-Category, Sales, Profit, Discount, Segment, Region, State 

---

## How to Run

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/ecommerce-sales-analysis.git
cd ecommerce-sales-analysis

# 2. Install dependencies
pip install pandas plotly jupyter

# 3. Add the dataset
# Place "Sample - Superstore.csv" in the root folder

# 4. Launch the notebook
jupyter notebook "_E_Commerce_project_1_ (2).ipynb"
```

---

##  Analysis 


 Data Cleaning & Integrity : Zero missing values, duplicate check, proper dtype conversion 
 Analytical Depth : 8+ analysis dimensions, multi-level groupby 
 Visualisation Quality : Interactive Plotly charts, donut, line, bar, grouped bar 
 Business Storytelling : Each chart is tied to a business question + actionable insight 
 Code Quality : Clean & readable; could add functions/classes for scale 
 Statistical Reasoning : Margins, ratios, comparisons — room to add hypothesis testing 
 Recommendations : 6 specific, quantified, prioritised action items 


---

## 👩‍💻 About the Author

**Disha Bhadauria**  
Aspiring Data Analyst | Python · Pandas · Plotly · SQL · EDA

📌 *Skills demonstrated in this project:*
- ✅ End-to-end data analysis pipeline
- ✅ Feature engineering from raw datetime fields
- ✅ Business-framed insight communication
- ✅ Multi-dimensional profitability analysis
- ✅ Interactive data visualisation
- ✅ Translating numbers into executive recommendations

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:764ba2,100:667eea&height=100&section=footer" width="100%"/>


</div>
