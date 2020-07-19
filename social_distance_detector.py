import numpy as np
import cv2
import random
import argparse
from detection_functions import *

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
ap.add_argument("-detm", "--detection_method", type=str, default="FasterRCNN", help = "Object Detection Method to Use")
ap.add_argument("-i", "--input", type=str, default="image", help = "Whether input is image or video")
ap.add_argument("-p", "--path", type=str, help = "path to input")
ap.add_argument("-distm", "--distance_method", type=str, default="birdseye", help = "Distance Estimation method to use")
args = vars(ap.parse_args())

cfg = get_cfg() # obtain detectron2's default config
if args["detection_method"] == "FasterRCNN": # Inference time -- 0.104
    cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/faster_rcnn_R_50_C4_3x.yaml"))
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.9  
    cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-Detection/faster_rcnn_R_50_C4_3x.yaml")
    predictor = DefaultPredictor(cfg)
elif args["detection_method"] == "FastRCNN": # Inference time -- 0.104
    cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/fast_rcnn_R_50_FPN_1x.yaml"))
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.9  
    cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-Detection/fast_rcnn_R_50_FPN_1x.yaml")
    predictor = DefaultPredictor(cfg)
elif args["detection_method"] == "RetinaNet": # Inference time -- 0.056
    cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/retinanet_R_50_FPN_3x.yaml"))
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.9  
    cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-Detection/retinanet_R_50_FPN_3x.yaml")
    predictor = DefaultPredictor(cfg)
'''
Add code here for YOLO
'''
'''
if args["input"] == "image":
    img = cv2.imread(args["path"])
    outputs = predictor(img)
    image_detection(img, outputs, args["distance_method"])
'''
global frame_num
frame_num =1
img = cv2.imread('lol.png')
outputs = predictor(img)
image_detection(img, outputs, 'basic', frame_num)
'''
Add code here for video input
'''
