from fastapi import FastAPI, UploadFile, File
from typing import List
from test import treatImage
import os

app = FastAPI()

# Directory to store the uploaded images
cwd = os.getcwd()
UPLOAD_DIR = cwd + "/assets"

# Create the upload directory if it doesn't exist
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload")
async def upload_image(images: List[UploadFile] = File(...)):
    """
    Endpoint to upload image(s) to the server and store them in a specific directory.
    """
    for image in images:
        file_path = os.path.join(UPLOAD_DIR, image.filename)
        with open(file_path, "wb") as f:
            contents = await image.read()
            f.write(contents)
    
    return {"message": "Images uploaded successfully"}


@app.get("/treat/{image_name}")
async def treat_image(image_name: str):
    """
    Endpoint to treat the image file and return the results as a JSON text object.
    """
    # Apply the "treat" function to the image file
    results = treat(image_name)
    
    return results

@app.delete("/delete/{image_name}")
async def delete_image(image_name: str):
    """
    Endpoint to delete the specified image file.
    """
    file_path = os.path.join(UPLOAD_DIR, image_name)
    if os.path.exists(file_path):
        os.remove(file_path)
        return {"message": f"Image '{image_name}' deleted successfully"}
    else:
        return {"message": f"Image '{image_name}' not found"}

def treat(image_name: str):
    """
    Function to process the image and return the results.
    This function can be customized according to your requirements.
    """
    results = treatImage(image_name)
    # file_path = os.path.join(UPLOAD_DIR, image_name)
    # if os.path.exists(file_path):
    #     os.remove(file_path)
    return results
