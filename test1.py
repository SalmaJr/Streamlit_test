import streamlit as st
st.title("Module 7 - AI")
st.header("StreamLit Test")
st.sidebar.title("EMC2")
st.sidebar.image('https://jamiati.ma/sites/default/files/styles/jamiati_card_logo_mobile_2x/public/jamiati-organization/ehtp-1.png?timestamp=1573738706')
app_type = st.sidebar.selectbox('Select APP Type', ['--- Select a type ---', 'Image analysis', 'OCR', 'Thumbnail imane', 'Face analysis'])

match app_type:
    case 'Image analysis':
        image_file = st.file_uploader('upload a photo')
    case _:
        st.caption("please choose an app type")