import streamlit as st

from app_core import read_csv, show_certificates, send_all_emails

st.set_page_config(page_title="Certificate Automation", page_icon="🎓", layout="wide")

st.title("🎓 Certificate Automation Tool")

# Sidebar for instructions
with st.sidebar:
    st.header("Instructions")
    st.markdown("""
    1. Upload a CSV file with two columns: `Name` and `Email`
    2. Preview the uploaded data on the main page
    3. Review the generated certificates below the data preview
    4. Click the **Send to All** button to email certificates to participants
    5. Watch the progress bar while sending emails
    6. If errors occur, they will be displayed on the page
    """)

# Layout columns for uploader and preview
col1, col2 = st.columns([3, 1])

with col1:
    uploaded_file = st.file_uploader("Upload CSV file (Name and Email)", type=["csv"], key="csv_uploader")
    if uploaded_file:
        df = read_csv(uploaded_file)
        if df.empty:
            st.warning("Uploaded CSV is empty! Please check your file.")
        else:
            st.write("Here is a preview of your data:")
            st.dataframe(df)
            show_certificates(df, st)
            if st.button("Send to All"):
                send_all_emails(df, st)
    else:
        st.info("Please upload a CSV file to get started.")

with col2:
    st.image("certificate_template.png", caption="Certificate Template Preview",  use_container_width=True)






