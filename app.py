import streamlit as st
from PIL import Image

def resize_image(image, width, height):
    return image.resize((width, height), Image.Resampling.LANCZOS)

# App Title
st.title("Image Resizer App")
st.text("Upload an image to resize it to your desired dimensions.")

# File Uploader
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Load the image
    img = Image.open(uploaded_file)
    st.image(img, caption="Original Image", use_column_width=True)

    # Input fields for resizing dimensions
    st.write("### Resize Options")
    col1, col2 = st.columns(2)
    with col1:
        width = st.number_input("Width", min_value=1, value=img.width)
    with col2:
        height = st.number_input("Height", min_value=1, value=img.height)

    # Resize button
    if st.button("Resize"):
        resized_img = resize_image(img, int(width), int(height))
        st.image(resized_img, caption="Resized Image", use_column_width=True)

        # Download the resized image
        st.write("### Download Resized Image")
        resized_img_buffer = st.download_button(
            label="Download Image",
            data=resized_img.tobytes(),
            file_name="resized_image.jpg",
            mime="image/jpeg"
        )
