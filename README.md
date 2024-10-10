# Image Captioning Project

This project utilizes Hugging Face's models to generate captions for images. It is built using Python, Poetry for dependency management, and Gradio for creating a user interface.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Requirements](#requirements)
- [Installation Instructions](#installation-instructions)
- [License](#license)

## Overview

This application is a powerful and user-friendly tool designed to generate captions for images using advanced AI models. Built on the Hugging Face framework, this application leverages the power of Python and Gradio to provide an intuitive interface for users to upload images and receive descriptive captions.

## Technologies Used

- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index) for model handling
- [Gradio](https://gradio.app/) for building the user interface
- [Poetry](https://python-poetry.org/) for dependency management
- [Python](https://www.python.org/) as the programming language

## Features

- Upload images and receive AI-generated captions
- User-friendly web interface for interaction
- Easy-to-extend architecture for future enhancements

## Requirements

- Python 3.12 or later
- Poetry for managing dependencies
- Hugging Face account (for accessing models)

## Installation Instruction: 

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Scherzo8/Image-Captioning.git
   cd Image-Captioning
   ```
2. **Install dependencies:**
    ```bash
    poetry install
    ```

3. **Log in to Hugging Face:**  
    
    You need to have a Hugging Face account and generate an access token.

    ```bash
    huggingface-cli login
    ```
4. **Run the application:** 
    ```bash
    poetry run python3 src/main.py
    ```
    
    Once the server is running, open your web browser and navigate to `http://localhost:7860` to access the Gradio interface.
    
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

