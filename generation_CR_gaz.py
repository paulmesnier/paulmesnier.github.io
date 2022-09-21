import streamlit as st
from test_placid import send_request
from PIL import Image

image = Image.open('papernest.png')
col1, col2,col3 = st.columns(3)
with col3 :
    st.image(image)
st.title("🔥 Gas Report Generation")
form = st.sidebar.form("duplicatas_form",clear_on_submit=False)
form.write("**Complete those informations to compute the report**")
input_client_name = form.text_input(label = 'Client Name', key='client_name')
input_supplier_name = form.text_input(label = 'Supplier Name', key='supplier_name')
validate = form.form_submit_button()

if validate :
    pdf_display = send_request(input_supplier_name)
    st.markdown(pdf_display, unsafe_allow_html=True)

