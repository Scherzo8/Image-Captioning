import gradio as gr
from generators.caption_generator import CaptionGenerator

def create_interface(caption_generator: CaptionGenerator):
    """
    Create a Gradio interface for the caption generator.

    Args:
        caption_generator (CaptionGenerator): The caption generator instance.
    """

    def predict(image):

        return caption_generator.generate(image)
    
    gr.Interface(fn=predict, inputs="image", outputs="text").launch()