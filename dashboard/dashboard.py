import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
import os

# Set Page Config
st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")

@st.cache_data
def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    file_path = os.path.join(current_dir, "Main_Data.zip")
    
    df = pd.read_csv(file_path, compression='zip')
    
    datetime_columns = ["order_purchase_timestamp", "order_delivered_customer_date"]
    for col in datetime_columns:
        df[col] = pd.to_datetime(df[col])
        
    return df

main_df = load_data()

# SIDEBAR
with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    st.title("Filter Data")
    # Filter rentang waktu
    min_date = main_df["order_purchase_timestamp"].min()
    max_date = main_df["order_purchase_timestamp"].max()
    
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Filter dataframe berdasarkan sidebar
filtered_df = main_df[(main_df["order_purchase_timestamp"] >= pd.to_datetime(start_date)) & 
                       (main_df["order_purchase_timestamp"] <= pd.to_datetime(end_date))]

st.header('Olist E-Commerce Dashboard :sparkles:')

col1, col2 = st.columns(2)
with col1:
    total_orders = filtered_df.order_id.nunique()
    st.metric("Total Pesanan", value=total_orders)

with col2:
    total_revenue = format_currency(filtered_df.price.sum(), "BRL", locale='pt_BR') 
    st.metric("Total Pendapatan", value=total_revenue)

st.divider()

# PRODUK
st.subheader("Performa Kategori Produk (Revenue vs Rating)")

# 1. Agregasi data (Top 10)
cat_perf = filtered_df.groupby('product_category_name_english').agg({
    'price': 'sum',
    'review_score': 'mean'
}).sort_values('price', ascending=False).head(10).reset_index()

# 2. Membuat Plot
fig, ax1 = plt.subplots(figsize=(14, 7))

# Bar Chart untuk Revenue (Sumbu Y kiri)
sns.barplot(
    data=cat_perf, 
    x='product_category_name_english', 
    y='price', 
    ax=ax1, 
    color='royalblue'
)
ax1.set_ylabel('Total Revenue (BRL)', fontsize=12)
ax1.set_xlabel('Product Category', fontsize=12)
ax1.set_title('Top 10 Product Categories: Revenue vs Satisfaction', fontsize=15)
plt.xticks(rotation=45, ha='right')

# 3. Line Chart untuk Review Score (Sumbu Y kanan)
ax2 = ax1.twinx()
sns.lineplot(
    data=cat_perf, 
    x='product_category_name_english', 
    y='review_score', 
    ax=ax2, 
    color='red', 
    marker='o', 
    linewidth=2,
    label='Avg Review Score'
)
ax2.set_ylabel('Average Review Score (1-5)', fontsize=12)
ax2.set_ylim(0, 5) # Skala rating 1-5
ax2.legend(loc='upper right')

plt.tight_layout()
st.pyplot(fig)

# GEOGRAFI & LOYALITAS
st.subheader("Analisis Pelanggan")
col3, col4 = st.columns(2)

with col3:
    st.markdown("### Distribusi per Negara Bagian")
    state_df = filtered_df.groupby("customer_state").order_id.nunique().sort_values(ascending=False).reset_index()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.barplot(data=state_df.head(10), x='order_id', y='customer_state', color='royalblue')
    st.pyplot(fig)

with col4:
    st.markdown("### Profil Loyalitas")
    loyalty_counts = filtered_df.groupby('customer_unique_id')['order_id'].nunique()
    loyalty_status = loyalty_counts.apply(lambda x: 'Repeat Order' if x > 1 else 'Single Order').value_counts()
    
    fig, ax = plt.subplots()
    ax.pie(loyalty_status, labels=loyalty_status.index, autopct='%1.1f%%', startangle=140, colors=['#66b3ff','#ff9999'])
    st.pyplot(fig)

st.caption('Copyright (c) Ammar 2026')