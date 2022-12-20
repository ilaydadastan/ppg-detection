# ROI SELECTION & PPG GRAPH | Video Processing 

In this project, The changes of the pixels on the video were calculated and a photopletsmography graph was created according to time.

### Dependencies

- numpy library
- cv2 library
- matplotlib library        


-----
### Description

- It has been added to the project directory by taking a hand video.

- ROI(region of interest) selection is made on the captured video.

<img width="383" alt="Screenshot 2022-12-13 at 14 49 09" src="https://user-images.githubusercontent.com/43909097/207322664-94be5352-0aa5-4b91-bcca-e6b12b65a39a.png">

- ROI selection is made with mouse movements and the desired frame can be drawn.

- Two points, p1 and p2, determine the frame.

- Then the frame is cropped and the average pixels in the frame are calculated.

- The changes of pixels with respect to time are converted into graph with matplotlib.

<img width="369" alt="Screenshot 2022-12-13 at 14 49 33" src="https://user-images.githubusercontent.com/43909097/207322722-f43ffbc3-9400-45f4-936d-5a6187c5be8f.png">

---
PPG graph image if we shoot a still camera and a still video;

<img width="366" alt="Screenshot 2022-12-20 at 16 04 54" src="https://user-images.githubusercontent.com/43909097/208686017-638ad4cf-3959-4ff4-a801-5b4966d44dce.png">
