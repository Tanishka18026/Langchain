from flask import Flask, render_template, request
from langchain_core.prompts import PromptTemplate
from googletrans import Translator, LANGUAGES

app = Flask(__name__)

translator = Translator()
prompt_template = PromptTemplate(
    input_variables=["text", "src_lang", "dest_lang"],
    template="Translate the following text from {src_lang} to {dest_lang}: {text}"
)

@app.route('/')
def index():
    languages = list(LANGUAGES.values())
    return render_template('index.html', languages=languages)

@app.route('/translate', methods=['POST'])
def translate():
    input_text = request.form['input_text']
    src_lang = request.form['src_lang']
    dest_lang = request.form['dest_lang']

    translated_text = translator.translate(input_text, src=src_lang, dest=dest_lang).text
    translation_prompt = prompt_template.format(text=input_text, src_lang=src_lang, dest_lang=dest_lang)

    return render_template('result.html', translation_prompt=translation_prompt, translated_text=translated_text)

if __name__ == "__main__":
    app.run(debug=True)
