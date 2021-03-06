﻿# GIPHYVision
<h2>Inspirtation</h2>
Each member of the group recognized the importance of GIFs when communicating with others digitally. Similar to emoticons, GIFs have the ability to potray a wide-range of emotions with a simple image. Searching for GIFs often involves typing; we built GIPHYVision to make it even easier to find the perfect GIF!!!

<h2>What it does</h2>
GiphyVision takes a snapshot of the user and returns a related GIF based on their portrayed emotion.

<h2>How we built</h2>
On the front-end, we used Flask. With the back-end we built GIPHYVision by integrating the Microsoft Azure Emotion API and a GIPHY API. Using the Python OpenCV library, we ask the user to take an image of themselves portraying a specific emotion The Emotion API then takes this image and calculates the "confidence" (i.e. likelihood that a specific emotion is being displayed in the image) for a preset number of emotions. Our time slightly modified this API to only return the emotion with the highest confidence score. Next, we would send the generated emotion from the Emotion API through the GIPHY API that takes a word and returns a specified number of related GIFs.

<h2>Challenges we ran into integrating</h2>
Our team is fairly new to hacking so, in addition to being introduced to new concepts (webapp, Flask, javascript, etc), we had to simultaneously apply these "loosely" developed skills to our project.

<h2>Accomplishments that were proud of</h2>
Our team is very proud that we were able to make a presentable, final product within the time given (considering our limited experience).

<h2>What we learned</h2>
The major concepts we were introduced to are the following: integrating APIs, Flask/webapp development, importing and utilizing different python libraries, and using terminals.

<h2>What's next</h2>
We hope to make a GIPHYVision app that is more accessible by exlporing other features of Flask and maybe make use of Ngrok!
