import speech_recognition as sr

def capture_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Please speak now. You have up to 60 seconds.")
        try:
            audio = r.listen(source, timeout=60, phrase_time_limit=60)
        except sr.WaitTimeoutError:
            print("⏰ No speech detected within 60 seconds.")
            return None
        try:
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("🤷 Couldn't understand the speech.")
            return None
        except sr.RequestError as e:
            print(f"❌ Google API error: {e}")
            return None

