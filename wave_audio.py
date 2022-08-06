import wave
#The audio file has to be in .wav format
obj = wave.open("testaudio.wav","rb")#replace 'testaudio.wav' with your own file name
#Getter functions
print("Number of channels: ",obj.getnchannels())
print("Sample width: ",obj.getsampwidth())
print("Framerate: ",obj.getframerate())
print("Number of frames: ",obj.getnframes)
print("Parameters: ",obj.getparams())


t_audio = obj.getnframes()/obj.getframerate()#this is used to get the duration of the audio
print("Duration of the audio: ",t_audio)



frames = obj.readframes(-1)
print(type(frames),type(frames[0]))#This will return 'byte', since byte is made up of integers, frames[n] will return int
print(len(frames))
obj.close()


#To save the data
obj_new = wave.open("newtestaudio.wav","wb")
#Setter functions
obj_new.setnchannels(3)
obj_new.setsampwidth(4)
obj_new.setframerate(30000.0)

obj_new.writeframes(frames)
obj_new.close()
