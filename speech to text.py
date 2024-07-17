import speech_recognition as sr

def speech_to_text():
    # Initialize recognizer class (for recognizing speech)
    recognizer = sr.Recognizer()

    # Capture audio from the default microphone
    with sr.Microphone() as source:
        print("Listening... (Speak for 5 seconds)")
        # Adjust for ambient noise levels
        recognizer.adjust_for_ambient_noise(source)
        
        # Record audio for 5 seconds
        audio_data = recognizer.record(source, duration=5)

        # Use Google Web Speech API to perform speech recognition
        try:
            text = recognizer.recognize_google(audio_data)
            print(f"Question: {text}")
            
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Error fetching results; {e}")
        
if __name__ == "__main__":
    speech_to_text()
