import streamlit as st
from googletrans import Translator, LANGUAGES
from langchain_core.prompts import PromptTemplate
import PyPDF2

class LanguageTranslationChatbotStreamlit:
    def __init__(self):
        self.translator = Translator()
        self.prompt_template = PromptTemplate(
            input_variables=["text", "src_lang", "dest_lang"],
            template="Translate the following text from {src_lang} to {dest_lang}: {text}"
        )

    def translate_text(self, text, src_lang='auto', dest_lang='en'):
        result = self.translator.translate(text, src=src_lang, dest=dest_lang)
        return result.text

    def create_translation_prompt(self, text, src_lang, dest_lang):
        prompt = self.prompt_template.format(text=text, src_lang=src_lang, dest_lang=dest_lang)
        return prompt

    def extract_text_from_pdf(self, pdf_file):
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        text = ""
        for page_num in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            text += page.extract_text()
        return text

    def run(self):
        # Custom CSS for blue theme and cool designs
        st.markdown("""
            <style>
                .main {
                    background-color: #e0f7fa;
                }
                .stTextInput, .stButton, .stSelectbox, .stTextArea {
                    border-radius: 10px;
                    padding: 10px;
                }
                .stTextInput, .stSelectbox, .stTextArea {
                    background-color: #ffffff;
                }
                .stButton {
                    background-color: #0288d1;
                    color: white;
                }
                .stTextArea {
                    background-color: #e1f5fe;
                }
                h1 {
                    color: #01579b;
                }
                .translate-button {
                    display: block;
                    width: 100%;
                    text-align: center;
                    margin: 10px 0;
                    padding: 10px;
                    border: none;
                    border-radius: 10px;
                    background-color: #0288d1;
                    color: white;
                    font-size: 16px;
                    cursor: pointer;
                }
                .translate-button:active {
                    background-color: #01579b;
                }
            </style>
        """, unsafe_allow_html=True)

        st.title("Language Translation Chatbot")

        # Input text
        input_text = st.text_input("Enter text to translate:")

        # File uploader
        uploaded_file = st.file_uploader("Upload a PDF or text file", type=["pdf", "txt"])

        # Language selections
        src_lang = st.selectbox("Select source language:", list(LANGUAGES.values()), index=list(LANGUAGES.values()).index("english"))
        dest_lang = st.selectbox("Select destination language:", list(LANGUAGES.values()), index=list(LANGUAGES.values()).index("hindi"))

        if uploaded_file is not None:
            if uploaded_file.type == "application/pdf":
                text_to_translate = self.extract_text_from_pdf(uploaded_file)
            elif uploaded_file.type == "text/plain":
                text_to_translate = uploaded_file.read().decode("utf-8")
            else:
                st.error("Unsupported file type")
                return

            st.text_area("Extracted Text:", value=text_to_translate, height=200)

            if st.button("Translate File", key="translate_file"):
                if src_lang and dest_lang:
                    translated_text = self.translate_text(text_to_translate, src_lang, dest_lang)
                    translation_prompt = self.create_translation_prompt(text_to_translate, src_lang, dest_lang)
                    st.text_area("Translation Prompt:", value=translation_prompt, height=100)
                    st.text_area("Translation Result:", value=translated_text, height=200)
                else:
                    st.error("Please select both source and destination languages.")

        if input_text and st.button("Translate Text", key="translate_text"):
            if src_lang and dest_lang:
                translated_text = self.translate_text(input_text, src_lang, dest_lang)
                translation_prompt = self.create_translation_prompt(input_text, src_lang, dest_lang)
                st.text_area("Translation Prompt:", value=translation_prompt, height=100)
                st.text_area("Translation Result:", value=translated_text, height=100)
            else:
                st.error("Please select both source and destination languages.")

if __name__ == "__main__":
    app = LanguageTranslationChatbotStreamlit()
    app.run()
