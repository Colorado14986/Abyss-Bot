import pyttsx3
engine = pyttsx3.init()
sentence = 'This is a longer test hopefully it goes ok'
engine.setProperty('rate', 100)
engine.save_to_file(sentence , 'latestTTS.mp3')
engine.runAndWait()
