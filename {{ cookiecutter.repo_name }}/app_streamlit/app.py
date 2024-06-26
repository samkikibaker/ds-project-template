import streamlit as st
import os
from PIL import Image
from {{ cookiecutter.package_name }}.utils.util import yaml2dict, set_hl_styles

import warnings

warnings.filterwarnings("ignore")
st.set_page_config(layout="wide")

conf = yaml2dict("conf/parameters.yaml")
colors = conf["hl_colors"]

if os.path.exists(os.path.join(os.getcwd(), "app_streamlit", "style.css")):
    set_hl_styles("app_streamlit/style.css")
elif os.path.exists(os.path.join(os.getcwd(), "style.css")):
    set_hl_styles("style.css")
else:
    print("Failed to load Hoare Lea styles.")

def main():
    logo = Image.open("assets/Hoare-Lea-logo-scaled.jpg")
    st.image(logo, width=600)
    st.title("{{cookiecutter.project_name}}")
    st.divider()

if __name__ == "__main__":
    main()
