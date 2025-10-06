import cv2

def check_camera_health(rtsp_url: str):
    cap = cv2.VideoCapture(rtsp_url)
    is_up = cap.isOpened()
    frame_rate = None
    if is_up:
        frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
    cap.release()
    return is_up, frame_rate