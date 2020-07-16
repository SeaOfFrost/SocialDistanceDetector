from scipy.spatial import distance
import cv2
import numpy as np

def mid_point(img, persons, idx):
  #get the coordinates
  x1,y1,x2,y2 = persons[idx]
  _ = cv2.rectangle(img, (x1, y1), (x2, y2), (0,0,255), 2)
  
  #compute bottom center of bbox
  x_mid = int((x1+x2)/2)
  y_mid = int(y2)
  mid   = (x_mid,y_mid)
  
  cv2.putText(img, str(idx + 1), mid, cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
  
  return mid

def compute_violations(midpoints, thresh = 150):
    D = distance.cdist(midpoints, midpoints, metric = "euclidean")
    p1 = []
    p2 = []
    # Just loop through the upper triangle cause symmetric matrix
    for i in range(0, D.shape[0]):
        for j in range(i + 1, D.shape[1]):
            if (i != j) and (D[i][j] <= thresh):
                p1.append(i)
                p2.append(j)
    return p1, p2

def change_to_red(img, persons, p1, p2):
    risky = np.unique(p1 + p2)
    for i in risky:
        x1, y1, x2, y2 = persons[i]
        _ = cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
    return img    