import numpy as np
import cv2
from distance_functions import *


def birdseye_pers (frm1, box_pts):
    src = np.float32(np.array(box_pts))
    dst = np.float32([[0, height], [width, height], [0, 0], [width, 0]])
    frame_map = cv2.getPerspectiveTransform(src, dst)
    return frame_map

def inp_pts(event, x, y, frm1):
    global mouseX, mouseY, box_pts
    box_pts=[]
    if event == cv2.EVENT_LBUTTONDOWN:
        mouseX, mouseY = x, y
        cv2.circle(frm1, (x, y), 10, (0, 255, 255), 10)
        box_pts.append((x, y))

#call function in the middle of main 
def birdseye_plot(frm1):
    global scale_w, scale_h, height, width
    scale_w = 4
    scale_h = 4
    height =frm1.shape[0]
    width = frm1.shape[1]
    
    cv2.namedWindow('frm1', frm1)
    cv2.setMouseCallback('frm1',inp_pts(frm1))
    while True:
    	cv2.imshow('frm1',frm1)
    	cv2.waitKey(1)
    	if len(box_pts) == 5:
    	    cv2.destroyWindow("frm1")
    	    break
    frame_map = birdseye_pers(frm1, box_pts)

    return frame_map

#call function when plotting birdseye view for each frame
def birdseye_nodes(midpoints, frame_map):

    node_radius = 10
    g_color_node = (0 , 255, 0)
    r_color_node = (255 , 0, 0)
    thickness_node = 20
    solid_back_color = (41, 41, 41)

    blank_image = np.zeros((int(height * scale_h), int(width * scale_w), 3), np.uint8)
    blank_image[:] = solid_back_color
    warped_pts = []

    for i in range(midpoints):

        pts = np.array(midpoints, dtype="float32")
        warped_pt = cv2.perspectiveTransform(pts, frame_map)[0][0]
        warped_pt_scaled = [int(warped_pt[0] * scale_w), int(warped_pt[1] * scale_h)]

        warped_pts.append(warped_pt_scaled)
        birdseye_frame = cv2.circle(blank_image,(warped_pt_scaled[0], warped_pt_scaled[1]),node_radius,g_color_node,thickness_node)

    p1, p2 = compute_violations(warped_pts)

    violations_ind = np.unique(p1+p2)
    violations_x = warped_pts[violations_ind][0]
    violations_y = warped_pts[violations_ind][1]
    
    birdseye_frame = cv2.circle(blank_image,(violations_x, violations_y),node_radius,r_color_node,thickness_node)        

    return birdseye_frame



