import streamlit as st
from googletrans import Translator, LANGUAGES
from langchain_core.prompts import PromptTemplate

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

    def run(self):
        st.title("Language Translation Chatbot")

        # Input text
        input_text = st.text_input("Enter text to translate:")

        # Language selections
        src_lang = st.selectbox("Select source language:", list(LANGUAGES.values()))
        dest_lang = st.selectbox("Select destination language:", list(LANGUAGES.values()))

        if st.button("Translate"):
            translated_text = self.translate_text(input_text, src_lang, dest_lang)
            translation_prompt = self.create_translation_prompt(input_text, src_lang, dest_lang)
            st.text_area("Translation Prompt:", value=translation_prompt, height=100)
            st.text_area("Translation Result:", value=translated_text, height=100)

if __name__ == "__main__":
    app = LanguageTranslationChatbotStreamlit()
    app.run()
