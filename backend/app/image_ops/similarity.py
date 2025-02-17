import cv2
import numpy as np

import time

def calc_similarity_of_images(img1_filepath: str, img2_filepath: str) -> float:
	start_time = time.time()

	original = cv2.imread(img1_filepath)
	image_to_compare = cv2.imread(img2_filepath)

	# scale_percent = 50 # percent of original size
	# width = int(original.shape[1] * scale_percent / 100)
	# height = int(original.shape[0] * scale_percent / 100)
	width = 100;
	height = 100;
	dim = (width, height)
	# resize image
	original = cv2.resize(original, dim, interpolation = cv2.INTER_AREA)

	# width2 = int(image_to_compare.shape[1] * scale_percent / 100)
	# height2 = int(image_to_compare.shape[0] * scale_percent / 100)
	width2 = 100;
	height2 = 100;
	dim2 = (width, height)
	# resize image
	image_to_compare = cv2.resize(image_to_compare, dim, interpolation = cv2.INTER_AREA)


	# 1) Check if 2 images are equals
	if original.shape == image_to_compare.shape:
	    print("The images have same size and channels")
	    difference = cv2.subtract(original, image_to_compare)
	    b, g, r = cv2.split(difference)

	    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
	        print("The images are completely Equal")
	    else:
	        print("The images are NOT equal")

	# 2) Check for similarities between the 2 images
	sift = cv2.xfeatures2d.SIFT_create()
	kp_1, desc_1 = sift.detectAndCompute(original, None)
	kp_2, desc_2 = sift.detectAndCompute(image_to_compare, None)

	index_params = dict(algorithm=0, trees=5)
	search_params = dict()
	flann = cv2.FlannBasedMatcher(index_params, search_params)

	matches = flann.knnMatch(desc_1, desc_2, k=2)

	good_points = []
	for m, n in matches:
	    if m.distance < 0.6*n.distance:
	        good_points.append(m)

	# Define how similar they are
	number_keypoints = 0
	if len(kp_1) <= len(kp_2):
	    number_keypoints = len(kp_1)
	else:
	    number_keypoints = len(kp_2)


	print("Keypoints 1ST Image: " + str(len(kp_1)))
	print("Keypoints 2ND Image: " + str(len(kp_2)))
	print("GOOD Matches:", len(good_points))
	match = len(good_points) / number_keypoints * 100
	print("How good it's the match: ", match)

	# result = cv2.drawMatches(original, kp_1, image_to_compare, kp_2, good_points, None)



	# cv2.imshow("result", cv2.resize(result, None, fx=0.4, fy=0.4))
	# cv2.imwrite("feature_matching.jpg", result)

	# 
	# cv2.imshow("Original", cv2.resize(original, None, fx=0.4, fy=0.4))
	# cv2.imshow("Duplicate", cv2.resize(image_to_compare, None, fx=0.4, fy=0.4))
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()

	print ("My program took", time.time() - start_time, "to run")

	return match

#
#path1 = "images/original_golden_bridge.jpg"
#path2 = "images/cartoonized.jpg"
#match_percent = calc_similarity_of_images(path1, path2) 
