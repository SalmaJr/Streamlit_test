import streamlit as st
st.title("This is the app title")
st.header("This is the header")
st.markdown("This is the markdown")
st.subheader("This is the subheader")
st.caption("This is the caption")
st.sidebar.title("EMC2")
st.sidebar.image('https://jamiati.ma/sites/default/files/styles/jamiati_card_logo_mobile_2x/public/jamiati-organization/ehtp-1.png?timestamp=1573738706')
app_type = st.sidebar.selectbox('Select APP Type', ['--- Select a type ---', 'Image analysis', 'OCR', 'Thumbnail imane', 'Face analysis'])

match app_type:
    case 'Image analysis':
         image_file = st.file_uploader()
    case _:
        print("pls choose")