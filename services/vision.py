from main import DETECTION_LATENCY, MATCH_ACCURACY
import time

async def process_rtsp_stream(rtsp_url, camera_id, session, model_name="ArcFace"):
    cap = cv2.VideoCapture(rtsp_url)
    while True:
        start = time.time()
        ret, frame = cap.read()
        if not ret:
            break
        # Detection
        with DETECTION_LATENCY.time():
            embeddings = extract_embedding(frame, model_name)
        # Recognition
        accuracy = 0.0
        if embeddings:
            user_ids = await match_embedding(session, embeddings)
            # Calculate match accuracy (fraction of embeddings matched)
            if len(embeddings):
                accuracy = len(user_ids) / len(embeddings)
            MATCH_ACCURACY.observe(accuracy)
        # Sleep for interval
        cv2.waitKey(2000)
    cap.release()