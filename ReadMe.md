# PDF to Word Converter

This script converts PDF files to Word documents using Python. It provides a command-line interface (CLI) that allows you to pass the file name as a command-line argument and outputs the converted file in the same directory with the same name.

## Features

- Converts PDF files to Word documents (.docx).
- Maintains the same file name and directory for the output file.
- Easy to use via command-line interface.

## Requirements

- Python 3.x
- `pdf2docx` library
- `argparse` library (part of the Python standard library)

## Installation

1. Clone the repository or download the script.

2. Install the required libraries:

    ```bash
    pip install pdf2docx
    ```

## Usage

1. Save the script as `pdf_to_word.py`.

2. Open your command line or terminal.

3. Run the script with the path to the PDF file you want to convert:

    ```bash
    python pdf_to_word.py path/to/your/file.pdf
    ```

   For example:

    ```bash
    python pdf_to_word.py example.pdf
    ```

   This will convert `example.pdf` to `example.docx` and save it in the same directory.

## Example

### Input

- `example.pdf`

### Command

```bash
python pdf_to_word.py example.pdf
