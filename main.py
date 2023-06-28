from typing import Union
from pydantic import BaseModel,Field
from fastapi import FastAPI,HTTPException 
from uuid import UUID

app = FastAPI()


class Image(BaseModel):
    id:UUID
    name:str=Field(min_length=1)
    idenitity_id:str=Field(min_length=1,max_length=100)
    image_name:str=Field(min_length=1,max_length=100)


IMAGES=[]
@app.post("/add")
def add_image(image:Image):
    IMAGES.append(image)
    return image

@app.get("/images")
def read_images():
    return IMAGES
@app.get("/{image_id}")
def get_by_id(image_id:UUID):
    for image in IMAGES:
        if image.id==image_id:
           return image
    raise HTTPException(
        status_code=404,
        detail='Does not exist'
    )
