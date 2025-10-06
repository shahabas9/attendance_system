from fastapi import UploadFile, File
import cv2
import numpy as np

@router.post("/liveness")
async def liveness_check(image: UploadFile = File(...)):
    """
    Basic liveness detection (returns True/False)
    """
    img_bytes = await image.read()
    np_img = np.frombuffer(img_bytes, np.uint8)
    frame = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
    # Simple demo: check for eye/face landmarks (replace with production model)
    # For production, use deep learning based liveness detection
    if frame is not None and frame.shape[0] > 0:
        # Placeholder logic
        liveness_score = 0.9
        is_live = liveness_score > 0.5
        return {"is_live": is_live, "score": liveness_score}
    return {"is_live": False, "score": 0}