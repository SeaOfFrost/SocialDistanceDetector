import numpy as np
import cv2
import random
from google.colab.patches import cv2_imshow
import matplotlib.pyplot as plt

# detectron2 dependencies
import detectron2
from detectron2.utils.logger import setup_logger
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog
setup_logger()

ap = argparse.ArgumentParser()
ap.add_argument("-dm", "--detection_method", type=str, default="FasterRCNN", help = "Object Detection Method to Use")
ap.add_argument("-i", "--video", type=str, required=True, help = "path to input video")
args = vars(ap.parse_args())

cfg = get_cfg() # obtain detectron2's default config
if arg["detection_method"] == "FasterRCNN": # Inference time -- 0.104
    cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/faster_rcnn_R_50_C4_3x.yaml"))
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.9  
    cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-Detection/faster_rcnn_R_50_C4_3x.yaml")
    predictor = DefaultPredictor(cfg)
elif arg["detection_method"] == "FastRCNN": # Inference time -- 0.104
    cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/fast_rcnn_R_50_FPN_1x.yaml"))
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.9  
    cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-Detection/fast_rcnn_R_50_FPN_1x.yaml")
    predictor = DefaultPredictor(cfg)
elif arg["detection_method"] == "RetinaNet": # Inference time -- 0.056
    cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/retinanet_R_50_FPN_3x.yaml"))
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.9  
    cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-Detection/retinanet_R_50_FPN_3x.yaml")
    predictor = DefaultPredictor(cfg)
elif arg["detection_method"] == "YOLO":
    # Add code to call this 

img = cv2.imread(args["image"])
outputs = predictor(img)

# Get the output boxes, for more info look here: https://detectron2.readthedocs.io/tutorials/models.html#model-output-format
bbox = outputs['instances'].pred_boxes.tensor.cpu().numpy()
# Get indices of only persons (class = 0)
indices = np.where(classes == 0)[0]
people  = bbox[indices]
bbox = outputs['instances'].pred_boxes.tensor.cpu().numpy()
num_people = len(people)

# Find distance between people