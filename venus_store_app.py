# ------------------------ تثبيت المكتبات ------------------------
!pip install streamlit pandas numpy scikit-learn plotly --quiet

# ------------------------ ملف التطبيق ------------------------
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import plotly.express as px

# ======================= إعداد الصفحة =======================
st.set_page_config(page_title="Venus Store 🌸", layout="wide")

# ======================= تنسيق الألوان والخطوط =======================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
html, body, [class*="css"] {
    font-family: 'Cairo', sans-serif;
    background: linear-gradient(to bottom, #ffe6f0, #fff0f5);
    color: #4a148c;
}
.stButton>button {
    background: linear-gradient(90deg, #ff99cc, #ff66b2);
    color: white;
    border-radius: 10px;
    font-weight: bold;
    transition: 0.3s;
}
.stButton>button:hover {
    background: linear-gradient(90deg, #ff66b2, #ff99cc);
    transform: scale(1.02);
}
h1 {
    color: #d63384;
    text-align: center;
    text-shadow: 1px 1px 3px #f8bbd0;
}
</style>
""", unsafe_allow_html=True)

# ======================= بيانات المنتجات =======================
products = {
    "Red Shirt": {"price": 25, "img": "https://i.pinimg.com/1200x/31/ce/f5/31cef5d7bfe8734918d5596323996ff4.jpg"},
    "Backpack": {"price": 50, "img": "https://i.pinimg.com/736x/a0/c4/17/a0c4175e744040d0d5e8527bbde49e04.jpg"},
    "Watch": {"price": 120, "img": "https://i.pinimg.com/736x/0e/e1/49/0ee149229d01511714827e5a3f055ddf.jpg"},
    "Sunglasses": {"price": 75, "img": "https://i.pinimg.com/1200x/dd/43/99/dd4399d6603c9f7468aa3920fa69c032.jpg"}
}

# ======================= واجهة المستخدم =======================
st.title("Venus Store 🌸")

st.markdown("## Products")

cart = {}
cols = st.columns(len(products))
for i, (name, info) in enumerate(products.items()):
    with cols[i]:
        st.image(info["img"], use_container_width=True)
        st.write(name)
        quantity = st.number_input(f"Quantity of {name}", min_value=0, max_value=10, key=name)
        if quantity > 0:
            cart[name] = quantity

# ======================= زر الشراء =======================
if st.button("Purchase"):
    if not cart:
        st.warning("Please select at least one product!")
    else:
        st.success("Purchase completed!")

        # ======================= محاكاة تنبؤ السلوك =======================
        # كل عملية شراء جديدة تعطي احتمال سلوك مريب
        total_items = sum(cart.values())
        user_data = np.array([[total_items]])
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(user_data)  # محاكاة فقط
        model = LogisticRegression()
        # نحتاج على الأقل صنفين لتدريب النموذج، محاكاة بيانات
        model.fit(np.array([[0],[5]]), [0,1])
        prob = model.predict_proba(X_scaled)[0]
        normal_pct = prob[0]*100
        suspicious_pct = prob[1]*100

        st.subheader("Customer Behavior Prediction")
        fig = px.bar(
            x=["Normal", "Suspicious"],
            y=[normal_pct, suspicious_pct],
            color=["Normal","Suspicious"],
            color_discrete_sequence=["#ff99cc","#ff66b2"],
            labels={'x':'Behavior','y':'Probability %'}
        )
        st.plotly_chart(fig, use_container_width=True)
