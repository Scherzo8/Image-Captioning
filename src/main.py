from models.model import ImageCaptioningModel
from generators.caption_generator import CaptionGenerator
from interface.gradio_interface import create_interface

model = ImageCaptioningModel()
caption_generator = CaptionGenerator(model=model)
create_interface(caption_generator=caption_generator)