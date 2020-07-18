import numpy as np
from distance_functions import *
from birds_eye import *
import matplotlib.pyplot as plt

def image_detection(img, outputs, distance_method):
    classes = outputs['instances'].pred_classes.cpu().numpy()
    # Get the output boxes, for more info look here: https://detectron2.readthedocs.io/tutorials/models.html#model-output-format
    bbox = outputs['instances'].pred_boxes.tensor.cpu().numpy()
    # Get indices of only persons (class = 0)
    indices = np.where(classes == 0)[0]
    persons  = bbox[indices]
    bbox = outputs['instances'].pred_boxes.tensor.cpu().numpy()
    num_persons = len(persons)
    
    #Code to get coordinates of base rectangle for transformation
    if frame_num == 1:
        birdseye_map = birdseye_plot(img)

    # Find distance between people
    midpoints = [mid_point(img, persons, i) for i in range(len(persons))] 
    if distance_method == "basic":
        p1, p2 = compute_violations(midpoints)
        img = change_to_red(img, persons, p1, p2)
        
    #Code for the bird's eye transformation method
    birds_plot = birdseye_nodes(midpoints, birdseye_map)
    
    
    plt.figure(figsize = (20, 10))
    plt.imshow(img)
    
    plt.figure(figsize = (20, 10))
    plt.imshow(birds_plot)
