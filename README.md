# Cooldown Buddy
Hi! I'm Callum Choi, a student at the University of Waterloo who is passionate about games. I developed Cooldown Buddy as a tool for League of Legends players to quickly and easily find the cooldowns of allies and enemies.

# Installation
As of Version 0.1, as a work in progress initial release, installation is a bit difficult right now.

First, download Visual Studio Code (https://code.visualstudio.com/), and the cd_grabber.py file. 

Follow set-up instructions and click "New file +". From there, click the blue "Select a language" and select Python, and follow set-up instructions for Python.

Import the cd_grabber.py by clicking "Open file" and finding where the cd_grabber.py file is located.

Then, press Ctrl + \` to open the terminal. Input "pip install requests".

Furthermore, for version 0.1, you must create and input your own API key (this is an unfortunate side effect of the current design of the product, this will be improved in version 0.2)

This is done by accessing https://developer.riotgames.com/ and creating a Riot Account. Then, go back to https://developer.riotgames.com/ and scroll down to the Development API Key and generate a new API key.

Input this API key into line 5 of cd_grabber.py.

From there, click the Run button in the top left!

# Tech Stack Used
Python, Riot RESTful API, Data Dragon (JSON Database), Visual Studio Code

# Features to Add
Make the application easier to install, and easier to use (GUI)
Visual interface (Pictures of abilities instead of Q W E R)
Demo Mode

# Closing Notes
Although a work in progress, I did learn a lot about both Python and RESTful APIs getting this project to this stage, and I hope to learn more! Thanks for checking this out.
