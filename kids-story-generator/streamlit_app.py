import base64
import os
import streamlit as st
from fpdf import FPDF
from prompts.prompt_builder import build_story_prompt
from generator.story_generator import generate_story
import unicodedata


# Normalize function to remove problematic characters
def normalize_text(text):
    return unicodedata.normalize('NFKD', text).encode('latin-1', 'ignore').decode('latin-1')


# PDF Generator
class PDF(FPDF):
    def header(self):
        # Using Helvetica to avoid font substitution warnings
        self.set_font("Helvetica", "B", 12)
        self.cell(0, 10, "Kids Poem/Story", align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def add_content(self, title, content):
        self.add_page()
        self.set_font("Helvetica", "B", 14)
        self.cell(0, 10, title)
        self.ln(10)
        self.set_font("Helvetica", "", 12)
        self.multi_cell(0, 10, content)


# Streamlit UI
st.title("Kids Poem/Story Generator with PDF Output")

# User Inputs
theme = st.text_input("Enter the theme or topic for your poem/story", "A magical forest")
generate_btn = st.button("Generate Poem/Story")

if generate_btn:
    try:
        # Generate poem/story using existing functions
        story_prompt = build_story_prompt(theme)
        story = generate_story(story_prompt)

        # Display the generated content
        st.subheader("Generated Poem/Story")
        st.write(story)

        # Normalize story text to handle non-ASCII characters
        normalized_story = normalize_text(story)

        # Ensure the 'assets' directory exists
        output_folder = "assets"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Format theme to create a valid file name
        theme_filename = theme.lower().replace(" ", "_")
        pdf_filename = f"{theme_filename}.pdf"

        # Define the path to save the PDF in the 'assets' folder
        pdf_output_path = os.path.join(output_folder, pdf_filename)

        # Generate PDF
        pdf = PDF()
        pdf.add_content(f"Poem/Story about {theme}", normalized_story)
        pdf.output(pdf_output_path)

        # Provide PDF download
        with open(pdf_output_path, "rb") as file:
            b64 = base64.b64encode(file.read()).decode()
            href = f'<a href="data:application/octet-stream;base64,{b64}" download="{pdf_filename}">Download the Poem/Story as PDF</a>'
            st.markdown(href, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"An error occurred: {e}")
