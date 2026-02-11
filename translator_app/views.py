from django.shortcuts import render
from googletrans import Translator

translator = Translator()

def home(request):
    translated_text = ""
    original_text = ""

    if request.method == "POST":
        original_text = request.POST.get("text")
        target_lang = request.POST.get("language")

        if original_text and target_lang:
            translated = translator.translate(original_text, dest=target_lang)
            translated_text = translated.text

    context = {
        "translated_text": translated_text,
        "original_text": original_text
    }

    return render(request, "home.html", context)
