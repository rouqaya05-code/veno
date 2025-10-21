import streamlit as st
import pandas as pd
import numpy as np
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
    "Backpack": {"price": 50, "img": "https://i.pinimg.com/736x/d1/70/ec/d170ec923e5e6a3c4f6cf75c84ddbafc.jpg"},
    "Watch": {"price": 120, "img": "https://i.pinimg.com/736x/0e/e1/49/0ee149229d01511714827e5a3f055ddf.jpg"},
    "Sunglasses": {"price": 75, "img": "https://i.pinimg.com/1200x/dd/43/99/dd4399d6603c9f7468aa3920fa69c032.jpg"},
    "White Dress": {"price": 300, "img": "https://i.pinimg.com/736x/40/80/38/4080388676549a16a6a03da69c588f22.jpg"},
    "Pink Pajamas": {"price": 23, "img": "https://i.pinimg.com/1200x/bb/a9/0b/bba90b9eaf89df5f15df26cc6b46c528.jpg"},
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
        total_items = sum(cart.values())

        # منطق السلوك: طبيعي إذا <5، مريب إذا >=5
        if total_items < 3:
            normal_pct = 100
            suspicious_pct = 0
        else:
            normal_pct = max(0, 100 - (total_items - 4)*20)  # كل زيادة بعد 4 تخفض الطبيعي
            suspicious_pct = 100 - normal_pct
            normal_pct = max(normal_pct, 0)
            suspicious_pct = min(suspicious_pct, 100)

        st.subheader("Customer Behavior Prediction")
        fig = px.bar(
            x=["Normal", "Suspicious"],
            y=[normal_pct, suspicious_pct],
            color=["Normal","Suspicious"],
            color_discrete_sequence=["#ff99cc","#ff66b2"],
            labels={'x':'Behavior','y':'Probability %'}
        )
        st.plotly_chart(fig, use_container_width=True)


