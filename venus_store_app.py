import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import plotly.express as px

# ======================= إعداد الصفحة =======================
st.set_page_config(
    page_title="Venus Store",
    page_icon="🌸",
    layout="wide"
)

# ======================= تنسيق الألوان والخطوط =======================
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
        html, body, [class*="css"]  {
            font-family: 'Cairo', sans-serif;
            background: linear-gradient(#ffe6f0, #fff0f5);
            color: #4a148c;
        }
        .stButton>button {
            background: linear-gradient(90deg, #ffb6c1, #ff69b4);
            color: white;
            border-radius: 10px;
            font-weight: bold;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #ff69b4, #ffb6c1);
            transform: scale(1.02);
        }
        h1, h2, h3 {
            color: #4a148c;
        }
        .block-container {
            padding-top: 2rem;
        }
        .stSlider>div>div>div>div {
            color: #4a148c;
        }
    </style>
""", unsafe_allow_html=True)

# ======================= بيانات وهمية للمنتجات =======================
products = [
    {"name": "Red Shirt", "price": 25, "image": "https://i.pinimg.com/1200x/31/ce/f5/31cef5d7bfe8734918d5596323996ff4.jpg"},
    {"name": "Backpack", "price": 60, "image": "https://i.pinimg.com/736x/a0/c4/17/a0c4175e744040d0d5e8527bbde49e04.jpg"},
    {"name": "Wrist Watch", "price": 120, "image": "https://i.pinimg.com/736x/0e/e1/49/0ee149229d01511714827e5a3f055ddf.jpg"},
    {"name": "Sunglasses", "price": 40, "image": "https://i.pinimg.com/1200x/dd/43/99/dd4399d6603c9f7468aa3920fa69c032.jpg"}
]

# ======================= واجهة المستخدم =======================
st.title("🌸 Venus Store")
st.markdown("---")

st.subheader("Select products and quantities:")

cart_data = []
for prod in products:
    qty = st.number_input(f"{prod['name']} (${prod['price']})", min_value=0, max_value=20, value=0, step=1)
    cart_data.append(qty)

total_items = sum(cart_data)
total_amount = sum([cart_data[i]*products[i]['price'] for i in range(len(products))])

st.markdown(f"**Total items:** {total_items} | **Total amount:** ${total_amount}")

# ======================= نموذج بسيط لتصنيف السلوك =======================
# خصائص: [total_items, total_amount]
X = np.array([[i, i*prod['price']] for i, prod in zip([1,3,5,10], products[:4])])
y = np.array([0, 0, 1, 1])  # 0 = Normal, 1 = Suspicious

scaler = StandardScaler()
X_scaled = scaler.fit_transform(np.array([[total_items, total_amount]]))

# تدريب نموذج لوجستيك بسيط
model = LogisticRegression()
# تدريب افتراضي على بيانات بسيطة
X_train = np.array([[1,50],[2,100],[5,250],[10,500]])
y_train = np.array([0,0,1,1])
model.fit(X_train, y_train)

prediction = model.predict(X_scaled)[0]
prob = model.predict_proba(X_scaled)[0]

cat_normal = prob[0]*100
cat_suspicious = prob[1]*100

# ======================= عرض النتائج =======================
if total_items > 0:
    st.subheader("Customer Behavior Prediction")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Normal Behavior", f"{cat_normal:.2f} %")
    with col2:
        st.metric("Suspicious Behavior", f"{cat_suspicious:.2f} %")

    fig = px.bar(
        x=["Normal", "Suspicious"],
        y=[cat_normal, cat_suspicious],
        color=["Normal", "Suspicious"],
        color_discrete_sequence=["#ffb6c1","#ff69b4"],
        labels={'x':'Behavior', 'y':'Probability'},
        title="Behavior Probability"
    )
    fig.update_layout(
        plot_bgcolor="#fff0f5",
        paper_bgcolor="#fff0f5",
        font=dict(color="#4a148c", size=16),
        title_x=0.4
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Add products to the cart to see behavior prediction.")
