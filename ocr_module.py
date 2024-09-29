import easyocr
import json
import numpy as np  # Needed to handle int32

def perform_ocr(image_path):
    # Initialize the reader with Hindi and English languages
    reader = easyocr.Reader(['en', 'hi'], gpu=False)  # Set gpu=True if CUDA is available
    
    # Perform OCR on the image
    try:
        results = reader.readtext(image_path)
    except Exception as e:
        raise ValueError(f"Failed to read the image: {e}")
    
    # Check if any text was detected
    if not results:
        raise ValueError("No text detected in the image.")
    
    # Extract the text
    extracted_text = " ".join([res[1] for res in results])
    
    # Structure the results
    structured_output = {
        "extracted_text": extracted_text,
        "details": results  # Contains bounding boxes and confidence scores
    }
    
    return structured_output

# Custom JSON encoder to handle non-serializable types like int32
def convert_non_serializable(obj):
    if isinstance(obj, np.int32):
        return int(obj)
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

if __name__ == "__main__":
    # For testing purposes
    image_path = 'img_3.png'  # Ensure you have a sample image in the same directory
    try:
        ocr_result = perform_ocr(image_path)
        
        # Use the custom encoder during JSON serialization
        print(json.dumps(ocr_result, ensure_ascii=False, indent=4, default=convert_non_serializable))
    except Exception as e:
        print(f"An error occurred: {e}")
