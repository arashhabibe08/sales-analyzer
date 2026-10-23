import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="داشبورد فروش", page_icon="📊")
st.title("📊داشبورد تحلیل فروشگاه")
st.write("به داشبورد مدیریتی خوش آمدید در اینجا میتوانید گزارش های فروش را مشاهده کنید  .")
try:
    df = pd.read_csv("sales.csv")
    df["total_income"] = df["quantity"] * df["price"]

    st.subheader("📁داده های خام فروش")
    st.dataframe(df)

    total_revenue = df["total_income"].sum()
    st.metric(label="💰کل درآمد فروشگاه", value=f"{total_revenue:,} دلار")
    st.subheader("🔥پرفروش ترین محصولات ")
    best_sellers = df.groupby("product")["quantity"].sum().reset_index()
    fig, ax = plt.subplots()
    ax.bar(best_sellers["product"],  best_sellers["quantity"],color="skyblue")
    ax.set_ylabel("تعداد فروش")

    st.pyplot(fig)
except FileNotFoundError:
    st.error("⚠️ فایل sales.csvپیدا نشد لطفا ابتدا کدهای پایتون خود را اجرا کنید تا فایل ساخته شود.")

