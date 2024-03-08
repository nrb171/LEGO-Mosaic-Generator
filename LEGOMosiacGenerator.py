import PIL 
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Load an image file
image = Image.open("image.jpg")

# crop outer border
amount = 50
image = image.crop((amount, amount, image.width-amount, image.height-amount))

# increase contrast
image = PIL.ImageOps.autocontrast(image, cutoff=0)

# increase sharpness



# Display the image
plt.imshow(image)
plt.axis('off')
plt.show()

#downscale the image
numberOfTiles = 3
pixelsPerTile = 18
subImage = image.resize((numberOfTiles*pixelsPerTile+2, numberOfTiles*pixelsPerTile+2), resample=Image.HAMMING)
image = image.resize((numberOfTiles*pixelsPerTile, numberOfTiles*pixelsPerTile), resample=Image.HAMMING)

image = image.convert("RGB")

# set colors and part IDs to use
colors = ["Dark Green", "Vibrant Yellow", "Nougat", "Medium Blue", "Spring Yellowish Green", "Light Purple", "Bright Yellowish Green", "Sand Blue", "Sand Yellow", "Dark Orange", "Dark Azur", "Flame Yellowish Orange", "Bright Purple", "Aqua", "Vibrant Coral", "Silver Metallic", "Warm Gold", "Bright Green", "Medium Azur", "Bright Reddish Violet", "Dark Brown", "Bright Bluish Green", "Bright Orange", "Bright Blue", "Light Nougat", "Dark Stone Grey", "Medium Nougat", "Reddish Brown", "Dark Red", "Bright Yellow", "Bright Red", "Brick Yellow", "White", "Black", "Olive Green", "Earth Blue"]
elementIDs = [6396247, 6376825, 6343472, 6284602, 6284598, 6284587, 6284583, 6322842, 6322841, 6322840, 6322824, 6322822, 6322821, 6322818, 6311436, 6238890, 6238891, 6353793, 6322819, 6322816, 6322813, 6311437, 6284582, 6284575, 6315196, 6284596, 6284589, 6284586, 6284585, 6284577, 6284574, 6284573, 6284572, 6284070, 6284595, 6284584]
colors = {
    'Dark Green': (0, 100, 0),
    'Vibrant Yellow': (255, 221, 0),
    'Nougat': (250, 193, 137),
    'Medium Blue': (102, 153, 204),
    'Spring Yellowish Green': (204, 255, 102),
    'Light Purple': (229, 204, 255),
    'Bright Yellowish Green': (176, 255, 0),
    'Sand Blue': (116, 134, 157),
    'Sand Yellow': (194, 178, 128),
    'Dark Orange': (204, 85, 0),
    'Dark Azur': (70, 155, 195),
    'Flame Yellowish Orange': (255, 163, 0),
    'Bright Purple': (204, 0, 204),
    'Aqua': (0, 255, 255),
    'Vibrant Coral': (255, 85, 127),
    'Silver Metallic': (192, 192, 192),
    'Warm Gold': (255, 215, 0),
    'Bright Green': (0, 255, 0),
    'Medium Azur': (60, 180, 220),
    'Bright Reddish Violet': (204, 0, 102),
    'Dark Brown': (85, 34, 0),
    'Bright Bluish Green': (0, 204, 204),
    'Bright Orange': (255, 85, 0),
    'Bright Blue': (0, 0, 255),
    'Light Nougat': (255, 204, 153),
    'Dark Stone Grey': (99, 95, 98),
    'Medium Nougat': (204, 142, 105),
    'Reddish Brown': (105, 64, 40),
    'Dark Red': (139, 0, 0),
    'Bright Yellow': (255, 255, 0),
    'Bright Red': (255, 0, 0),
    'Brick Yellow': (243, 207, 155),
    'White': (255, 255, 255),
    'Black': (0, 0, 0),
    'Olive Green': (128, 128, 0),
    'Earth Blue': (0, 32, 96)
}

# plot these colors with labels
fig, ax = plt.subplots()
for i, color in enumerate(colors):
    ax.add_patch(plt.Rectangle((0, i), 1, 1, color=(colors[color][0]/255, colors[color][1]/255, colors[color][2]/255)))
    ax.text(1.5, i+0.5, color, va='center')
ax.set_xlim(0, 2)
ax.set_ylim(0, len(colors))
ax.axis('off')
plt.show()

# Match colors in the image to the closest color in the LEGO palette
def matchColor(color):
    minDist = 99999999
    closestColor = "White"
    for c in colors:
        dist = ((color[0]-colors[c][0])**2 + (color[1]-colors[c][1])**2 + (color[2]-colors[c][2])**2)**0.5
        if dist < minDist:
            minDist = dist
            closestColor = c
    return closestColor

# Create a mosaic of the image using the LEGO colors
mosaic = Image.new("RGB", (numberOfTiles*pixelsPerTile, numberOfTiles*pixelsPerTile))

for i in range(0, numberOfTiles*pixelsPerTile, 1):
    for j in range(0, numberOfTiles*pixelsPerTile, 1):
        color = image.getpixel((i, j))
        closestColor = matchColor(color)
        mosaic.paste(colors[closestColor], (i, j, i+1, j+1))
"""
nubMosaic = Image.new("RGB", (numberOfTiles*pixelsPerTile, numberOfTiles*pixelsPerTile))
for i in range(0, numberOfTiles*pixelsPerTile, 1):
    for j in range(0, numberOfTiles*pixelsPerTile, 1):
        dr = (image.getpixel((i, j))[0] - mosaic.getpixel((i, j))[0])
        dg = (image.getpixel((i, j))[1] - mosaic.getpixel((i, j))[1])
        db = (image.getpixel((i, j))[2] - mosaic.getpixel((i, j))[2])
        closestColor = matchColor((dr, dg, db))
        nubMosaic.paste(colors[closestColor], (i, j, i+1, j+1))
        """

subMosaic = Image.new("RGB", (numberOfTiles*pixelsPerTile, numberOfTiles*pixelsPerTile))
nubMosaic = np.zeros((numberOfTiles*pixelsPerTile, numberOfTiles*pixelsPerTile))
for i in range(0, numberOfTiles*pixelsPerTile, 1):
    for j in range(0, numberOfTiles*pixelsPerTile, 1):
        mr = mosaic.getpixel((i, j))[0]
        mg = mosaic.getpixel((i, j))[1]
        mb = mosaic.getpixel((i, j))[2]
        dr = (image.getpixel((i, j))[0] - mr*np.pi/4)/(1-np.pi/4)
        dg = (image.getpixel((i, j))[1] - mg*np.pi/4)/(1-np.pi/4)
        db = (image.getpixel((i, j))[2] - mb*np.pi/4)/(1-np.pi/4)
        closestColor = matchColor((dr, dg, db))
        subMosaic.paste(colors[closestColor], (i, j, i+1, j+1))

        
        darkener = np.mean((np.array(image.getpixel((i,j)))-(np.array(colors[closestColor])*(1-np.pi/4) + np.array((mr*np.pi/4, mg*np.pi/4, mb*np.pi/4)))))
        # check if darkening is needed
         
        if darkener < -5:
            nubMosaic[i, j] = 1


xGrid = np.arange(0.5, mosaic.size[0]+0.5, 1)
yGrid = -np.arange(0.5, mosaic.size[1]+0.5, 1)
[x, y] = np.meshgrid(xGrid, np.flip(yGrid))

#circular patch of size 1
for i in range(0, numberOfTiles*pixelsPerTile-1, 1):
    for j in range(0, numberOfTiles*pixelsPerTile-1, 1):
        plt.gca().add_patch(plt.Rectangle((xGrid[i]-0.5, yGrid[j]-0.5), 1, 1, color=(subMosaic.getpixel((i, j))[0]/255, subMosaic.getpixel((i, j))[1]/255, subMosaic.getpixel((i, j))[2]/255)))
        plt.gca().add_patch(plt.Circle((xGrid[i], yGrid[j]), 0.48, color=(mosaic.getpixel((i, j))[0]/255, mosaic.getpixel((i, j))[1]/255, mosaic.getpixel((i, j))[2]/255)))
        if nubMosaic[i, j] == 1:
            shadowCoef = 0.6
            nubColor = (mosaic.getpixel((i, j))[0]/255*shadowCoef , mosaic.getpixel((i, j))[1]/255*shadowCoef, mosaic.getpixel((i, j))[2]/255*shadowCoef)
            plt.gca().add_patch(plt.Circle((xGrid[i], yGrid[j]-0.12), 0.25, color=nubColor))
            plt.gca().add_patch(plt.Circle((xGrid[i], yGrid[j]), 0.25, color=(mosaic.getpixel((i, j))[0]/255, mosaic.getpixel((i, j))[1]/255, mosaic.getpixel((i, j))[2]/255)))
        

plt.ylim(0, -numberOfTiles*pixelsPerTile)
plt.xlim(0, numberOfTiles*pixelsPerTile)

plt.gca().invert_yaxis()

plt.axis('equal')
plt.axis('off')

# Save the mosaic high resolution 
plt.savefig("mosaic.png", dpi=500, bbox_inches='tight', pad_inches=0)