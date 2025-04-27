from prompts.prompt_builder import build_story_prompt, build_image_prompt
from generator.story_generator import generate_story
from generator.image_generator import generate_image
from utils.display import display_image_from_url, save_image_from_url

from PIL import Image

theme = input("🎨 Enter a story theme (e.g., magical forest, friendly dragon): ")
element = input("🌟 Optional: Any specific element to include in the image (e.g., girl, moon): ")

story_prompt = build_story_prompt(theme)
story = generate_story(story_prompt)
print("\n📝 Here's your generated story:\n")
print(story)

image_prompt = build_image_prompt(story, element)

try:
    image_url = generate_image(image_prompt)
    save_image_from_url(image_url)
    display_image_from_url(image_url)
except Exception as e:
    print(f"⚠️ Image generation failed: {e}")
    try:
        image = Image.open("assets/generated_image.png")
        image.show()
    except Exception as fallback_error:
        print(f"⚠️ Failed to load local placeholder image: {fallback_error}")
