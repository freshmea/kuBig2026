"""
Run with:
    pip install mediapipe opencv-python

MediaPipe Tasks API hand landmark demo (works with mediapipe 0.10.x tasks-only builds).
Required model file:
    /home/aa/kuBig2026/opencv_ex/data/hand_landmarker.task

You can download it from MediaPipe model zoo:
https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task
"""

from __future__ import annotations

import os
import time
from pathlib import Path

import cv2
import mediapipe as mp
from mediapipe.tasks import python as mp_python
from mediapipe.tasks.python import vision

MODEL_PATH = "/home/aa/kuBig2026/opencv_ex/data/hand_landmarker.task"
DEFAULT_QT_FONTDIR = "/usr/share/fonts/truetype/dejavu"


def _prepare_qt_font_dir() -> None:
    if not os.path.isdir(DEFAULT_QT_FONTDIR):
        return

    try:
        cv2_dir = Path(cv2.__file__).resolve().parent
        target = cv2_dir / "qt" / "fonts"
        target.parent.mkdir(parents=True, exist_ok=True)

        if not target.exists():
            target.symlink_to(DEFAULT_QT_FONTDIR, target_is_directory=True)
    except OSError:
        # Continue even if symlink preparation fails; this only affects warning noise.
        pass


def _to_px(x: float, y: float, w: int, h: int) -> tuple[int, int]:
    return int(x * w), int(y * h)


def main() -> None:
    _prepare_qt_font_dir()

    if not os.path.exists(MODEL_PATH):
        print("Model file not found:", MODEL_PATH)
        print("Download:")
        print("  https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task")
        return

    cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 30)

    if not cap.isOpened():
        print("Unable to connect to camera")
        return

    base_options = mp_python.BaseOptions(model_asset_path=MODEL_PATH)
    options = vision.HandLandmarkerOptions(
        base_options=base_options,
        running_mode=vision.RunningMode.VIDEO,
        num_hands=2,
        min_hand_detection_confidence=0.5,
        min_hand_presence_confidence=0.5,
        min_tracking_confidence=0.5,
    )

    prev_time = time.time()
    frame_index = 0

    with vision.HandLandmarker.create_from_options(options) as landmarker:
        while True:
            ok, frame = cap.read()
            if not ok:
                break

            frame = cv2.flip(frame, 1)
            h, w = frame.shape[:2]

            # MediaPipe Tasks expects SRGB image wrapper.
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            timestamp_ms = int(frame_index * (1000.0 / 30.0))
            result = landmarker.detect_for_video(mp_image, timestamp_ms)
            frame_index += 1

            if result.hand_landmarks:
                for hand_landmarks in result.hand_landmarks:
                    for lm in hand_landmarks:
                        px, py = _to_px(lm.x, lm.y, w, h)
                        cv2.circle(frame, (px, py), 3, (0, 255, 255), -1)

                    connections = vision.HandLandmarksConnections.HAND_CONNECTIONS
                    for conn in connections:
                        p1 = hand_landmarks[conn.start]
                        p2 = hand_landmarks[conn.end]
                        x1, y1 = _to_px(p1.x, p1.y, w, h)
                        x2, y2 = _to_px(p2.x, p2.y, w, h)
                        cv2.line(frame, (x1, y1), (x2, y2), (255, 180, 0), 2)

            now = time.time()
            fps = 1.0 / max(now - prev_time, 1e-6)
            prev_time = now

            cv2.putText(
                frame,
                f"FPS: {fps:.1f}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.0,
                (0, 255, 0),
                2,
                cv2.LINE_AA,
            )

            cv2.imshow("57_handpose_mediapipe_tasks", frame)
            key = cv2.waitKey(1) & 0xFF
            if key in (27, ord("q")):
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
