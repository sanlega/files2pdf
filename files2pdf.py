import os
import argparse
from fpdf import FPDF

def extract_text(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except:
        print(f"Error reading file: {file_path}")
        return ""

def traverse_directory(dir_path, pdf):
    for root, dirs, files in os.walk(dir_path):
        if '.git' in dirs:
            dirs.remove('.git')  # this will prevent os.walk from traversing this directory
        for file in files:
            file_path = os.path.join(root, file)
            text = extract_text(file_path)
            if text:
                pdf.add_page()
                pdf.set_font('Arial', 'B', 16)  # Set font for title
                pdf.cell(0, 10, file_path, ln=True)
                pdf.set_font('Arial', '', 12)  # Set font for file content
                pdf.multi_cell(0, 10, text)

def create_pdf(dir_path, pdf_path):
    pdf = FPDF()
    traverse_directory(dir_path, pdf)
    pdf.output(pdf_path, 'F')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('dir_path', help='Directory path to traverse')
    parser.add_argument('pdf_path', help='Output PDF file name')
    args = parser.parse_args()

    create_pdf(args.dir_path, args.pdf_path)

if __name__ == "__main__":
    main()
