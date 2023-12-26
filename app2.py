from flask import Flask, render_template, jsonify
import threading
import speech_recognition as sr
import webbrowser

app = Flask(__name__)

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

search_triggered = False

def continuous_listen():
    global search_triggered
    while search_triggered:
        command = listen()
        if "exit" in command:
            print("Exiting continuous listen...")
            search_triggered = False  # Reset the flag to allow retriggering
            break
        else:
            perform_action(command)

def start_continuous_listen():
    threading.Thread(target=continuous_listen).start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute_command', methods=['GET'])
def execute_command():
    command = listen()
    if "exit" in command:
        print("Exiting...")
        return jsonify({'status': 'Command execution stopped.'})
    else:
        perform_action(command)
        return jsonify({'status': 'Command executed.'})

if __name__ == "__main__":
    app.run(debug=True)
