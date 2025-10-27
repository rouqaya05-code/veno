import streamlit as st
import plotly.express as px

# إعداد الصفحة
st.set_page_config(page_title="Mytheresa", layout="wide")

# تنسيق CSS للخطوط والتصميم
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Libre Baskerville', serif;
            background-color: #fef6f9;
            color: #2c2c2c;
        }

        .store-title {
            font-family: 'Cinzel Decorative', serif;
            font-size: 64px;
            text-align: center;
            color: #1a1a1a;
            margin-top: 1rem;
            margin-bottom: 1rem;
            letter-spacing: 2px;
        }

        .section-title {
            font-family: 'Playfair Display', serif;
            font-size: 36px;
            font-weight: 700;
            text-align: center;
            color: #1a1a1a;
            margin-top: 2rem;
            margin-bottom: 1rem;
            letter-spacing: 1px;
        }

        .price-tag {
            font-family: 'Libre Baskerville', serif;
            font-size: 18px;
            font-weight: bold;
            color: #6b0f1a;
        }

        .product-title {
            font-family: 'Playfair Display', serif;
            font-size: 18px;
            font-weight: 600;
        }

        .stButton>button {
            background-color: #000;
            color: white;
            border-radius: 0px;
            font-weight: bold;
            font-family: 'Libre Baskerville', serif;
        }

        .clear-button {
            text-align: center;
            margin-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# عنوان المتجر
st.markdown("<div class='store-title'>Mytheresa</div><hr>", unsafe_allow_html=True)

# بيانات الزبون
st.sidebar.header("Customer Info")
age = st.sidebar.slider("Age", 18, 60, 25)
income = st.sidebar.slider("Monthly Income ($)", 1000, 10000, 3000)

# قسم العروض
st.markdown("<div class='section-title'>HOLIDAY SEASON IS COMING</div>", unsafe_allow_html=True)
st.image("https://www.mytheresa.com/content/2760/1250/65/8b117e66-3bef-4dc4-8eeb-e1facf155a7e.jpg", use_container_width=True)

st.markdown("---")

# قسم المنتجات المميزة
st.markdown("<div class='section-title'>Featured Products</div>", unsafe_allow_html=True)
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
        st.markdown(f"<div class='price-tag'>${item['price']}</div>", unsafe_allow_html=True)

st.markdown("---")

# المنتجات الأساسية
st.markdown("<div class='section-title'>Best-selling Categories</div>", unsafe_allow_html=True)
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

if "cart" not in st.session_state:
    st.session_state.cart = []

cols = st.columns(4)
for i, product in enumerate(products):
    with cols[i % 4]:
        st.image(product["img"], use_container_width=True)
        st.markdown(f"<div class='product-title'>{product['name']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='price-tag'>${product['price']}</div>", unsafe_allow_html=True)
        qty = st.number_input(f"Qty", min_value=0, max_value=10, value=0, key=product['name'])
        if qty > 0:
            st.session_state.cart.append({"name": product['name'], "quantity": qty, "price": product['price']})

# زر التنبؤ
if st.button("Checkout & Predict Behavior"):
    purchases = sum([item['quantity'] for item in st.session_state.cart])
    st.markdown("<div class='section-title'>Behavior Prediction</div>", unsafe_allow_html=True)

    if purchases == 0:
        st.warning("No items selected.")
    else:
        if purchases <= 3:
            behavior = "Normal"
        else:
            behavior = "Suspicious"

        fig = px.pie(
            names=["Normal", "Suspicious"],
            values=[100 if behavior == "Normal" else 0, 100 if behavior == "Suspicious" else 0],
            color=["Normal", "Suspicious"],
            color_discrete_map={
                "Normal": "#e4b7c4",
                "Suspicious": "#990033"
            },
            title="Customer Behavior Analysis",
            hole=0.3
        )
        fig.update_traces(textinfo='percent+label', textfont_size=16)
        st.plotly_chart(fig, use_container_width=True)

# زر Clear لإعادة تعيين المشتريات
st.markdown("<div class='clear-button'>", unsafe_allow_html=True)
if st.button("Clear"):
    st.session_state.cart = []
    st.success("Cart cleared. Purchases reset to zero.")
st.markdown("</div>", unsafe_allow_html=True)
