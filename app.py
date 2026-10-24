import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="داشبورد فروش", page_icon="📊")
st.title("📊داشبورد تحلیل فروشگاه")
st.write("شما میتوانید فایل CSVخود را اینجا اپلود کنید تا تحلیل شود.")

uploaded_file = st.file_uploader("یک فایل CSVانتخاب کنید", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅فایل شما با موفقیت اپلود و خوانده شد!")
else:

    try:
        df = pd.read_csv("sales.csv")
        st.info("ℹ️درحال نمایش داده های پیش فرض (sales.csv).برای دیدن فایل خودتان از دکمه  بالا استفاده کنید")
    except FileNotFoundError:
        st.error("⚠️فایل پیش فرض پیدا نشد لطفا یک فایل آپلود کنید.")
        st.stop()


try:

    df["total_income"] = df["quantity"] * df["price"]

    st.subheader("📁 داده های خام فروش")
    st.dataframe(df)

    total_revenue = df["total_income"].sum()
    st.metric(label="💰کل درآمد فروشگاه", value=f"{total_revenue:},دلار")


    st.subheader("🔥پر فروش ترین محصولات")
    best_sellers = df.groupby("product")["quantity"].sum().reset_index()

    fig, ax = plt.subplots()
    ax.bar(best_sellers["product"], best_sellers["quantity"], color="skyblue")
    ax.set_ylabel("تعداد فروش")
    st.pyplot(fig)
except KeyError:
    st.warning("⚠️ستون های فایل شما باید دقیقا شامل name, product, quantity, price باشد.")
except Exception as e:
    st.error(f"خطایی رخ داد : {e}")

