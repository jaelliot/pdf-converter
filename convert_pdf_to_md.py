import os
import time
import logging
import subprocess
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set environment variables for marker
os.environ['TORCH_DEVICE'] = 'cuda'
os.environ['INFERENCE_RAM'] = '16'
os.environ['OCR_ENGINE'] = 'surya'
os.environ['DEFAULT_LANG'] = 'English'

def convert_pdf_to_md(input_pdf, output_md):
    command = [
        'marker_single', input_pdf, output_md,
        '--batch_multiplier', '2', 
        '--langs', 'English'
    ]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        logging.info(f"Command output: {result.stdout}")
        logging.info(f"Successfully converted {input_pdf} to {output_md}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to convert {input_pdf} to {output_md}: {e}")
        logging.error(f"Command stderr: {e.stderr}")

def process_pdfs(input_dir, output_dir):
    logging.info(f"Checking for PDF files in {input_dir}")
    for filename in os.listdir(input_dir):
        if filename.endswith('.pdf'):
            input_pdf = os.path.join(input_dir, filename)
            output_md = os.path.join(output_dir, filename.replace('.pdf', '.md'))
            logging.info(f"Found PDF: {input_pdf}")
            convert_pdf_to_md(input_pdf, output_md)
            logging.info(f"Checking if the output file {output_md} was created")
            if os.path.exists(output_md):
                logging.info(f"Output file {output_md} created successfully.")
            else:
                logging.error(f"Output file {output_md} was not created.")

def main():
    input_dir = '/mnt/d/file-converter/input'
    output_dir = '/mnt/d/file-converter/output'

    # Check if directories exist
    if not os.path.exists(input_dir):
        logging.error(f"Input directory does not exist: {input_dir}")
        return

    if not os.path.exists(output_dir):
        logging.error(f"Output directory does not exist: {output_dir}")
        return

    logging.info(f"Starting the PDF to Markdown conversion service...")
    logging.info(f"Input directory: {input_dir}")
    logging.info(f"Output directory: {output_dir}")

    while True:
        try:
            process_pdfs(input_dir, output_dir)
        except Exception as e:
            logging.error(f"Error during processing: {e}")
        time.sleep(60)  # Wait for 60 seconds before checking again

if __name__ == "__main__":
    main()
