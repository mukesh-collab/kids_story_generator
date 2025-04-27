# Kids Story Generator

A Python project that generates creative and engaging poems or stories for kids based on a user-provided theme or topic. The generated content can be exported as a PDF file for easy sharing or printing.

## Features
- **AI-Generated Stories**: Uses OpenAI's GPT model to create unique and imaginative stories or poems.
- **Theme-Based Generation**: Input a theme or topic, and the application generates content tailored to it.
- **PDF Export**: Save the generated content as a downloadable PDF file.
- **User-Friendly Interface**: Built using Streamlit for a simple and interactive user experience.

## Project Structure

## git clone https://github.com/mukesh-collab/kids_story_generator.git
cd kids_story_generator

streamlit run main.py

### Environment Variables
Create a `.env` file in the root directory with the following keys:


```plaintext
kids_story_generator/
├── assets/                 # Directory for storing generated PDFs
├── fonts/                  # Directory for custom fonts (optional)
├── prompts/                # Contains prompt builder modules
│   └── prompt_builder.py
├── generator/              # Contains the story generator logic
│   └── story_generator.py
├── main.py                 # Main application file (Streamlit app)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

pip install -r requirements.txt



