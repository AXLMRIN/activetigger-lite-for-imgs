import streamlit as st 
from utils import current_image

# Body =======================================

st.header("ActiveTigger — lite for images")

st.write("## Parameters")

img_width = st.number_input(
    label = "Image width", 
    min_value=200, 
    max_value= 500, 
    step = 50
)

st.write(f"Your labels: {" / ".join(current_image.available_labels)}")

st.write("## Annotation")

st.write(f"Image number {current_image.current_index} out of {current_image.max_value}")

cols_control = st.columns([0.1, 0.6, 0.2, 0.1], vertical_alignment="bottom")

active_label = cols_control[1].selectbox(
    label = "Label", 
    options = current_image.available_labels, 
)

cols_control[0].button(
    label = "", 
    on_click=current_image.previous, 
    key="previous", 
    icon=":material/arrow_back:", 
    use_container_width=True,
    
)

cols_control[2].button(
    label = "Save", 
    on_click=current_image.save_label,
    type="primary",
    args=[active_label],
    use_container_width=True,
)

cols_control[3].button(
    label = "", 
    on_click=current_image.next, 
    key="next", 
    icon=":material/arrow_forward:", 
    use_container_width=True,
)

if current_image.label is None: 
    st.write("Current label: **None**")
else:
    st.write(f"Current label: **{current_image.label}**")

st.image(
    f"./img/{current_image.image_name}", 
    caption= current_image.image_name,
    width = img_width
)