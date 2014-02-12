import tkFileDialog
import wave
import struct
import pyaudio
from Tkinter import *
import os
import signal

def pl():
	chunk=1024
	cur=os.getcwd()
	cur+=str("/output.wav")
	wf=wave.open(cur,'rb')
	p=pyaudio.PyAudio()
	stream=p.open(
		format=p.get_format_from_width(wf.getsampwidth()),
		channels=wf.getnchannels(),
		rate=wf.getframerate(),
		output=True
	)
	data=wf.readframes(chunk)
	while data!= '':
		stream.write(data)
		data=wf.readframes(chunk)
	stream.close()
	p.terminate()
def pl1():
	chunk=1024
	cur=os.getcwd()
	cur+=str("/rec.wav")
	wf=wave.open(cur,'rb')
	p=pyaudio.PyAudio()
	stream=p.open(
		format=p.get_format_from_width(wf.getsampwidth()),
		channels=wf.getnchannels(),
		rate=wf.getframerate(),
		output=True
	)
	data=wf.readframes(chunk)
	while data!= '':
		stream.write(data)
		data=wf.readframes(chunk)
	stream.close()
	p.terminate()
def pl2():
	chunk=1024
	cur=os.getcwd()
	cur+=str("/output1.wav")
	wf=wave.open(cur,'rb')
	p=pyaudio.PyAudio()
	stream=p.open(
		format=p.get_format_from_width(wf.getsampwidth()),
		channels=wf.getnchannels(),
		rate=wf.getframerate(),
		output=True
	)
	data=wf.readframes(chunk)
	while data!= '':
		stream.write(data)
		data=wf.readframes(chunk)
	stream.close()
	p.terminate()

def mixing():
	SHRT_MIN=-32767 - 1
	SHRT_MAX=32767
	fl1=0
	fl2=0
	fl3=0
	if user1.checkitvar3.get()==1:           
		fl1=1
	if user2.checkitvar3.get()==1:
		fl2=1
	if user3.checkitvar3.get()==1:
		fl3=1
	if (fl1==1 & fl2==1) or (fl2==1 & fl3==1) or (fl1==1 & fl3==1):
		if (fl1==1 & fl2==1):
			data=user1.readfile(1)
			data2=user2.readfile(2)
			fi = wave.open('output_file1.wav',"rb")
			fi2 = wave.open('output_file2.wav',"rb")
	  	elif (fl1==1 & fl3==1):
			data=user1.readfile(1)
	  		data2=user3.readfile(3)
			fi = wave.open('output_file1.wav',"rb")
			fi2 = wave.open('output_file3.wav',"rb")
		elif (fl2==1 & fl3==1):
			data=user2.readfile(2)
			data2=user3.readfile(3)
			fi = wave.open('output_file2.wav',"rb")
			fi2 = wave.open('output_file3.wav',"rb")
		fo = wave.open("output.wav","w")
		fo.setparams(fi.getparams())
		width=fi.getsampwidth()
		width2=fi2.getsampwidth()      
		if width<width2:
			width=width2
		fmts=(None, "=B", "=h", None, "=l")
		fmt=fmts[width]
		dcs=(None, 128, 0, None, 0)
		dc=dcs[width]
		if fi.getnframes()>fi2.getnframes():
			maxi=fi.getnframes()
			flag=1         
		else:
			maxi=fi2.getnframes()
			flag=2
		amp=[]
		print flag
		for i in range(maxi):
			if flag==1 and i>=fi2.getnframes():
				if data[i]<SHRT_MIN:
					iframe=SHRT_MIN
				elif data[i]>SHRT_MAX:
					iframe=SHRT_MAX
				else:
					iframe=data[i]
			elif flag==2 and i>=fi.getnframes():
				if data2[i]<SHRT_MIN:
					iframe=SHRT_MIN
				elif data2[i]>SHRT_MAX:
					iframe=SHRT_MAX
				else:
					iframe=data2[i]
			else:
				if data2[i]+data[i]<SHRT_MIN:
					iframe=SHRT_MIN
				elif data2[i]+data[i]>SHRT_MAX:
					iframe=SHRT_MAX
				else:
					iframe=data2[i]+data[i]
			iframe-=dc
			oframe=iframe/2;
			oframe+=dc
			oframe=struct.pack(fmt, oframe)
			fo.writeframes(oframe)
		fi.close()
		fo.close()
		pl();
	elif (fl1==1 & fl2==1 & fl3==1):
		data=user1.readfile(1)
		data2=user2.readfile(2)    
		data3=user3.readfile(3)
		fi = wave.open('output_file1.wav',"rb")
		fi2 = wave.open('output_file2.wav',"rb")
		fi3 = wave.open('output_file3.wav',"rb")
		fo = wave.open("output.wav","w")
		fo.setparams(fi.getparams())
		width=fi.getsampwidth()
		width2=fi2.getsampwidth()
	 	width3=fi3.getsampwidth()      
	 	if width<width2:
	 		width=width2
	 	if width<width3:
			width=width3
		fmts=(None, "=B", "=h", None, "=l")
		fmt=fmts[width]
		dcs=(None, 128, 0, None, 0)
		dc=dcs[width]
		if fi.getnframes()>fi2.getnframes():
			maxi=fi.getnframes()
			flag=1         
		else:
			maxi=fi2.getnframes()
			flag=2
		if fi3.getnframes()>maxi:
			maxi=fi3.getnframes()
			flag=3
		amp=[]
		for i in range(maxi):
			if flag==1 and i>=fi2.getnframes():
				if data[i]<SHRT_MIN:
					iframe=SHRT_MIN
				elif data[i]>SHRT_MAX:
					iframe=SHRT_MAX
				else:
					iframe=data[i]
			elif flag==2 and i>=fi.getnframes():
				if data2[i]<SHRT_MIN:
					iframe=SHRT_MIN
				elif data2[i]>SHRT_MAX:
					iframe=SHRT_MAX
				else:
					iframe=data2[i]
			elif flag==3 and i>=fi3.getnframes():
				if data3[i]<SHRT_MIN:
					iframe=SHRT_MIN
				elif data3[i]>SHRT_MAX:
					iframe=SHRT_MAX
				else:
					iframe=data3[i]
			else:
				if data2[i]+data[i]+data3[i]<SHRT_MIN:
					iframe=SHRT_MIN
				elif data2[i]+data[i]+data3[i]>SHRT_MAX:
					iframe=SHRT_MAX
				else:
					iframe=data2[i]+data[i]+data3[i]
#       print int(iframe)
			iframe-=dc
			oframe=iframe/2;
			oframe+=dc
			oframe=struct.pack(fmt, oframe)
			fo.writeframes(oframe)
		fi.close()
		fo.close()
		pl()
def modulation():
	SHRT_MIN=-32767 - 1
	SHRT_MAX=32767
	fl1=0
	fl2=0
	fl3=0
	if user1.checkitvar2.get()==1:           
		fl1=1
	if user2.checkitvar2.get()==1:
		fl2=1
	if user3.checkitvar2.get()==1:
		fl3=1
	if (fl1==1 & fl2==1) or (fl2==1 & fl3==1) or (fl1==1 & fl3==1):
		if (fl1==1 & fl2==1):
			data=user1.readfile(1)
			data2=user2.readfile(2)
			fi = wave.open('output_file1.wav',"rb")
			fi2 = wave.open('output_file2.wav',"rb")
	  	elif (fl1==1 & fl3==1):
			data=user1.readfile(1)
	  		data2=user3.readfile(3)
			fi = wave.open('output_file1.wav',"rb")
			fi2 = wave.open('output_file3.wav',"rb")
		elif (fl2==1 & fl3==1):
			data=user2.readfile(2)
			data2=user3.readfile(3)
			fi = wave.open('output_file2.wav',"rb")
			fi2 = wave.open('output_file3.wav',"rb")
		fo = wave.open("output1.wav","w")
		fo.setparams(fi.getparams())
		width=fi.getsampwidth()
		width2=fi2.getsampwidth()      
		if width>width2:
			width=width2
		fmts=(None, "=B", "=h", None, "=l")
		fmt=fmts[width]
		dcs=(None, 128, 0, None, 0)
		dc=dcs[width]
		if fi.getnframes()<fi2.getnframes():
			maxi=fi.getnframes()
			flag=1         
		else:
			maxi=fi2.getnframes()
			flag=2
		amp=[]
		for i in range(maxi):
			if flag==1 and i>=fi2.getnframes():
				if data[i]<SHRT_MIN:
					iframe=SHRT_MIN
				elif data[i]>SHRT_MAX:
					iframe=SHRT_MAX
				else:
					iframe=data[i]
			elif flag==2 and i>=fi.getnframes():
				if data2[i]<SHRT_MIN:
					iframe=SHRT_MIN
				elif data2[i]>SHRT_MAX:
					iframe=SHRT_MAX
				else:
					iframe=data2[i]
			else:
				if data2[i]*data[i]<SHRT_MIN:
					iframe=SHRT_MIN
				elif data2[i]*data[i]>SHRT_MAX:
					iframe=SHRT_MAX
				else:
					iframe=data2[i]*data[i]
			iframe-=dc
			oframe=iframe/2;
			oframe+=dc
			oframe=struct.pack(fmt, oframe)
			fo.writeframes(oframe)
		fi.close()
		fo.close()
		pl2()
	elif (fl1==1 & fl2==1 & fl3==1):
		data=user1.readfile(1)
		data2=user2.readfile(2)    
		data3=user3.readfile(3)
		fi = wave.open('output_file1.wav',"rb")
		fi2 = wave.open('output_file2.wav',"rb")
		fi3 = wave.open('output_file3.wav',"rb")
		fo = wave.open("output1.wav","w")
		fo.setparams(fi.getparams())
		width=fi.getsampwidth()
		width2=fi2.getsampwidth()
	 	width3=fi3.getsampwidth()      
	 	if width>width2:
	 		width=width2
	 	if width>width3:
			width=width3
		fmts=(None, "=B", "=h", None, "=l")
		fmt=fmts[width]
		dcs=(None, 128, 0, None, 0)
		dc=dcs[width]
		if fi.getnframes()<fi2.getnframes():
			maxi=fi.getnframes()
			flag=1         
		else:
			maxi=fi2.getnframes()
			flag=2
		if fi3.getnframes()<maxi:
			maxi=fi3.getnframes()
			flag=3
		amp=[]
		for i in range(maxi):
			if flag==1 and i>=fi2.getnframes():
				if data[i]<SHRT_MIN:
					iframe=SHRT_MIN
				elif data[i]>SHRT_MAX:
					iframe=SHRT_MAX
				else:
					iframe=data[i]
			elif flag==2 and i>=fi.getnframes():
				if data2[i]<SHRT_MIN:
					iframe=SHRT_MIN
				elif data2[i]>SHRT_MAX:
					iframe=SHRT_MAX
				else:
					iframe=data2[i]
			elif flag==3 and i>=fi3.getnframes():
				if data3[i]<SHRT_MIN:
					iframe=SHRT_MIN
				elif data3[i]>SHRT_MAX:
					iframe=SHRT_MAX
				else:
					iframe=data3[i]
			else:
				if data2[i]*data[i]*data3[i]<SHRT_MIN:
					iframe=SHRT_MIN
				elif data2[i]*data[i]*data3[i]>SHRT_MAX:
					iframe=SHRT_MAX
				else:
					iframe=data2[i]*data[i]*data3[i]
#       print int(iframe)
			iframe-=dc
			oframe=iframe/2;
			oframe+=dc
			oframe=struct.pack(fmt, oframe)
			fo.writeframes(oframe)
		fi.close()
		fo.close()
		pl2()

def callback():
    wf=wave.open('output_file.wav','rb')
    #data = wf.readframes(frame_coun)
    data = wf.getframerate()
    global pflag
    if pflag:
	return (data, pyaudio.paContinue)
    else:
	return (data, pyaudio.paAbort)

class AudioFile:
    chunk = 1024

    def __init__(self):
        """ Init audio stream """
	self.playflag=0
	self.pauseflag=0

    def play(self,fileit):
        """ Play entire file """
	if(self.pauseflag==1):
		#Continue the process
		self.pauseflag=0
		self.playflag=1
	    	os.kill(self.pid,signal.SIGCONT)
	else:
		self.pid=os.fork()
		if(self.pid==0):
        		self.wf = wave.open(fileit, 'rb')
			self.playflag=0
			self.pauseflag=0
			self.pid=0
        		self.p = pyaudio.PyAudio()
		        self.stream = self.p.open(
	        	    format = self.p.get_format_from_width(self.wf.getsampwidth()),
        	    	channels = self.wf.getnchannels(),
	            	rate = self.wf.getframerate(),
        	    	output = True
		        )
			self.play=1
			self.pause=0
       			data = self.wf.readframes(self.chunk)
		        while data != '':
        		    self.stream.write(data)
	        	    data = self.wf.readframes(self.chunk)
        		self.stream.close()
	        	self.p.terminate()
	  		exit(0)

    def pause(self):
	    self.playflag=0
	    self.pauseflag=1
	    os.kill(self.pid,signal.SIGSTOP)

'''def record():
	chunk=1024
	arr=[]
	FORMAT=pyaudio.paInt16
	channelsit=1
	rateit=44100
	record_seconds=5
	p=pyaudio.PyAudio()
	stream=p.open(format=FORMAT, channels=channelsit,rate=rateit,input=True,output=True,frames_per_buffer=chunk)
	for i in range(0,44100/chunk*record_seconds):
		data=stream.read(chunk)
		arr.append(data)
	wf=wave.open("rec.wav",'wb')
	wf.setnchannels(channelsit)
			exit(0)

    def close(self):
        """ Graceful shutdown """ 
        self.stream.close()
        self.p.terminate()

    def pause(self):
	    self.playflag=0
	    self.pauseflag=1
	    os.kill(self.pid,signal.SIGSTOP)'''

def record():
	chunk=1024
	arr=[]
	FORMAT=pyaudio.paInt16
	channelsit=1
	rateit=44100
	record_seconds=5
	p=pyaudio.PyAudio()
	stream=p.open(format=FORMAT, channels=channelsit,rate=rateit,input=True,output=True,frames_per_buffer=chunk)
	for i in range(0,44100/chunk*record_seconds):
		data=stream.read(chunk)
		arr.append(data)
	wf=wave.open("rec.wav",'wb')
	wf.setnchannels(channelsit)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(rateit)
	wf.writeframes(b''.join(arr))
	wf.close()
	stream.stop_stream()
	stream.close()
	p.terminate()

class Wave_Mixer():

	def __init__(self,input_file):	
		## Input music file and its attributes
		music_file = wave.open(input_file, 'rb')
		self.type_channel = music_file.getnchannels()
		self.sample_rate = music_file.getframerate()
		self.sample_width = music_file.getsampwidth()
		self.num_frames = music_file.getnframes()
#self.formated_data=5

		self.raw_data = music_file.readframes( self.num_frames ) # Returns byte data
		music_file.close()

		## Formating raw_data into Integer data

		self.num_samples = self.num_frames * self.type_channel

		if self.sample_width == 1: 
       			fmt = "%iB" % self.num_samples # read unsigned chars
    		elif self.sample_width == 2:
        		fmt = "%ih" % self.num_samples # read signed 2 byte shorts
    		else:
       	 		raise ValueError("Only supports 8 and 16 bit audio formats.")

		self.formated_data = list(struct.unpack(fmt, self.raw_data))
	
	def amplitude_amplification(self,factor):	
		max_amplification = 32767
		min_amplification = -32768
		frm=self.formated_data
		for i in xrange(len(self.formated_data)):
			if self.formated_data[i] * factor > max_amplification:
				self.formated_data[i] = max_amplification
			elif self.formated_data[i] * factor < min_amplification:
				self.formated_data[i] = min_amplification
			else:
				self.formated_data[i] = self.formated_data[i] * factor

	def time_reversal(self):
		if self.type_channel == 1:
			self.formated_data.reverse()
		else:
			self.formated_data.reverse()
			for i in xrange(len(self.formated_data) - 1):
				temp = self.formated_data[i]
				self.formated_data[i] = self.formated_data[i+1]
				self.formated_data[i+1] = temp

	def timeshift(self,factor):
		shift_frames = factor * self.sample_rate
		shift_frames=int(shift_frames)
		if(factor > 0):
			if(self.type_channel == 1):
				a=[]
				for i in range(shift_frames,0,-1):
					a.append(0)
				self.formated_data = a + self.formated_data
			else:
				a=[]
				for i in range(2*shift_frames,0,-1):
					a.append(0)
				self.formated_data = a + self.formated_data
		else:
			if(self.type_channel == 1):
				self.formated_data=self.formated_data[shift_frames::1]
			else:
				self.formated_data=self.formated_data[2*shift_frames::1]

		self.num_frames = len(self.formated_data)/self.type_channel
	def tscale(self,factor):
                a=[]
               
                if(factor == 0):
                        factor=1
               
                if self.type_channel == 1: 
                        k=int(len(self.formated_data)/factor)
                        for i in range(k):
                                a.append(self.formated_data[int(factor*i) ])
                else:
                        e_li=[]
                        o_li=[]
                        for i in range( len(self.formated_data) ):
                                if(i%2 == 0):
                                        e_li.append(self.formated_data[i])
                                else:
                                        o_li.append(self.formated_data[i])
                        k=int(len(e_li)/factor)
                        for i in range(k):
                                a.append(e_li[ int(factor*i) ])
                                a.append(o_li[ int(factor*i) ])
               
                self.formated_data = a                   
                self.num_frames = len(self.formated_data)/self.type_channel
	def pack_file(self,filename):
		if self.sample_width==1: 
			fmt="%iB" % self.num_frames*self.type_channel 
		else: 
			fmt="%ih" % self.num_frames*self.type_channel

		out_data=struct.pack(fmt,*(self.formated_data))
		out_music_file=wave.open(filename,'wb')
		
		out_music_file.setframerate(self.sample_rate) 
		out_music_file.setnframes(self.num_frames) 
		out_music_file.setsampwidth(self.sample_width) 
		out_music_file.setnchannels(self.type_channel)

		out_music_file.writeframes(out_data)
		
		out_music_file.close()

class UI:
	def readfile(self,flag):
		new_object=Wave_Mixer(self.label1['text'])
		ampit=self.amplitude.get()
		timescaleit=self.time_scaling.get()
		timeshiftit=self.time_shift.get()

		new_object.amplitude_amplification(ampit)

		if(self.checkitvar1.get()):
			new_object.time_reversal()
		new_object.timeshift(timeshiftit)
		new_object.tscale(timescaleit)
		if(flag==1):
			new_object.pack_file('output_file1.wav')
#a.play('outputfile1.wav')
		elif(flag==2):
			new_object.pack_file('output_file2.wav')
#a.play('output_file2.wav')
		else:
			new_object.pack_file('output_file3.wav')
#a.play('output_file3.wav')
		return new_object.formated_data
	def file_input(self):
		files=tkFileDialog.askopenfilename()
		self.label1['text']=files
	
	def pause_music(self):
		a.pause()	
	def play_music(self):
		new_object=Wave_Mixer(self.label1['text'])
		ampit=self.amplitude.get()
		new_object.amplitude_amplification(ampit)
		timescaleit=self.time_scaling.get()
		timeshiftit=self.time_shift.get()
		
		if(self.checkitvar1.get()):
			new_object.time_reversal()
		new_object.timeshift(timeshiftit)
		new_object.tscale(timescaleit)
		
		if(self.labelit['text']=="Wave 1"):
			new_object.pack_file('output_file1.wav')
			a.play('output_file1.wav')
		elif(self.labelit['text']=="Wave 2"):
			new_object.pack_file('output_file2.wav')
			a.play('output_file2.wav')
		else:
			new_object.pack_file('output_file3.wav')
			a.play('output_file3.wav')
#play_object.close()

	def __init__(self,root,flag):
		if(flag==1):
			self.labelit=LabelFrame(root,text="Wave 1")
			self.labelit.pack(side=LEFT,fill=None,expand=True)
		elif(flag==2):
			self.labelit=LabelFrame(root,text="Wave 2")
			self.labelit.pack(side=LEFT,fill=None,expand=True)
		else:
			self.labelit=LabelFrame(root,text="Wave 3")
			self.labelit.pack(side=LEFT,fill=None,expand=True)

		self.button=Button(self.labelit,text="Select File",command=self.file_input)
		self.button.pack(side=TOP)
		self.label1=Label(self.labelit,text='')
		self.label1.pack(side=TOP)
			
		self.amplitude=DoubleVar()
		self.scrollbar1 = Scale(self.labelit,label="Amplitude",variable=self.amplitude,from_=0, to=5, orient=HORIZONTAL, resolution=0.1)
		self.scrollbar1.set(0)
		self.scrollbar1.pack(side=TOP, anchor=CENTER)

		self.time_shift=DoubleVar()
		self.scrollbar2 = Scale(self.labelit,label="Time Shift",variable=self.time_shift,from_=-1, to=1, orient=HORIZONTAL, resolution=0.1)
		self.scrollbar2.set(0)
		self.scrollbar2.pack(side=TOP, anchor=CENTER)
		
		self.time_scaling=DoubleVar()
		self.scrollbar3 = Scale(self.labelit,label="Time Scaling",variable=self.time_scaling,from_=0, to=8, orient=HORIZONTAL, resolution=0.1)
		self.scrollbar3.set(0)
		self.scrollbar3.pack(side=TOP, anchor=CENTER)

		self.checkitvar1=IntVar()
		self.check1=Checkbutton(self.labelit,text="Time Reversal",variable=self.checkitvar1,onvalu=1,offvalue=0,height=3,width=21)
		self.check1.pack(side=TOP)

		self.checkitvar2=IntVar()
		self.check2=Checkbutton(self.labelit,text="Select for Modulation",variable=self.checkitvar2,onvalu=1,offvalue=0,height=3,width=21)
		self.check2.pack(side=TOP)
		
		self.checkitvar3=IntVar()
		self.check3=Checkbutton(self.labelit,text="Select for Mixing",variable=self.checkitvar3,onvalu=1,offvalue=0,height=3,width=21)
		self.check3.pack(side=TOP)
		
		self.button1=Button(self.labelit,text="Play",command=self.play_music)
		self.button1.pack(side=TOP)
		
		self.button2=Button(self.labelit,text="Pause",command=self.pause_music)
		self.button2.pack(side=TOP)

builder=Tk()
var=StringVar()
var.set("WAVE MIXER")
label=Label(builder,textvariable=var,relief=RAISED)
label.pack()
lineit=Frame(builder,height=1,width=900,bg="black")
lineit.pack()
user1=UI(builder,1)
user2=UI(builder,2)
user3=UI(builder,3)
a=AudioFile()

buttonit=Button(builder,text="Mix and Play",command=mixing,fg="brown")
buttonit.place(relx=0.2,rely=0.85,anchor=CENTER)

#buttonit=Button(builder,text="Pause",command=a.pause,fg="brown")
#buttonit.place(relx=0.2,rely=0.90,anchor=CENTER)

buttonit1=Button(builder,text="Modulate and Play",command=modulation,fg="brown")
buttonit1.place(relx=0.8,rely=0.85,anchor=CENTER)

buttonit2=Button(builder,text="Record",command=record,fg="brown")
buttonit2.place(relx=0.5,rely=0.86,anchor=CENTER)

buttonit3=Button(builder,text="Play",command=pl1,fg="brown")
buttonit3.place(relx=0.5,rely=0.9,anchor=CENTER)

builder.geometry("800x800+300+300")
builder.mainloop()
