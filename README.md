

```markdown
# 🌍 Multilingual OCR Web Application

## Overview
This web application allows users to upload images containing Hindi and English text and extracts the text using Optical Character Recognition (OCR). Users can also search for specific keywords within the extracted text, and matching keywords are highlighted.

## Features
- 📸 **Image Upload:** Users can upload images in JPG, JPEG, or PNG formats.
- 📝 **Text Extraction:** Uses EasyOCR to extract text from uploaded images.
- 🔍 **Keyword Search:** Enter keywords to highlight matches in the extracted text.
- 📱 **Responsive Layout:** Organized layout for better readability.

## Tech Stack
- **Frontend:** Streamlit
- **OCR Library:** EasyOCR
- **Image Handling:** PIL (Python Imaging Library)
- **Python Version:** Ensure Python 3.7 or higher is installed.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ocr_web_app.git
   cd ocr_web_app
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv ocr_env
   source ocr_env/bin/activate  # On Windows use `ocr_env\Scripts\activate`
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To run the application locally, execute the following command:

```bash
streamlit run app.py
```

Then open your web browser and go to `http://localhost:8501` to view the app. 🚀

## Deployment

This application can be easily deployed on Streamlit Community Cloud. Follow these steps:

1. Create a GitHub repository and push your code.
2. Sign in to Streamlit Community Cloud using your GitHub account.
3. Click on "New app" and select your repository, branch, and `app.py`.
4. Click "Deploy".

## Usage

1. 📤 **Upload** an image containing Hindi and English text.
2. ⏳ **Wait** for the OCR process to complete.
3. 🔑 **Enter keywords** in the provided text box and click "Search" to highlight matches.

## Troubleshooting

- ⚠️ Ensure all required libraries are listed in `requirements.txt`.
- 🖼️ Check for supported image formats.
- ❓ If you encounter issues with OCR, verify that the image quality is sufficient for text recognition.

## Contributing

🤝 Feel free to fork the repository and submit pull requests for any improvements or features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- 🎉 [EasyOCR](https://github.com/JaidedAI/EasyOCR) for OCR functionality.
- 🌟 [Streamlit](https://streamlit.io/) for building the web app.
```

### Notes:
- Replace `yourusername` in the clone command with your actual GitHub username.
- Feel free to adjust emojis or text as per your preferences!