# Directory to PDF Converter 📁 ➡️ 📄

This Python script traverses a directory and converts all the text files found into a PDF. 

## 💼 Usage

```
python script.py <dir_path> <pdf_path>
```
Here,
- `dir_path`: Directory path to traverse. The script will look for text files in this directory and its subdirectories.
- `pdf_path`: The output PDF file name.

## 📜 Description

The script performs the following tasks:
- Traverse the directory and its subdirectories using os.walk
- For each file found, the text is extracted and written into a PDF. The file path is used as a title for each page in the PDF.
- The '.git' directories are excluded from traversal.

## 🧩 Features

1. Skip `.git` directories during directory traversal.
2. Dynamic font setting for title and file content.

## 📚 Dependencies

You'll need the following python libraries: 

- os
- argparse
- fpdf

You can install the `fpdf` library using pip: 

```
pip install fpdf
```

## ⚙️ How it Works

The script's main function `main()` takes two arguments from the command line: `dir_path` and `pdf_path`. It passes these arguments to the `create_pdf()` function which creates a `FPDF` object, traverses the directory by calling `traverse_directory()`, and saves the created PDF.

The `traverse_directory()` function recursively walks through the directory and its subdirectories. For each file it finds, it reads the file content with `extract_text()`, adds a new page to the PDF, sets the title as the file's path, and writes the file content to the PDF.

## 🚀 Getting Started

Clone this repository, install the required python libraries and you're good to go! 😃

```bash
git clone <repo_url>
cd <repo_folder>
pip install fpdf
python script.py <dir_path> <pdf_path>
```

## 🐞 Bug Reports & Feature Requests

Feel free to open an issue if you've found a bug or have a feature request.

## 💖 Contributions

All contributions are welcome! Please feel free to make a pull request.

## ⚖️ License

This project is licensed under the MIT License.
