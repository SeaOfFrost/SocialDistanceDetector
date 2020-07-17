import numpy as np
import cv2 as cv
from scipy.spatial import distance


def birdseye_pers (frm1, box_pts)
    src = np.float32(np.array(box_pts))
    dst = np.float32([[0, height], [width, height], [0, 0], [width, 0]])
    frame_map = cv.getPerspectiveTransform(src, dst)
    return frame_map

def inp_pts(event, x, y)
	global mouseX, mouseY, box_pts =[]
    if event == cv2.EVENT_LBUTTONDOWN:
        mouseX, mouseY = x, y
        cv2.circle(image, (x, y), 10, (0, 255, 255), 10)
        box_pts.append((x, y))

#call function in the middle of main 
def birdseye_plot(frm1)
    global scale_w = 4
    global scale_h = 4
    global height = frm1.shape[0]
    global width = frm1.shape[1]

    cv2.namedWindow('frm1', frm1)
    cv2.setMouseCallback('frm1',inp_pts)
	while True:
        cv2.imshow('frm1',frm1)
        cv2.waitKey(1)
        if len(mouse_pts) == 5:
            cv2.destroyWindow("frm1")
            break
	frame_map = birdseye_pers(frm1, box_pts)
    birdseye_view = np.zeros((int(height * scale_h), int(width * scale_w), 3), np.uint8)
    return birdseye_view

#call function when plotting birdseye view for each frame
def birdseye_nodes(frame, pedestrian_boxes, frame_map):

	global birdseye_thresh = 120

    node_radius = 10
    g_color_node = (0 , 255, 0)
    r_color_node = (255 , 0, 0)
    thickness_node = 20
    solid_back_color = (41, 41, 41)

    blank_image = np.zeros((int(height * scale_h), int(width * scale_w), 3), np.uint8)
    blank_image[:] = solid_back_color
    warped_pts = []

    for i in range(len(pedestrian_boxes)):
        mid_point_x = int((pedestrian_boxes[i][1] * width + pedestrian_boxes[i][3] * width) / 2)
        mid_point_y = int((pedestrian_boxes[i][0] * height + pedestrian_boxes[i][2] * height) / 2)

        pts = np.array([[[mid_point_x, mid_point_y]]], dtype="float32")
        warped_pt = cv2.perspectiveTransform(pts, frame_map)[0][0]
        warped_pt_scaled = [int(warped_pt[0] * scale_w), int(warped_pt[1] * scale_h)]

        warped_pts.append(warped_pt_scaled)
        birdseye_frame = cv2.circle(blank_image,(warped_pt_scaled[0], warped_pt_scaled[1]),node_radius,g_color_node,thickness_node,)

        dist_mat = pdist(np.array(warped_pts), metric  ="Euclidean")
        node_dist = squareform(dist_mat)

        dd = np.where(node_dist < birdseye_thresh)
    	close_p = []
    	color_10 = (255,0,0)
    	lineThickness = 4
    	violations = len(np.where(dist_mat < birdseye_thresh)[0])
    	for i in range(int(np.ceil(len(dd[0]) / 2))):
        	if dd[0][i] != dd[1][i]:
            	point1 = dd[0][i]
            	point2 = dd[1][i]

            	close_p.append([point1, point2])

            	cv2.line(bird_image,(p[point1][0], p[point1][1]),(p[point2][0], p[point2][1]),color_10,lineThickness)
            	
        birdseye_frame = cv2.circle(blank_image,(close_p[0], close_p[1]),node_radius,r_color_node,thickness_node,)


        

    return warped_pts, birdseye_frame



