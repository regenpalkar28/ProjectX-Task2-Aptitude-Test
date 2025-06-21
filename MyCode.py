import numpy as np
import cv2 as cv

testcase1 = {
    'red': 'Testcase1/Raghav.jpg',
    'blue': 'Testcase1/Bhaskar.jpg',
    'green': 'Testcase1/Ganshyam.jpg',
    'cyan': 'Testcase1/Chintan.jpg',
    'orange': 'Testcase1/Omkar.jpg',
    'yellow': 'Testcase1/Yash.jpg'
}

testcase2 = {
    'red': 'Testcase2/Raghav.jpg',
    'green': 'Testcase2/Ganshyam.jpg',
    'blue': 'Testcase2/Bhaskar.jpg',
    'cyan': 'Testcase2/Chintan.png',
    'orange': 'Testcase2/Om.png',
    'yellow': 'Testcase2/Yash.png',
}

max_display = 400

def resizer(testcase, test_name=""):
    resized_images = {}
    for name, path in testcase.items():
        img = cv.imread(path)

        if img is not None:
            height, width, _ = img.shape
            scale = max_display/width;
            disp_height = int(scale*height)
            resized = cv.resize(img, (max_display,disp_height))
            resized_images[name] = resized
        else:
            print(f"ERROR for {test_name}: could not find {path}.")
    return resized_images

def bitwise_or_converter(testcase, test_name=""):
    resized_images = resizer(testcase, test_name)
    required_rgb = ['red', 'blue', 'green']
    usable_red = resized_images.get('red')
    usable_blue = resized_images.get('blue')
    usable_green = resized_images.get('green')

    usable_yellow = resized_images.get('yellow')
    usable_orange = resized_images.get('orange')
    usable_cyan = resized_images.get('cyan')

    if usable_red is not None and usable_blue is not None and usable_green is not None and usable_orange is not None and usable_cyan is not None and usable_yellow is not None:
        temp_rgb = cv.bitwise_or(usable_red, usable_green)
        result_rgb = cv.bitwise_or(temp_rgb, usable_blue)
        temp_cyo = cv.bitwise_or(usable_cyan, usable_orange)
        result_cyo = cv.bitwise_or(temp_cyo, usable_yellow)
        result = cv.bitwise_or(result_rgb, result_cyo) 
        # cv.imshow(f'OR performed on RGB for ({test_name})', result_rgb) 
    else:
        print(f"Could not perform BITWISE OR for {test_name}. Missing one or more of {required_rgb}")
    return result_rgb


pattern1 = bitwise_or_converter(testcase1, "testcase 1")
pattern2 = bitwise_or_converter(testcase2, "testcase 2")

def solid_detector(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    _, threshed = cv.threshold(gray, 10, 255, cv.THRESH_BINARY)

    threshed[:70, :] = 0
    threshed[:, :50] = 0
    # cv.imshow("threshed",threshed)
    contours, _ = cv.findContours(threshed, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    print(f"No. of contours detected: {len(contours)}")

    display_image = image.copy()
    solid_centers = []  # list of centers of solid objects

    for contour in contours:
        area = cv.contourArea(contour)
        if area < 50:
            continue

        mask = np.zeros(gray.shape, dtype=np.uint8)
        cv.drawContours(mask, [contour], -1, 255, cv.FILLED)
        pixels_inside_contour = cv.countNonZero(cv.bitwise_and(threshed, mask))

        solidity_threshold = 0.85
        if pixels_inside_contour / area > solidity_threshold:
            M = cv.moments(contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                solid_centers.append((cx, cy))  
                cv.circle(display_image, (cx, cy), 4, (0, 0, 0), -1)

    x_clusters = group_centroid([cx for cx, cy in solid_centers])
    y_clusters = group_centroid([cy for cx, cy in solid_centers])

    col_labels = [chr(ord('A') + i) for i in range(len(x_clusters))]  # A, B, C...
    row_labels = list(range(1, len(y_clusters) + 1))  # 1, 2, 3...

    for cx, cy in solid_centers:
        col_id = np.argmin([abs(cx - x) for x in x_clusters])
        row_id = np.argmin([abs(cy - y) for y in y_clusters])

        col = col_labels[col_id]
        row = row_labels[row_id]
        label = f"{row}{col}"

        cv.putText(display_image, label, (cx + 10, cy), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        print(f"solid object detected at: {label}")

    print(f"Total solid dots: {len(solid_centers)}")
    cv.imshow("Number-Letter combo identified ", display_image)

def group_centroid(values, threshold=30):
    values = sorted(values)
    clusters = []
    temp = []

    for v in values:
        if not temp or abs(v - np.mean(temp)) <= threshold:
            temp.append(v)
        else:
            clusters.append(int(np.mean(temp)))
            temp = [v]
    if temp:
        clusters.append(int(np.mean(temp)))
    return clusters

solid_detector(pattern1)
# solid_detector(pattern2)
cv.waitKey(0)
cv.destroyAllWindows()
