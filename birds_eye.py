import numpy as np
import cv2 as cv
from scipy.spatial import distance


def birdseye_pers (frm1, box_pts)
    height = frm1.shape[0]
    width = frm1.shape[1]
    src = np.float32(np.array(box_pts))
    dst = np.float32([[0, height], [width, height], [0, 0], [width, 0]])

    M = cv.getPerspectiveTransform(src, dst)
    return M

def inp_pts(frm1)
	for i in range(3):
		image = frame
        cv2.imshow(frm1)
        cv2.waitKey(1)
    if len(mouse_pts) == 5:
        cv2.destroyWindow()
        break
    box_pts = mouse_pts
    return box_pts

#call function in the middle of main 
def birdseye_plot(frm1, box_pts)
    scale_w = 1.2 / 2
    scale_h = 4 / 2
    height = frm1.shape[0]
    width = frm1.shape[1]
    box_pts = inp_pts(frm1)
	M = birdseye_trans(frame, box_pts)
    birdseye_view = np.zeros((int(height * scale_h), int(width * scale_w), 3), np.uint8)
    return birdseye_view

#call function when plotting birdseye view for each frame
def birdseye_nodes(frame, pedestrian_boxes, M, scale_w, scale_h):
    height = frame.shape[0]
    weidht = frame.shape[1]

    node_radius = 10
    color_node = (192, 133, 156)
    thickness_node = 20
    solid_back_color = (41, 41, 41)

    blank_image = np.zeros((int(frame_h * scale_h), int(frame_w * scale_w), 3), np.uint8)
    blank_image[:] = solid_back_color
    warped_pts = []

    for i in range(len(pedestrian_boxes)):
        mid_point_x = int((pedestrian_boxes[i][1] * frame_w + pedestrian_boxes[i][3] * frame_w) / 2)
        mid_point_y = int((pedestrian_boxes[i][0] * frame_h + pedestrian_boxes[i][2] * frame_h) / 2)

        pts = np.array([[[mid_point_x, mid_point_y]]], dtype="float32")
        warped_pt = cv2.perspectiveTransform(pts, M)[0][0]
        warped_pt_scaled = [int(warped_pt[0] * scale_w), int(warped_pt[1] * scale_h)]

        warped_pts.append(warped_pt_scaled)
        birdseye_frame = cv2.circle(blank_image,(warped_pt_scaled[0], warped_pt_scaled[1]),node_radius,color_node,thickness_node,)

    return warped_pts, birdseye_frame



