FROM nvidia/cuda:11.7.1-base-ubuntu20.04

WORKDIR /app

# Set environment variable to suppress interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install Python 3.9 and other system dependencies
RUN apt-get update && apt-get install -y \
    software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && apt-get install -y \
    python3.9 \
    python3.9-venv \
    python3.9-dev \
    python3-pip \
    wget \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && apt-get clean

# Ensure pip for Python 3.9 is installed
RUN python3.9 -m ensurepip --upgrade

# Set Python 3.9 as the default python3
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 2

# Ensure pip is up-to-date
RUN python3.9 -m pip install --upgrade pip

# Download and install Marker
RUN wget https://github.com/VikParuchuri/marker/archive/refs/tags/v0.2.16.tar.gz \
    && tar -xzvf v0.2.16.tar.gz \
    && cd marker-0.2.16 \
    && python3.9 -m pip install .

# Copy application code
COPY requirements.txt .
RUN python3.9 -m pip install -r requirements.txt

COPY convert_pdf_to_md.py .
COPY .env .

# Ensure the dotenv file is copied
RUN touch .env

# Run the application
CMD ["python3", "convert_pdf_to_md.py"]
