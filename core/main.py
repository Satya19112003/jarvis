import threading
from voice import speak, listen
from brain import think
from memory import remember, recall
from vision import recognize_face
from smarthome import lights_on, lights_off
import ui

# -------------------------------
# Launch Iron Man UI in background
# -------------------------------
def start_ui():
    ui.launch_ui()

threading.Thread(target=start_ui, daemon=True).start()

# -------------------------------
# Jarvis Startup
# -------------------------------
speak("Initializing all systems")

# Face recognition security
if recognize_face():
    speak("Face recognized. Access granted.")
else:
    speak("Face not recognized. Limited access mode.")

# Load memory
user_name = recall("name")
if user_name:
    speak(f"Welcome back {user_name}")

# -------------------------------
# Main Command Loop (BRAIN)
# -------------------------------
while True:
    command = listen()

    if not command:
        continue

    # MEMORY
    if "my name is" in command:
        name = command.replace("my name is", "").strip()
        remember("name", name)
        speak(f"I will remember you, {name}")

    # SMART HOME
    elif "lights on" in command:
        lights_on()
        speak("Lights turned on")

    elif "lights off" in command:
        lights_off()
        speak("Lights turned off")

    # EXIT
    elif "shutdown jarvis" in command:
        speak("Shutting down. Goodbye.")
        break

    # AI FALLBACK (LLM)
    else:
        response = think(command)
        speak(response)

