def build_story_prompt(theme):
    return f"Write a short, imaginative, and age-appropriate story for kids about '{theme}'."

def build_image_prompt(story, element=None):
    base = f"An illustration for the story: {story[:200]}..."  # Truncate to avoid long prompts
    if element:
        base += f" Include a {element}."
    return base + " Style: cartoon, colorful, watercolor, 4:3 aspect ratio"
