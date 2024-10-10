from PIL import Image

def preprocess_image(image_path: str) -> str:
    """
    Load and preprocess the image for model input.

    Args:
        image_path (str): Path to the image file.

    Returns:
        Image: Preprocessed PIL Image.
    """

    return Image.open(image_path).convert("RGB")
