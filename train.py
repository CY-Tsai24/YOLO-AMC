import sys
import os

sys.path.insert(0, r"")

os.environ["OMP_NUM_THREADS"] = "8"
os.environ["USE_BLIS"] = "1"
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import ultralytics
print("ultralytics loaded from:", ultralytics.__file__)

from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO(r"")
    model.train(
        data=r"",
        imgsz=640,
        epochs=800,
        single_cls=False,
        batch=32,
        workers=8,
        device='0',
        project=r'',
        name=''
    )





