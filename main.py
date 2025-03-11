import imageio.v3 as imageio

#List of images from the same folder
filenames = ['dog3.jpg', 'dog2.jpg', 'dog1.jpg']
images = []

for filename in filenames:
	images.append(imageio.imread(filename))

#Save the images as a gif
imageio.imwrite('dogo.gif', images, duration=500, loop=0)