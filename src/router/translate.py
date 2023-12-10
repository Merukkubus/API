from fastapi import APIRouter
from googletrans import Translator

router = APIRouter(
    prefix="/translate",
    tags=["translate"]
)

@router.post("/")
def get_translate(text: str):
    try:
        translator = Translator()
        if translator.detect(text).lang == 'en':
            return translator.translate(text=text, src='en', dest='ru').text
        if translator.detect(text).lang == 'ru':
            return translator.translate(text=text, src='ru', dest='en').text
        else:
            return "Only RU --> EN  or EN --> RU"
    except Exception as e:
        return e