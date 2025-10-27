# File: venus_store_app.py

import streamlit as st
import pandas as pd
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
        <img src="{logo_url}" style="width:32px; height:32px; margin-right:10px;" />
        <h1 style="margin:0;">Venus Store</h1>
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

# المنتجات
products = [
    {"name": "Red Shirt", "price": 25, "img": "https://i.pinimg.com/1200x/31/ce/f5/31cef5d7bfe8734918d5596323996ff4.jpg"},
    {"name": "Backpack", "price": 60, "img": "https://i.pinimg.com/736x/a0/c4/17/a0c4175e744040d0d5e8527bbde49e04.jpg"},
    {"name": "Watch", "price": 120, "img": "https://i.pinimg.com/736x/0e/e1/49/0ee149229d01511714827e5a3f055ddf.jpg"},
    {"name": "Sunglasses", "price": 50, "img": "https://i.pinimg.com/1200x/dd/43/99/dd4399d6603c9f7468aa3920fa69c032.jpg"}
]

st.markdown("### Select your products:")
cart = []
cols = st.columns(4)
for i, product in enumerate(products):
    with cols[i]:
        st.image(product["img"], use_column_width=True)
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
