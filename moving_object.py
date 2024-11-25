import cv2 as cv

capture = cv.VideoCapture('Resources/Videos/dog.mp4')


# Create ORB detectors
def matchThreeType(image1,image2):
    orb = cv.ORB_create()
    sift = cv.SIFT_create()
    akaze = cv.AKAZE_create()

    # Find keypoints and descriptors in both images for each method
    keypoints1_orb, descriptors1_orb = orb.detectAndCompute(image1, None)
    keypoints2_orb, descriptors2_orb = orb.detectAndCompute(image2, None)

    keypoints1_sift, descriptors1_sift = sift.detectAndCompute(image1, None)
    keypoints2_sift, descriptors2_sift = sift.detectAndCompute(image2, None)

    keypoints1_akaze, descriptors1_akaze = akaze.detectAndCompute(image1, None)
    keypoints2_akaze, descriptors2_akaze = akaze.detectAndCompute(image2, None)

    # Create Brute-Force Matchers
    bf = cv.BFMatcher()

    # Match descriptors for each method
    matches_orb = bf.knnMatch(descriptors1_orb, descriptors2_orb, k=2)
    matches_sift = bf.knnMatch(descriptors1_sift, descriptors2_sift, k=2)
    matches_akaze = bf.knnMatch(descriptors1_akaze, descriptors2_akaze, k=2)

    # Apply Lowe's ratio test to filter good matches for each method
    good_matches_orb = []
    for m, n in matches_orb:
        if m.distance < 0.75 * n.distance:
            good_matches_orb.append(m)

    good_matches_sift = []
    for m, n in matches_sift:
        if m.distance < 0.75 * n.distance:
            good_matches_sift.append(m)

    good_matches_akaze = []
    for m, n in matches_akaze:
        if m.distance < 0.75 * n.distance:
            good_matches_akaze.append(m)

    # Calculate matching percentages for each method
    percentage_orb = len(good_matches_orb) / max(len(keypoints1_orb), len(keypoints2_orb)) * 100
    percentage_sift = len(good_matches_sift) / max(len(keypoints1_sift), len(keypoints2_sift)) * 100
    percentage_akaze = len(good_matches_akaze) / max(len(keypoints1_akaze), len(keypoints2_akaze)) * 100

    # Display matching percentages on the second image
    print(f"ORB Match: {percentage_orb}")
    print(f"SIFT Match: {percentage_sift}")
    print(f"AKAZE Match: {percentage_akaze}")
    with open('videoMatch.csv','a') as file:
        file.write(f"{percentage_orb},{percentage_sift},{percentage_akaze}\n")

# Display the resulting image with matching percentages
# cv_imshow(result_image)
Frame = []
count = 0
while True:
    print("Adding Image")
    r,f = capture.read()
    if not r:
        break
    Frame.append(f)
    # print(len(Frame))
    cv.imshow("Video",Frame[count])
    if cv.waitKey(20) and (0xFF==ord('d')):
        break
    count = count + 1

cv.imshow("Frame 1",Frame[300])
cv.imshow("Frame 2",Frame[321])
cv.waitKey(0)


with open('videoMatch.csv','w') as file:
    file.write("ORB,SIFT,AKAZE\n")
for i in range(1,len(Frame)):
    matchThreeType(Frame[i-1],Frame[i])