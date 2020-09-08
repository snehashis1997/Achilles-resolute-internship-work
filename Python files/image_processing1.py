
import cv2
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

img = cv2.imread(r"E:\achlies_resoulute_project\arindam_maitra_project_dataset\my_data\84images\54.png")
b,g,r = cv2.split(img)
bins = np.arange(0,np.max(b),2)

plt.hist(r.flatten(),bins=bins)
plt.xlabel("Pixel values")
plt.ylabel("Pixel counts")
plt.title("Histogram plot of R channel");

img = cv2.imread(r"E:\achlies_resoulute_project\arindam_maitra_project_dataset\my_data\TORTUIOSITY\TORTUIOSITY\ROP\temp\imgs\104.png")
img = cv2.GaussianBlur(img,(5,5),0)
b,g,r = cv2.split(img)
#r = r*2
g = g//3
b = b//3
bins = np.arange(0,np.max(b),2)
plt.imshow(img);

plt.hist(g.flatten(),bins=bins)
plt.xlabel("Pixel values")
plt.ylabel("Pixel counts")
plt.title("Histogram plot of G channel");

img = cv2.merge((r,g,b))

plt.imshow(img)
plt.axis("off")
plt.title("After fixing red channel issue")
