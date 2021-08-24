import os
import datetime
import gtts

mySpeech = gtts.gTTS(text="Hi there, hope you are learning new things. Welcome to this world, you can do really great Abbas.",lang='en', slow=False)
mySpeech.save("output.mp3")
os.system("output.mp3")
