import os
import tempfile
import sounddevice as sd
import soundfile as sf
import gtts
import speech_recognition as sr
import subprocess

# ---------------- Record audio ----------------
def record_to_wav(duration=8, fs=16000, channels=1):
    print("\n🎤 Speak now for up to", duration, "seconds...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=channels, dtype='int16')
    sd.wait()
    fd, path = tempfile.mkstemp(suffix=".wav")
    os.close(fd)
    sf.write(path, recording, fs)
    print("Saved:", path)
    return path

# ---------------- Transcribe ----------------
def transcribe_audio_file(path):
    r = sr.Recognizer()
    try:
        with sr.AudioFile(path) as source:
            audio = r.record(source)
        text = r.recognize_google(audio)
        print("Transcription:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn’t understand your speech.")
        return ""
    except sr.RequestError as e:
        print("Speech recognition error:", e)
        return ""
    finally:
        if os.path.exists(path):
            os.remove(path)



def query_ollama(prompt, model="tinyllama"):
    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt,       # send plain string input
            text=True,          # ensure text mode
            capture_output=True,
            encoding="utf-8",    
            errors="ignore"# capture stdout
        )
        response = result.stdout.strip()
        if not response:
            return "I'm here to listen."
        # Remove Ollama's prompt artifacts
        if "Send a message" in response:
            response = response.split("Send a message")[0].strip()
        if ">>>" in response:
            response = response.split(">>>")[0].strip()
        return response
    except Exception as e:
        return f"Error contacting Ollama: {e}"


# ---------------- Text-to-speech ----------------
def speak_text(text):
    if not text:
        return
    tts = gtts.gTTS(text)
    fd, path = tempfile.mkstemp(suffix=".mp3")
    os.close(fd)
    tts.save(path)

    data, sr_rate = sf.read(path)
    sd.play(data, sr_rate)
    sd.wait()
    os.remove(path)

# ---------------- Main Assistant Loop ----------------
def run_assistant():
    print("🤖 Mindmate")
    speak_text("Hello, I’m your AI wellness assistant. How are you feeling today?")

    while True:
        path = record_to_wav()
        text = transcribe_audio_file(path)

        if not text:
            continue
        if text.lower() in ["exit", "quit", "stop", "bye"]:
            speak_text("Goodbye. Take care of yourself.")
            break

        print("You:", text)
        ai_response = query_ollama(
            f"You are a kind, empathetic mental health support assistant. "
            f"Respond to this user in a supportive and calming way:\n{text}"
        )
        print("Assistant:", ai_response)
        speak_text(ai_response)

if __name__ == "__main__":
    run_assistant()
