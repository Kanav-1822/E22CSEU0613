from fastapi import FastAPI


app = FastAPI()

@app.get("/social-media-analytics/{param}")
def social_media_analytics(number_id: int):
    pass
