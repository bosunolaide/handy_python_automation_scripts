import fitz  # PyMuPDF

def pdf_to_images(pdf_file, output_folder):
    """
    Converts each page of a PDF file to an image (PNG).

    :param pdf_file: Path to the PDF file.
    :param output_folder: Path to the output folder where images will be saved.
    """
    # Open the PDF file
    pdf_document = fitz.open(pdf_file)
    
    # Iterate through each page of the PDF
    for page_num in range(len(pdf_document)):
        # Get the page
        page = pdf_document.load_page(page_num)
        
        # Convert page to image (PNG)
        image = page.get_pixmap()
        
        # Save image to output folder
        image_path = f"{output_folder}/page_{page_num + 1}.png"
        image.save(image_path)
        print(f"Page {page_num + 1} saved as {image_path}")
    
    # Close the PDF document
    pdf_document.close()

# Example usage
if __name__ == "__main__":
    pdf_file = "example.pdf"  # Replace with your PDF file path
    output_folder = "output_images"  # Replace with your desired output folder
    
    # Create output folder if it doesn't exist
    import os
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Convert PDF to images
    pdf_to_images(pdf_file, output_folder)