import streamlit as st
from PIL import Image
import tempfile
from ocr_module import perform_ocr
import re

def highlight_keywords(text, keywords):
    # Escape keywords for regex
    escaped_keywords = [re.escape(word) for word in keywords]
    pattern = re.compile(r'(' + '|'.join(escaped_keywords) + r')', re.IGNORECASE)
    # Replace with HTML highlight
    highlighted_text = pattern.sub(r'<mark>\1</mark>', text)
    return highlighted_text

def main():
    st.set_page_config(page_title="Multilingual OCR App", layout="wide")
    st.title("📄 Multilingual OCR Web Application")
    st.write("Upload an image containing Hindi and English text to extract and search keywords.")

    # File uploader
    uploaded_file = st.file_uploader("📤 Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        try:
            # Open the image with PIL to check if it is valid
            image = Image.open(uploaded_file)

            # Create two columns for layout optimization
            col1, col2 = st.columns(2)

            with col1:
                st.image(image, caption='Uploaded Image', use_column_width=True)

            with col2:
                # Save the uploaded file to a temporary file
                with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
                    tmp_file.write(uploaded_file.getvalue())
                    temp_file_path = tmp_file.name

                # Perform OCR with a progress spinner
                with st.spinner('🔍 Performing OCR...'):
                    ocr_result = perform_ocr(temp_file_path)

                extracted_text = ocr_result['extracted_text']
                st.subheader("📝 Extracted Text")
                st.text_area("Text", extracted_text, height=300)

                # Keyword Search
                st.subheader("🔑 Keyword Search")
                keywords_input = st.text_input("Enter keywords separated by commas (e.g., hello, world)")

                if st.button("Search"):
                    if keywords_input.strip() == "":
                        st.warning("⚠️ Please enter at least one keyword.")
                    else:
                        keyword_list = [word.strip() for word in keywords_input.split(',') if word.strip() != ""]
                        if not keyword_list:
                            st.warning("⚠️ Please enter valid keywords.")
                        else:
                            highlighted = highlight_keywords(extracted_text, keyword_list)
                            st.markdown("**Search Results:**")
                            st.markdown(highlighted, unsafe_allow_html=True)  # Allow HTML rendering

        except Exception as e:
            st.error(f"❌ An error occurred during OCR processing: {e}")

if __name__ == "__main__":
    main()
