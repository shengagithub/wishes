import streamlit as st
from PIL import Image
st.write("希望我的吴珊媚开心快乐每一天，每天都有惊喜！")

image = Image.open('1.jpg')
st.image(image, caption='Sunrise by the mountains',use_column_width=True)
