### `README.md`

```markdown
# PDF to Markdown Converter

This project is a Dockerized application that converts PDF files to Markdown format using the Marker tool. The application leverages GPU acceleration for efficient processing and is configured to run continuously, monitoring a specified directory for new PDF files to convert.

## Features

- Converts PDF files to Markdown format.
- Uses GPU acceleration for faster processing.
- Continuously monitors a directory for new PDF files.
- Configurable via environment variables.

## Prerequisites

- Docker
- NVIDIA GPU with CUDA support
- NVIDIA Container Toolkit

## Setup

### Clone the Repository

```sh
git clone git@github.com:jaelliot/pdf-converter.git
cd pdf-converter
```

### Create `.env` File

Create a `.env` file in the project root to store your environment variables.

```plaintext
# .env file example
# Add your specific environment variables here
```

### .gitignore and .dockerignore

Ensure that the `.env` file and other sensitive information are not tracked by Git and Docker by including them in the `.gitignore` and `.dockerignore` files.

### Build the Docker Image

```sh
docker build -t yourusername/pdf-to-md-converter:latest .
```

### Run the Docker Container

```sh
docker run --gpus all --env-file .env -v /mnt/d/file-converter:/mnt/d/file-converter -d yourusername/pdf-to-md-converter:latest
```

## Environment Variables

The application uses environment variables for configuration. These can be set in the `.env` file.

- `TORCH_DEVICE`: Specify the torch device (e.g., `cuda`).
- `INFERENCE_RAM`: Set the VRAM per GPU (e.g., `16` for 16 GB of VRAM).
- `OCR_ENGINE`: Set the OCR engine (`surya` or `ocrmypdf`).
- `DEFAULT_LANG`: Default language for OCR (e.g., `English`).

## Usage

The application continuously monitors the `/mnt/d/file-converter/input` directory for new PDF files. When a new PDF is detected, it converts the PDF to Markdown format and saves the output in the `/mnt/d/file-converter/output` directory.

### Convert a Single File

```sh
marker_single /path/to/file.pdf /path/to/output.md --batch_multiplier 2 --langs English
```

### Convert Multiple Files

```sh
marker /path/to/input/folder /path/to/output/folder --workers 10 --max 10 --metadata_file /path/to/metadata.json --min_length 10000
```

## Troubleshooting

- Ensure the GPU is properly configured and accessible by Docker.
- Check the Docker logs for any errors or issues during the conversion process.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## Contact

For questions or feedback, please contact [jaelliot](https://github.com/jaelliot).

---

*This project is hosted on [GitHub](https://github.com/jaelliot/pdf-converter) and available as a Docker image on [DockerHub](https://hub.docker.com/r/yourusername/pdf-to-md-converter).*
```
