import imageio

# you can add any type of image like png or jpg
filenames = ["R1.jpg", "R2.jpg", "R3.jpg"]

images = []
for filename in filenames:
    images.append(imageio.imread(filename))

imageio.mimsave("RS.gif", images, "GIF", duration=1)
