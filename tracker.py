import cv2
import numpy as np
from datetime import datetime
from ultralytics import YOLO

class VehicleTracker:
    def __init__(self, model_path='yolov8n.pt', meters_per_pixel=0.05):
        self.model = YOLO(model_path)
        self.meters_per_pixel = meters_per_pixel
        self.vehicles_data = {}

    def process_video(self, input_video_path, output_video_path=None):
        cap = cv2.VideoCapture(input_video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out = None
        if output_video_path:
            out = cv2.VideoWriter(
                output_video_path, 
                cv2.VideoWriter_fourcc(*'mp4v'), 
                fps, 
                (width, height)
            )

        frame_idx = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            # كلاسات المركبات من COCO: 2: car, 3: motorcycle, 5: bus, 7: truck
            results = self.model.track(
                frame, 
                persist=True, 
                tracker="bytetrack.yaml", 
                classes=[2, 3, 5, 7], 
                verbose=False
            )
            
            current_time_sec = frame_idx / fps

            if results[0].boxes is not None and results[0].boxes.id is not None:
                boxes = results[0].boxes.xyxy.cpu().numpy().astype(int)
                track_ids = results[0].boxes.id.cpu().numpy().astype(int)
                
                for box, track_id in zip(boxes, track_ids):
                    t_id = int(track_id)
                    x1, y1, x2, y2 = box
                    bottom_center = ((x1 + x2) / 2, float(y2))
                    
                    if t_id not in self.vehicles_data:
                        self.vehicles_data[t_id] = {
                            "entry_time_sec": round(current_time_sec, 2),
                            "first_detected_at": datetime.now().isoformat(),
                            "positions": [(bottom_center, current_time_sec)],
                            "speed_kmh": 0.0
                        }
                    else:
                        self.vehicles_data[t_id]["positions"].append((bottom_center, current_time_sec))
                        pos_history = self.vehicles_data[t_id]["positions"]
                        
                        if len(pos_history) >= 2:
                            (p1, t1), (p2, t2) = pos_history[-2], pos_history[-1]
                            dt = t2 - t1
                            if dt > 0:
                                pixel_dist = np.linalg.norm(np.array(p2) - np.array(p1))
                                speed = ((pixel_dist * self.meters_per_pixel) / dt) * 3.6
                                self.vehicles_data[t_id]["speed_kmh"] = round(speed, 1)

                    speed = self.vehicles_data[t_id]["speed_kmh"]
                    
                    if out:
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        label = f"ID: {t_id} | {speed} km/h"
                        cv2.putText(frame, label, (x1, max(y1 - 10, 20)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            if out:
                out.write(frame)
            frame_idx += 1

        cap.release()
        if out:
            out.release()
            
        return self.vehicles_data
