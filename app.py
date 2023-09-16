import streamlit as st 
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from lib.utils import * 
from lib.uu import *
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
st.header("Breast-cancer Segmentation")
st.write("""Breast-Cancer Segmentation using a fine-tuned Segment Anything Model (SAM)
            called Breast-Cancer_SAM_v1 https://huggingface.co/ayoubkirouane/Breast-Cancer_SAM_v1 
            is a project that aims to develop a fine-tuned SAM model for the segmentation of breast
            cancer tumors in medical images. The project uses the Breast Cancer Segmentation Dataset 
            (BCSD), which is a publicly available dataset of breast cancer images with corresponding 
            segmentation masks.""")
image_up = st.file_uploader("Upload your file")
if image_up :
    if st.button("Get input Boxe") :
        input_boxes = main(image_up.name) 
        st.write("Your will segment this part of your input image")
        if st.button("Start Segmentation ") : 
            with st.spinner("This process may take some time..") : 
                img_name = image_up.name
                image = Image.open(img_name).convert("RGB") 
                run_sam(input_boxes ,device ,image , img_name ) 
                st.image(f"results/{img_name}_result.png")

