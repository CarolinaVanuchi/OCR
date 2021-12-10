import numpy as np
import cv2

# sort a list of list points by their distance from the origin list point
def sort_dist(list, origin):
    new_list = []
    dist = []
    i = 0
    
    for (x, y) in list:
        d = np.linalg.norm(np.array(origin) - np.array([x, y]))
        dist.append([i, d])
        i += 1

    dist.sort(key = lambda n: n[1]) 

    for (i, d) in dist:
        new_list.append(list[i])

    return new_list


# organize corner pairs from a list of top corners and bottom corners
def organize_crop_corners(top_corner_rect_list, bottom_corner_rect_list):
    corner_pairs = []

    # sort top corner by crescent distance of 0,0, this will be the processing order
    top_corner_rect_list = sort_dist(top_corner_rect_list, [0,0])

    # find the closest bottom corner for each top one
    for (x, y) in top_corner_rect_list:
        bottom_matches = sort_dist(bottom_corner_rect_list, [x, y])

        for (xx, yy) in bottom_matches:
            if xx > x and yy > y:
                corner_pairs.append([[x, y], [xx, yy]])
                break

    return corner_pairs


# apply blur, correct contrast, hsv convertion
def preprocessing(image):

    # # pattern match image show
    # pm_image = image.copy()

    # morph
    kernel = np.ones((7,7),np.uint8)
    morph = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

    hsv = cv2.cvtColor(morph, cv2.COLOR_BGR2HSV)

    # red hue mask
    mask = cv2.inRange(hsv, (165, 50, 127), (195, 255, 255))
    # cv2.imwrite("output/image/hsvmask.png", mask)

    return mask


# match patterns
def pmatch(image, confidence_threshold):
    # for div 
    div = cv2.imread("image/div_bw.png", cv2.IMREAD_GRAYSCALE) 
    match = cv2.matchTemplate(image, div, cv2.TM_CCOEFF_NORMED)

    h, w = div.shape
    y_loc, x_loc = np.where(match >= confidence_threshold)

    vdivs = []
    for (x, y) in zip(x_loc, y_loc):
        vdivs.append([x, y, w, h])
        vdivs.append([x, y, w, h])
    
    vdivs, n = cv2.groupRectangles(vdivs, 1, 0.2)

    # for (x, y, w, h) in vdivs:
    #     cv2.rectangle(pm_image, [x,y], [x + w, y + h], (255, 0, 255), 2)
    
    # for top corners 
    topcorner = cv2.imread("image/top_corner_bw.png", cv2.IMREAD_GRAYSCALE) 
    match = cv2.matchTemplate(image, topcorner, cv2.TM_CCOEFF_NORMED)

    h, w = topcorner.shape
    y_loc, x_loc = np.where(match >= confidence_threshold)

    tcorners = []
    for (x, y) in zip(x_loc, y_loc):
        tcorners.append([x, y, w, h])
        tcorners.append([x, y, w, h])
    
    tcorners, n = cv2.groupRectangles(tcorners, 1, 0.2)

    # for (x, y, w, h) in tcorners:
    #     cv2.rectangle(pm_image, [x,y], [x + w, y + h], (255, 0, 255), 2)
    
    # for bottom corners 
    bottomcorner = cv2.imread("image/bottom_corner_bw.png", cv2.IMREAD_GRAYSCALE) 
    match = cv2.matchTemplate(image, bottomcorner, cv2.TM_CCOEFF_NORMED)

    h, w = bottomcorner.shape
    y_loc, x_loc = np.where(match >= confidence_threshold)


    bcorners = []
    for (x, y) in zip(x_loc, y_loc):
        bcorners.append([x, y, w, h])
        bcorners.append([x, y, w, h])
    
    bcorners, n = cv2.groupRectangles(bcorners, 1, 0.2)
    
    # for (x, y, w, h) in bcorners:
    #     cv2.rectangle(pm_image, [x,y], [x + w, y + h], (255, 0, 255), 2)
    
    return [vdivs, tcorners, bcorners]


def process(image, corner_width_pad, confidence_threshold):

    proc = preprocessing(image)
    matches = pmatch(proc, confidence_threshold)

    vdivs, tcorners, bcorners = matches

    # convert ndarray to list 
    tcorners = tcorners.tolist()
    buf = []
    for n in tcorners:
        # add a little clearance
        n[0] += corner_width_pad
        n[1] += corner_width_pad
        # cut the width and height
        buf.append(n[:2])

    tcorners = buf

    # convert ndarray to list 
    bcorners = bcorners.tolist()
    buf = []
    for n in bcorners:
        # since templatematch matches the top right corner, we add the width and height
        # to the bottom corner
        n[0] += n[2]
        n[1] += n[3]
        # add a little clearance
        n[0] -= corner_width_pad
        n[1] -= corner_width_pad
        # cut the width and height
        buf.append(n[:2])

    bcorners = buf

    # group corner pairs
    pairs = organize_crop_corners(tcorners, bcorners)
    # print("images:", pairs)

    i = 0
    for (t, b) in pairs:
        # cv2.imwrite("output/image/image_{}.png".format(i), image[t[1]:b[1], t[0]:b[0]])
        i += 1

    for (t, b) in pairs:
        cv2.rectangle(image, t, b, (255, 255, 0), 2)

    return image

    # cv2.imwrite("output/image/pm_image.png", pm_image)
    # cv2.imwrite("output/image/rect_pairs_image.png", image)