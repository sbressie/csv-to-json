
import streamlit as st
import pandas as pd
import json

st.set_page_config(page_title="CSV to JSON Converter", layout="centered")

st.title("📄 CSV to JSON Converter for AJAX")
st.markdown("Upload a CSV file and get a valid JSON output for frontend AJAX usage.")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

indent_level = st.slider("Indentation (for readability)", 0, 8, 2)
orient_option = st.selectbox(
    "Choose JSON Structure",
    options=["records", "split", "index", "columns", "values"],
    help="Choose a format that matches how your HTML/JS frontend expects data."
)

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("CSV loaded successfully!")

        json_data = df.to_json(orient=orient_option, indent=indent_level)

        # Validate JSON by loading and dumping again
        try:
            parsed_json = json.loads(json_data)
            valid_json = json.dumps(parsed_json, indent=indent_level)
            st.code(valid_json, language="json")
            st.download_button("Download JSON", valid_json, file_name="converted.json", mime="application/json")
            st.success("JSON is valid and ready for use in AJAX.")
        except json.JSONDecodeError as e:
            st.error(f"JSON validation error: {e}")
    except Exception as e:
        st.error(f"Failed to process CSV: {e}")
