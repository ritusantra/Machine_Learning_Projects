import streamlit as st
import pandas as pd
import pickle

# -------------------------------
# Load Models & Pipelines - Final
# -------------------------------

def cost_cols(df):
    df['Weight (Kilograms)'] = df['Weight (Kilograms)'].astype(str).str.extract(r'(\d+\.?\d*)')
    df['Weight (Kilograms)'] = pd.to_numeric(df['Weight (Kilograms)'])
    df['Freight Cost (USD)'] = df['Freight Cost (USD)'].astype(str).str.extract(r'(\d+\.?\d*)')
    df['Freight Cost (USD)'] = pd.to_numeric(df['Freight Cost (USD)'])
    df['Weight (Kilograms)'] = df['Weight (Kilograms)'].fillna(df['Weight (Kilograms)'].mean())
    df['Freight Cost (USD)'] = df['Freight Cost (USD)'].fillna(df['Freight Cost (USD)'].mean())
    return df

def missing(df):
    df['Shipment Mode'] = df['Shipment Mode'].fillna('Unknown')
    return df

with open("shp_ins_model.pkl", "rb") as f:
    ins_model = pickle.load(f)
with open("shp_ins_pipeline.pkl", "rb") as f:
    ins_pipe = pickle.load(f)
with open("shp_type_model.pkl", "rb") as f:
    mode_model = pickle.load(f)
with open("shp_type_pipeline.pkl", "rb") as f:
    mode_pipe = pickle.load(f)

# -------------------------------
# App Title
# -------------------------------
st.markdown("""
    # 🚢 PredictShip: One Stop Shipment Intelligence System
    ### ML Based Shipment Mode & Shipment Insurance Prediction System
""")

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("🔍 Prediction Module")
model_choice = st.sidebar.radio(
    "Choose Prediction Module",
    ["Shipment Mode", "Insurance Cost"]
)
st.sidebar.markdown("---")
st.sidebar.markdown("""
**💰 Cost Savings** – Estimates shipment insurance cost (USD).  
**⚡ Faster Decisions** – Quickly predicts optimal shipment mode.  
**🛡️ Risk Reduction** – Helps avoid financial and logistical setbacks.
""")

st.divider()

# =====================================================
# 🛡️ Insurance Cost Prediction
# =====================================================
if model_choice == "Insurance Cost":
    st.subheader("Insurance Cost Prediction")

    col1, col2 = st.columns(2)
    with col1:
        pack_price = st.number_input("Pack Price (USD)", 0.0, 1345.64, 22.0)
        weight = st.number_input("Weight (kg)", 0.0, 857354.0, 4000.0)
    with col2:
        qty = st.number_input("Line Item Quantity", 1, 619999, 20000)
        freight = st.number_input("Freight Cost (USD)", 0.0, 289653.20, 10000.0)

    mode = st.selectbox("Shipment Mode", ["Air", "Air Charter", "Ocean", "Truck"])

    if st.button("Predict Insurance", use_container_width=True):
        df = pd.DataFrame({
            "Pack Price": [pack_price],
            "Line Item Quantity": [qty],
            "Weight (Kilograms)": [weight],
            "Freight Cost (USD)": [freight],
            "Shipment Mode": [mode]
        })
        X = ins_pipe.transform(df)
        pred = ins_model.predict(X)[0]
        st.success(f"💰 Predicted Insurance Cost: ${pred:.2f}")

# =====================================================
# 🚚 Shipment Mode Prediction
# =====================================================
else:
    st.subheader("Shipment Mode Prediction")

    col1, col2 = st.columns(2)
    with col1:
        qty = st.number_input("Line Item Quantity", 1, 619999, 5000)
        pack_price = st.number_input("Pack Price (USD)", 0.0, 1250.0, 10.0)
        country = st.text_input("Country", "Kenya")
        product = st.selectbox("Product Group", ["ACT", "ANTM", "ARV", "HRDT", "MRDT"])
    with col2:
        value = st.number_input("Line Item Value (USD)", 0.0, 5951991.0, 100000.0)
        weight = st.number_input("Weight (kg)", 0.0, 857354.00, 4000.0)
        vendor = st.text_input("Vendor", "CIPLA LIMITED")

    if st.button("Predict Mode", use_container_width=True):
        df = pd.DataFrame({
            "Line Item Quantity": [qty],
            "Line Item Value": [value],
            "Pack Price": [pack_price],
            "Country": [country],
            "Vendor": [vendor],
            "Product Group": [product],
            "Weight (Kilograms)": [weight]
        })
        X = mode_pipe.transform(df)
        pred = mode_model.predict(X)[0]
        labels = ["Air", "Air Charter", "Ocean", "Truck"]
        st.success(f"🚚 Predicted Shipment Mode: {labels[int(pred)]}")