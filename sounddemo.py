#step 1 - import lib
import cmu_sphinx4

#step2 - read audit file 
audio_URL = 'http://www.music.helsinki.fi/tmt/opetus/uusmedia/esim/a2002011001-e02-16kHz.wav'
transcriber = cmu_sphinx4.Transcriber(audio_URL)

#step3 - Print it out 
for line in transcriber.transcript_stream():
	print(line)
	