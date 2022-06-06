import streamlit as st
from PIL import Image
st.set_page_config(page_title="宋梦装逼专用网站",    #页面标题
    page_icon=":rainbow:",        #icon
    layout="wide",                #页面布局
    initial_sidebar_state="auto"  )
st.write("希望梦公子越长越帅！")

image = Image.open('2.jpg')
st.image(image, caption='Sunrise by the mountains',use_column_width=True)
