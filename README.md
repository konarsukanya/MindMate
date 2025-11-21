
# 🧠 MindMate – Offline AI Wellness Assistant

### A local, privacy-focused AI mental wellness companion powered by **TinyLlama + Ollama**

MindMate is an **offline AI wellness assistant** that listens to your voice, transcribes your speech, analyzes your emotional content, and responds empathetically using a locally-run LLM — **without sending data to any cloud service**.

This project integrates **speech recognition, local LLM inference, and text-to-speech** into a simple interactive wellness assistant designed for mental-health support.

---

## ✨ Features

* 🎙️ **Voice Recording** — Captures microphone audio (8 seconds) and saves as `.wav`.
* 📝 **Speech-to-Text** — Accurate transcription using `SpeechRecognition` + Google SR.
* 🧠 **Local LLM Response Generation** — Uses `TinyLlama` via **Ollama** (fully offline).
* 🔊 **Text-to-Speech** — Speaks responses using `gTTS` + `sounddevice`.
* 💬 **Empathetic Mental-Health Responses** — Special prompting for supportive tone.
* 🔐 **Privacy-Friendly** — No cloud storage. Everything happens locally.
* 🖥️ **Cross-Platform Python Implementation** — Works on Windows, Linux, macOS.

---

## 🏗️ Architecture

```
User Voice → Recorder → .wav File  
         → Speech Recognition → Text  
         → Local LLM (Ollama) → AI Reply  
         → Text-to-Speech → Audio Output  
```

Modules used:

| Component          | Technology             |
| ------------------ | ---------------------- |
| Recording          | sounddevice, soundfile |
| Transcription      | SpeechRecognition      |
| LLM Inference      | Ollama + TinyLlama     |
| TTS                | gTTS                   |
| Temp File Handling | tempfile               |
| Orchestration      | Python                 |

---

## 📦 Installation

### 1️⃣ Install Python dependencies

```bash
pip install sounddevice soundfile SpeechRecognition gTTS numpy
```

### 2️⃣ Install PortAudio (if needed)

**Windows:**
Included by default with sounddevice.

**Linux:**

```bash
sudo apt install portaudio19-dev
```

### 3️⃣ Install Ollama

Download from:
[https://ollama.com/download](https://ollama.com/download)

### 4️⃣ Download the TinyLlama model

```bash
ollama pull tinyllama
```

---

## ▶️ Usage

Run the assistant:

```bash
python ol4.py
```

It will:

1. Ask how you are feeling
2. Record your voice
3. Transcribe what you say
4. Generate an empathetic reply using the local LLM
5. Speak the response back to you

---

## 🧩 Code Structure

```
MindMate/
│
├── ol4.py      # Main assistant script
├── README.md        # Project documentation

```

---

---


## 🤝 Contributing

Pull requests and suggestions are welcome!
Looking for collaborators interested in:

* Speech processing
* Emotion AI
* LLM fine-tuning
* Offline AI systems

---

## 📜 License

MIT License

---

## ❤️ Acknowledgements

* [Ollama](https://ollama.com/)
* TinyLlama team
* Python OSS community

---


