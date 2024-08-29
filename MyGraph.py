import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()


#step 1 - create a virtual environment 
#command : py -3 -m venv NAMEOFVENV

#step 2
#Activate your virtual environment 
#directory location : myvenv/Scripts/activate

#step 3
#install 3rd party library 
#pip3 install matplotlib

#difference between source control and version control 
#version control - everything related to your project (hdml, css, photos, videos)
#source control - talking specifically about source code (only css and hdml)
#only dealing with source control in vs code