import speech_recognition as sr
import webbrowser

# Initialize recognizer
recognizer = sr.Recognizer()

# Function to perform actions based on commands
def perform_action(command):
    if "search" in command:
        query = command.split("search", 1)[1].strip()
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        return True
    else:
        return False

# Function to listen to voice commands
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        recognized_text = recognizer.recognize_google(audio)
        print(f"You said: {recognized_text}")
        return recognized_text.lower()  # Convert recognized text to lowercase
    except sr.UnknownValueError:
        print("Could not understand the audio")
        return ""
    except sr.RequestError as e:
        print(f"Error: {e}")
        return ""

# Continuous listening loop
search_triggered = False
while True:
    if not search_triggered:
        command = listen()
        if "exit" in command:
            print("Exiting...")
            break
        else:
            search_triggered = perform_action(command)
    else:
        # Waits for new command or exits the loop
        command = listen()
        if "exit" in command:
            print("Exiting...")
            break
        else:
            search_triggered = perform_action(command)
