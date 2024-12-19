import streamlit as st
import pickle
import pandas as pd
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log",
    filemode="a"  # Append to the log file
)

logging.info("BigMart Sales Prediction App started.")

try:
    # Load the model
    with open("BigMart_Model.pkl", "rb") as file:
        model = pickle.load(file)
    logging.info("Model loaded successfully.")
except Exception as e:
    logging.error(f"Error loading model: {e}")
    st.error("Error loading the model. Please check the log file.")
    st.stop()

try:
    # Load encoders
    with open("BigMart_Encodings.pkl", "rb") as file:
        encoders = pickle.load(file)
    logging.info("Encoders loaded successfully.")
except Exception as e:
    logging.error(f"Error loading encoders: {e}")
    st.error("Error loading encoders. Please check the log file.")
    st.stop()

# Sidebar navigation
st.sidebar.title("Home")
page = st.sidebar.radio("Go to", ["Description", "Sales Prediction"])

if page == "Description":
    st.title("BigMart Sales Prediction APP")
    st.markdown(
    """

    ### Big Mart Sales Predictor

    Predict product sales across Big Mart outlets with ease! This app leverages machine learning and real-world data to provide actionable insights into sales performance.

    ### Key Features:
    - **Data-Driven Insights:** Analyze how product characteristics and outlet attributes affect sales.
    - **User-Friendly Interface:** Input product and outlet details with ease.
    - **Accurate Predictions:** Get reliable sales forecasts based on the trained model.
    ### How It Works:
    1. Fill in the product and outlet details in the form below.
    2. Click the "Predict Sales" button to get the estimated sales.

    ### About the Project:
    This project uses advanced machine learning techniques and real-world data from BigMart to help businesses optimize their operations and improve revenue generation. The model has been trained on a comprehensive dataset with features such as item type, outlet location, and more.

    ### Objectives:
    - Provide actionable insights for inventory and sales management.
    - Enhance decision-making for pricing and stocking strategies.
    

    """
)

elif page == "Sales Prediction":
    
    st.header("Input Features")

    # Create two columns for side-by-side input
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("### Product Information")
        item_identifier = st.text_input("Item Identifier")
        item_weight = st.slider("Item Weight (kg)", min_value=0.0, max_value=100.0, step=0.1)
        item_fat_content = st.selectbox("Item Fat Content", ["Low Fat", "Regular"])
        item_visibility = st.slider("Item Visibility (%)", min_value=0.0, max_value=1000.0, step=0.01)
        item_type = st.selectbox(
            "Item Type", 
            ['Dairy', 'Soft Drinks', 'Meat', 'Fruits and Vegetables', 'Household', 'Baking Goods',
             'Snack Foods', 'Frozen Foods', 'Breakfast', 'Health and Hygiene', 'Hard Drinks',
             'Canned', 'Breads', 'Starchy Foods', 'Others', 'Seafood']
        )
        item_mrp = st.number_input("Item MRP (₹)", min_value=0.0, max_value=1000.0, step=0.1)

    with col2:
        st.markdown("### Outlet Information")
        outlet_identifier = st.selectbox(
            "Outlet Identifier", 
            ['OUT049', 'OUT018', 'OUT010', 'OUT013', 'OUT027', 'OUT045', 
             'OUT017', 'OUT046', 'OUT035', 'OUT019']
        )
        outlet_establishment_year = st.radio(
            "Outlet Establishment Year", 
            [1999, 2009, 1998, 1987, 1985, 2002, 2007, 1997, 2004],
            horizontal=True
        )
        outlet_size = st.radio(
            "Outlet Size", 
            options=["Small", "Medium", "High"], 
            horizontal=True
        )
        outlet_location_type = st.radio(
            "Outlet Location Type", 
            ["Tier 1", "Tier 2", "Tier 3"], 
            horizontal=True
        )
        outlet_type = st.selectbox(
            "Outlet Type", 
            ["Supermarket Type1", "Supermarket Type2", "Supermarket Type3", "Grocery Store"]
        )

    st.markdown("---")

    # Validation
    try:
        item_weight = float(item_weight) if item_weight else 0.0
        item_visibility = float(item_visibility) if item_visibility else 0.0
        item_mrp = float(item_mrp) if item_mrp else 0.0
    except ValueError as e:
        logging.warning(f"Invalid input: {e}")
        st.error(f"Invalid input: {e}")
        st.stop()

    # Encoding inputs
    try:
        encoded_inputs = {
            "Item_Identifier": encoders["Item_Identifier"].transform([item_identifier])[0] if item_identifier in list(encoders["Item_Identifier"].classes_) else -1,
            "Item_Weight": item_weight,
            "Item_Fat_Content": encoders["Item_Fat_Content"].transform([item_fat_content])[0] if item_fat_content in list(encoders["Item_Fat_Content"].classes_) else -1,
            "Item_Visibility": item_visibility,
            "Item_Type": encoders["Item_Type"].transform([item_type])[0] if item_type in list(encoders["Item_Type"].classes_) else -1,
            "Item_MRP": item_mrp,
            "Outlet_Identifier": encoders["Outlet_Identifier"].transform([outlet_identifier])[0] if outlet_identifier in list(encoders["Outlet_Identifier"].classes_) else -1,
            "Outlet_Establishment_Year": outlet_establishment_year,
            "Outlet_Size": encoders["Outlet_Size"].transform([outlet_size])[0] if outlet_size in list(encoders["Outlet_Size"].classes_) else -1,
            "Outlet_Location_Type": encoders["Outlet_Location_Type"].transform([outlet_location_type])[0] if outlet_location_type in list(encoders["Outlet_Location_Type"].classes_) else -1,
            "Outlet_Type": encoders["Outlet_Type"].transform([outlet_type])[0] if outlet_type in list(encoders["Outlet_Type"].classes_) else -1,
        }
        logging.info("Inputs encoded successfully.")
    except AttributeError as e:
        logging.error(f"Encoding error: {e}")
        st.error(f"Encoding error: {e}")
        st.stop()

    input_df = pd.DataFrame([encoded_inputs])

    # Prediction button
    if st.button("Predict Sales"):
        if item_identifier not in encoders["Item_Identifier"].classes_:
            logging.error(f"Invalid Item Identifier: {item_identifier}")
            st.error(f"Invalid Item Identifier: {item_identifier}. Please enter a valid identifier.")
        else:
            try:
                prediction = model.predict(input_df)
                logging.info(f"Prediction successful: {prediction[0]}")
                st.success(f"Predicted Sales: ₹{prediction[0]:,.2f}")
            except Exception as e:
                logging.error(f"Prediction error: {e}")
                st.error(f"An error occurred during prediction: {e}")
