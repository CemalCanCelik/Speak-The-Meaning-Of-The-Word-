import pyttsx3
from PyDictionary import PyDictionary

class Speaking:
    def speak(self, audio):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(audio)
        engine.runAndWait()

class CodingKnowledge:
    def Dictionary(self):
        speak = Speaking()
        dic = PyDictionary()
        speak.speak("Which word do you want to find the meaning of:")
        query = str(input())
        word = dic.meaning(query)
        
        if word:  
            for state in word:
                meanings = ', '.join(word[state])
                print(f"{state}: {meanings}")
                speak.speak(f"The meaning is {meanings}")
        else:
            speak.speak("Sorry, I couldn't find the meaning of that word.")

if __name__ == '__main__':
    knowledge = CodingKnowledge()
    knowledge.Dictionary()
