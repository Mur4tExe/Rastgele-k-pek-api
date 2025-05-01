from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Merhaba! Bu API rastgele köpek fotoğrafı döner.",
        "kullanim": "/randomdog"
    }

@app.get("/randomdog")
def get_random_dog():
    try:
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        data = response.json()
        return {
            "success": True,
            "image": data["message"],
            "note": "Telegram: @ZaherOrj @QueryBots"
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
