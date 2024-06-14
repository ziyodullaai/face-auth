from fastapi import FastAPI, Body

import df

app = FastAPI()


@app.post("/deepface/verify")
def deepface_verify(
        img_1: str = Body(),
        img_2: str = Body()
):
    return df.verify(img_1, img_2)
