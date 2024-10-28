import yaml
{% if cookiecutter.include_streamlit_app.lower() in ['yes', 'y'] -%}
import numpy as np
import streamlit as st
import plotly.graph_objects as go
import plotly.io as pio
from typing import Iterable
{% endif %}

def yaml2dict(fpath: str) -> dict:
    """Opens yaml file at fpath and returns content as dict"""
    content = yaml.safe_load(open(fpath))
    return content


{% if cookiecutter.include_streamlit_app.lower() in ['yes', 'y'] -%}
hl_colors = [
    "#343334",
    "#d02e6f",
    "#e3ed64",
    "#b5d1c0",
    "#7aaabe",
    "#9b8dc6",
    "#5d5c5d",
    "#f1f6b1",
    "#cbdfd3",
    "#aac9d3",
    "#c1a5d7",
    "#858485",
]


def set_hl_styles(style_fpath: str = "style.css", colors: Iterable = hl_colors) -> None:
    """Sets streamlit css and plotly templates to Hoare Lea styles"""
    hl_template = dict(
        layout=go.Layout(
            title=dict(pad=dict(l=0, r=0, t=10, b=0), x=0.0),
            font=dict(family="Lato"),
            title_font=dict(family="Grueber", size=22),
            colorway=colors,
            margin=dict(l=0, r=0, t=50, b=40),
        )
    )
    fig = go.Figure()
    fig.update_layout(title="", template=hl_template)
    pio.templates["hoare_lea"] = fig.layout.template
    pio.templates.default = "plotly+hoare_lea"

    with open(style_fpath) as css:
        st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)


def get_rand_colors(seed: int = None, repeat: int = 1):
    """Generates a colour scheme using random order of default plotly colours"""
    np.random.seed(seed)
    cols = pio.templates[pio.templates.default].layout.colorway

    return list(np.random.choice(cols, len(cols), replace=False)) * repeat
{% endif -%}