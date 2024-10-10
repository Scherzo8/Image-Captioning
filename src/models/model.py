from transformers import BlipProcessor, BlipForConditionalGeneration
from config import Config

class ImageCaptioningModel():
    """Class for loading and running inference for captioning model."""

    def __init__(self) -> None:
        
        self.processor = BlipProcessor.from_pretrained(Config.MODEL_NAME)
        self.model = BlipForConditionalGeneration.from_pretrained(Config.MODEL_NAME)

    
    def generate_caption(self, image) -> str:
        """
        Generate a caption for the given image.
        
        Args:
            image: Input image for captioning.
        
        Returns:
            str: The generated caption.
        """
        inputs = self.processor(images=image, return_tensors="pt")
        output = self.model.generate(**inputs, max_length=Config.MAX_CAPTION_LENGTH)
        
        caption = self.processor.decode(output[0], skip_special_tokens=True)

        return caption