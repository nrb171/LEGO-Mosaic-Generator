# LEGO-Mosaic-Generator
## Introduction
My wife wanted to make a LEGO portrait, but all of the tools available online did not meet my expectations — so, I wrote this tool.

| Before                               | After                                |
| ------------------------------------ | ------------------------------------ |
| ![](https://i.imgur.com/ZymZOkX.png) | ![](https://i.imgur.com/Ic3sZjC.png) |
Hint: you may want to squint, the effect is much easier to see.

## Methodology
0. Downscale the initial image using a Hamming filter.
	1. Hamming seemed to do the best job to preserve important image features. Other options may include Lanczos or Cubic filters.
1. Identify the closest LEGO color to the color of each pixel
2. Identify an appropriate "adjustment" color to bring the entire pixel closer to the original image
	1. Take into account uncovered corners of the pixel
	2. We can use nubs or flats to darken/lighten the pixel by accounting for extra shadows.

![](https://i.imgur.com/M2r33WN.png)


## Roadmap
- [ ] Macro-pixel calculation
	- Account for large-scale features that could be addressed with pieces like this:
		- ![](https://i.imgur.com/mcuJutM.png)
		- ![](https://i.imgur.com/OB2ZTdb.png)
- [ ] Transparent bricks
- [ ] Final piece calculation and price/piece/complexity optimization
- [ ] Assembly instructions.
