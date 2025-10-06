import os
import numpy as np
import cv2
import face_recognition
from fastapi import UploadFile

def save_image(file: UploadFile, upload_dir: str) -> str:
    filename = file.filename
    out_path = os.path.join(upload_dir, filename)
    with open(out_path, "wb") as buffer:
        buffer.write(file.file.read())
    return out_path

def detect_faces(image_path: str):
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image)
    encodings = face_recognition.face_encodings(image, face_locations)
    # Convert numpy arrays to lists so they are JSON serializable
    encodings = [enc.tolist() for enc in encodings]
    return encodings, face_locations

def recognize_face(encoding, known_encoding, tolerance=0.5):
    # encoding, known_encoding are lists, need to convert to np.array
    return face_recognition.compare_faces(
        [np.array(known_encoding)], np.array(encoding), tolerance=tolerance
    )[0]