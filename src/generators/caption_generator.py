from models.model import ImageCaptioningModel

class CaptionGenerator():
    """Class to generate caption using the image captioning model."""

    def __init__(self, model: ImageCaptioningModel) -> None:
        
        self.model = model

    
    def generate(self, image) -> str:
        """
        Generate a caption for the provided image.

        Args:
            image: The input image for caption generation.

        Returns:
            str: The generated caption.
        """

        return self.model.generate_caption(image=image)