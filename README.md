﻿# giphyvision

What it does
GiphyVision takes a snapshot of the user and returns a related GIF based on their potrayed emotion.

How we built
We built GIPHYVision by intergrating the Microsoft Azure Emotion API and a GIPHY API. Using the Python OpenCV library, we ask the user to take an image of themself potraying a specific emotion The Emotion API then takes this image and calculates the "confidence" (i.e. likelihood that a specific emotion is being displayed in the image) for a preset number of emotions. Our time slightly modified this API to only return the emotion with the highest confidence score. Next, we would send the generated emotion from the Emotion API through the GIPHY API that takes a word and returns a specified number of related GIFs.
