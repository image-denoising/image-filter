import matplotlib.pyplot as plt
import cv2 as cv
import filters

# load images & testing filter
fig = plt.figure(figsize=(20, 20))
plt.gray()
image = cv.imread("./noised.png", 0)
real = cv.imread("./real.png", 0)
result = filters.amf(image)

# display real image
fig.add_subplot(1, 3, 1)
plt.imshow(real)
plt.axis('off')
plt.title("Original")

# display noised
fig.add_subplot(1, 3, 2)
plt.imshow(image)
plt.axis('off')
plt.title("Noised")

# display result image
fig.add_subplot(1, 3, 3)
plt.imshow(result)
plt.axis('off')
plt.title("Result")

plt.show()
