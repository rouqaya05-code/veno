import streamlit as st
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import plotly.express as px

# إعداد الصفحة
st.set_page_config(page_title="Venus Store", layout="wide")

# شعار التطبيق
logo_url = "https://www2.0zz0.com/2025/10/27/20/506464810.png"
st.markdown(f"""
    <div style="display:flex; align-items:center; justify-content:center;">
        <img src="{logo_url}" style="height:48px; margin-right:10px;" />
        <h1 style="margin:0; font-size:48px;">Venus Store</h1>
    </div>
    <hr>
""", unsafe_allow_html=True)

# تنسيق CSS
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
        html, body, [class*="css"] {
            font-family: 'Cairo', sans-serif;
            background-color: #fef6f9;
            color: #4a148c;
        }
        .stButton>button {
            background-color: #ff69b4;
            color: white;
            border-radius: 10px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# بيانات الزبون
st.sidebar.header("Customer Info")
age = st.sidebar.slider("Age", 18, 60, 25)
income = st.sidebar.slider("Monthly Income ($)", 1000, 10000, 3000)

# قسم عروض اليوم
st.markdown("## Today's Deals")
deals = [
    {"name": "Wireless Earbuds", "price": 39, "old_price": 59, "img": "https://placehold.co/300x200?text=Earbuds"},
    {"name": "Leather Wallet", "price": 29, "old_price": 45, "img": "https://placehold.co/300x200?text=Wallet"}
]
deal_cols = st.columns(len(deals))
for i, deal in enumerate(deals):
    with deal_cols[i]:
        st.image(deal["img"], use_container_width=True)
        st.markdown(f"**{deal['name']}**")
        st.markdown(f"**${deal['price']}** ~~${deal['old_price']}~~")

st.markdown("---")

# قسم المنتجات المميزة
st.markdown("## Featured Products")
featured = [
    {"name": "Smart Watch", "price": 99, "img": "https://placehold.co/300x200?text=Smart+Watch"},
    {"name": "Stylish Backpack", "price": 75, "img": "https://placehold.co/300x200?text=Backpack"},
    {"name": "Elegant Sunglasses", "price": 55, "img": "https://placehold.co/300x200?text=Sunglasses"}
]
feat_cols = st.columns(len(featured))
for i, item in enumerate(featured):
    with feat_cols[i]:
        st.image(item["img"], use_container_width=True)
        st.markdown(f"**{item['name']}**")
        st.markdown(f"Price: ${item['price']}")

st.markdown("---")

# المنتجات الأساسية
st.markdown("## Select Your Products")
products = [
    {"name": "Red Shirt", "price": 25, "img": "https://placehold.co/300x200?text=Red+Shirt"},
    {"name": "Backpack", "price": 60, "img": "https://placehold.co/300x200?text=Backpack"},
    {"name": "Watch", "price": 120, "img": "https://placehold.co/300x200?text=Watch"},
    {"name": "Sunglasses", "price": 50, "img": "https://placehold.co/300x200?text=Sunglasses"},
    {"name": "Denim Jacket", "price": 85, "img": "https://placehold.co/300x200?text=Denim+Jacket"},
    {"name": "Running Shoes", "price": 110, "img": "https://placehold.co/300x200?text=Running+Shoes"},
    {"name": "Perfume", "price": 45, "img": "https://placehold.co/300x200?text=Perfume"},
    {"name": "Wireless Headphones", "price": 95, "img": "https://placehold.co/300x200?text=Headphones"}
]

cart = []
cols = st.columns(4)
for i, product in enumerate(products):
    with cols[i % 4]:
        st.image(product["img"], use_container_width=True)
        st.markdown(f"**{product['name']}**")
        st.markdown(f"Price: ${product['price']}")
        qty = st.number_input(f"Qty", min_value=0, max_value=10, value=0, key=product['name'])
        if qty > 0:
            cart.append({"name": product['name'], "quantity": qty, "price": product['price']})

# زر التنبؤ
if st.button("Checkout & Predict Behavior"):
    if not cart:
        st.warning("Your cart is empty!")
    else:
        purchases = sum([item['quantity'] for item in cart])
        X_input = np.array([[age, income, purchases]])
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X_input)

        # نموذج تدريبي بسيط
        X_train = np.array([
            [22, 2500, 1], [30, 4000, 2], [45, 7000, 5],
            [28, 3000, 0], [35, 5000, 3], [50, 9000, 8]
        ])
        y_train = np.array([0, 0, 1, 0, 1, 1])  # 1 = مريب

        X_train_scaled = scaler.fit_transform(X_train)
        model = LogisticRegression()
        model.fit(X_train_scaled, y_train)

        pred_prob = model.predict_proba(X_scaled)[0]
        normal_prob = pred_prob[0] * 100
        suspicious_prob = pred_prob[1] * 100

        st.subheader("Behavior Prediction")
        col1, col2 = st.columns(2)
        col1.metric("Normal Behavior", f"{normal_prob:.2f}%")
        col2.metric("Suspicious Behavior", f"{suspicious_prob:.2f}%")

        fig = px.pie(
            names=["Normal", "Suspicious"],
            values=[normal_prob, suspicious_prob],
            color=["Normal", "Suspicious"],
            color_discrete_map={"Normal": "#ffb6c1", "Suspicious": "#ff69b4"},
            title="Customer Behavior Analysis"
        )
        st.plotly_chart(fig, use_container_width=True)

