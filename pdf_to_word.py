import os
import argparse
import fitz  # PyMuPDF
from docx import Document

def convert_pdf_to_word(pdf_file):
    word_file = os.path.splitext(pdf_file)[0] + '.docx'
    
    # Open the PDF file
    pdf_document = fitz.open(pdf_file)
    
    # Create a new Word document
    doc = Document()
    
    # Iterate through each page
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text = page.get_text()
        doc.add_paragraph(text)
    
    # Save the Word document
    doc.save(word_file)
    print(f'Converted {pdf_file} to {word_file}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert PDF to Word')
    parser.add_argument('pdf_file', type=str, help='Path to the PDF file to be converted')
    args = parser.parse_args()

    convert_pdf_to_word(args.pdf_file)
