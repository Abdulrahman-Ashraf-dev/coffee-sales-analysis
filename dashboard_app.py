import streamlit as st
import pandas as pd
import plotly.express as px



# ---------- Page Config ----------
st.set_page_config(page_title="Coffee Sales Dashboard", page_icon="☕", layout="wide")

# ---------- Load Data ----------
@st.cache_data
def load_data():
    df = pd.read_csv("coffee_sales_dataset.csv")
    return df

df = load_data()

# ---------- Header ----------
st.title("☕ Coffee Sales Dashboard")
st.markdown("### Explore insights about coffee sales performance")

# ---------- KPIs ----------
total_revenue = df["revenue"].sum()
avg_discount = df["discount_pct"].mean()
total_orders = df["order_id"].nunique()

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Avg. Discount", f"{avg_discount:.2%}")
col3.metric("Total Orders", total_orders)

st.markdown("---")

# ---------- Filter Section ----------
region = st.selectbox("Select Region", ["All"] + sorted(df["region"].unique().tolist()))

filtered_df = df if region == "All" else df[df["region"] == region]

# ---------- Charts ----------
st.subheader("Revenue by Product")
fig1 = px.bar(filtered_df, x="product", y="revenue", color="product", title="Revenue by Product")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Sales Trend Over Time")
fig2 = px.line(filtered_df, x="date", y="revenue", color="region", title="Revenue Over Time")
st.plotly_chart(fig2, use_container_width=True)
