import streamlit as st
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import plotly.express as px

# إعداد الصفحة
st.set_page_config(page_title="MYTHERESA", layout="wide")

# تنسيق CSS للخطوط والتصميم
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;700&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Libre Baskerville', serif;
            background-color: #fef6f9;
            color: #2c2c2c;
        }

        h1, h2, h3, h4 {
            font-family: 'Playfair Display', serif;
            letter-spacing: 1px;
        }

        .stButton>button {
            background-color: #000;
            color: white;
            border-radius: 0px;
            font-weight: bold;
            font-family: 'Libre Baskerville', serif;
        }

        .stSlider label, .stNumberInput label {
            font-weight: bold;
        }

        .product-title {
            font-family: 'Playfair Display', serif;
            font-size: 18px;
            font-weight: 600;
        }
    </style>
""", unsafe_allow_html=True)

# عنوان المتجر
st.markdown("<h1 style='text-align:center;'>MYTHERESA</h1><hr>", unsafe_allow_html=True)

# بيانات الزبون
st.sidebar.header("Customer Info")
age = st.sidebar.slider("Age", 18, 60, 25)
income = st.sidebar.slider("Monthly Income ($)", 1000, 10000, 3000)

# قسم عروض اليوم (صور فقط بدون نص)
st.markdown("## Today's Deals")
deal_images = [
    "https://www2.0zz0.com/2025/10/27/21/138787801.png",
    "https://i.pinimg.com/1200x/9a/00/c8/9a00c8436f2fadecb607943533041883.jpg"
]
deal_cols = st.columns(len(deal_images))
for i, img_url in enumerate(deal_images):
    with deal_cols[i]:
        st.image(img_url, use_container_width=True)

st.markdown("---")

# قسم المنتجات المميزة
st.markdown("## Featured Products")
featured = [
    {"name": "Coffee 1940s Faux Fur Coat", "price": 200, "img": "https://i.pinimg.com/736x/89/1b/06/891b06dc311ba96d1cad22eed7f986f1.jpg"},
    {"name": "1996 gripoix-buttons velour shirt", "price": 500, "img": "https://i.pinimg.com/736x/ac/a2/1e/aca21e70d95e62dedc827d59018a371a.jpg"},
    {"name": "Chichi silk bustier gown", "price": 800, "img": "https://i.pinimg.com/736x/ad/f6/0d/adf60d0058ebb13457f6d239eeb0b4b0.jpg"}
]
feat_cols = st.columns(len(featured))
for i, item in enumerate(featured):
    with feat_cols[i]:
        st.image(item["img"], use_container_width=True)
        st.markdown(f"<div class='product-title'>{item['name']}</div>", unsafe_allow_html=True)
        st.markdown(f"Price: ${item['price']}")

st.markdown("---")

# المنتجات الأساسية
st.markdown("## Best-selling Categories")
products = [
    {"name": "Bettina Mini croc-effect leather tote bag", "price": 600, "img": "https://i.pinimg.com/736x/ad/f6/0d/adf60d0058ebb13457f6d239eeb0b4b0.jpg"},
    {"name": "Anagram leather-trimmed quilted jacket", "price": 1000, "img": "https://www.mytheresa.com/media/1094/1238/100/e5/P01117649.jpg"},
    {"name": "Florie satin-trimmed halterneck gown", "price": 1200, "img": "https://www.mytheresa.com/media/1094/1238/100/8c/P01114291_b1.jpg"},
    {"name": "Holli 70 mirrored leather slingback pumps", "price": 695, "img": "https://www.mytheresa.com/media/1094/1238/100/5c/P01108790.jpg"},
    {"name": "Mid-rise barrel-leg jeans", "price": 850, "img": "https://www.mytheresa.com/media/1094/1238/100/0a/P01084945.jpg"},
    {"name": "Uma shearling wrap coat", "price": 1400, "img": "https://www.mytheresa.com/media/1094/1238/100/84/P01102423.jpg"},
    {"name": "Cassandre Envelope Small leather wallet on chain", "price": 950, "img": "https://www.mytheresa.com/media/1094/1238/100/2d/P01130307_b1.jpg"},
    {"name": "Alaska suede mid-calf boots", "price": 1100, "img": "https://www.mytheresa.com/media/1094/1238/100/10/P01129115_d2.jpg"}
]

cart = []
cols = st.columns(4)
for i, product in enumerate(products):
    with cols[i % 4]:
        st.image(product["img"], use_container_width=True)
        st.markdown(f"<div class='product-title'>{product['name']}</div>", unsafe_allow_html=True)
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
            color_discrete_map={"Normal": "#d4afcd", "Suspicious": "#ff69b4"},
            title="Customer Behavior Analysis"
        )
        st.plotly_chart(fig, use_container_width=True)
