import streamlit as st
import plotly.express as px

# إعداد الصفحة
st.set_page_config(page_title="Mytheresa", layout="wide")

# تنسيق CSS
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

# قسم العروض
st.markdown("<div class='section-title'>HOLIDAY SEASON IS COMING</div>", unsafe_allow_html=True)
st.image("https://www.mytheresa.com/content/2760/1250/65/8b117e66-3bef-4dc4-8eeb-e1facf155a7e.jpg", use_container_width=True)

# المنتجات
st.markdown("<div class='section-title'>Best-selling Categories</div>", unsafe_allow_html=True)
products = [
    {"name": "Mini croc-effect tote bag", "price": 600, "img": "https://i.pinimg.com/736x/ad/f6/0d/adf60d0058ebb13457f6d239eeb0b4b0.jpg"},
    {"name": "Quilted jacket", "price": 1000, "img": "https://www.mytheresa.com/media/1094/1238/100/e5/P01117649.jpg"},
    {"name": "Satin halterneck gown", "price": 1200, "img": "https://www.mytheresa.com/media/1094/1238/100/8c/P01114291_b1.jpg"},
    {"name": "Leather slingback pumps", "price": 695, "img": "https://www.mytheresa.com/media/1094/1238/100/5c/P01108790.jpg"}
]

# سلة المشتريات
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
            color = "#e4b7c4"
        else:
            behavior = "Suspicious"
            color = "#990033"

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
