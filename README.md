# AI Speech Recognition System

## Overview

This project is a Python desktop application that converts speech from audio files into text using OpenAI's Whisper model. It has a simple Tkinter-based graphical interface that allows users to upload an audio file, generate its transcription, and save the result as a text file.

## Features

* User-friendly graphical interface
* Supports multiple audio formats (MP3, WAV, M4A, FLAC, OGG, AAC)
* Converts speech to text using Whisper AI
* Save the transcription as a `.txt` file
* Progress bar and status updates during processing

## Technologies Used

* Python
* Tkinter
* OpenAI Whisper
* PyTorch

## Installation

1. Clone this repository.
2. Install the required packages:

   ```bash
   pip install openai-whisper torch torchvision torchaudio
   ```
3. Make sure FFmpeg is installed and added to your system PATH.
4. Run the application:

   ```bash
   python speech_recognition_gui.py
   ```

## Project Structure

```text
AI-Speech-Recognition-System/
│── speech_recognition_gui.py
│── README.md

```

## How to Use

1. Launch the application.
2. Click **Upload Audio** and select an audio file.
3. Wait for the transcription to complete.
4. View the generated text in the output box.
5. Save the transcription using the **Save Text** button.

## Future Improvements

* Live microphone speech recognition
* Support for multiple languages
* Dark and light theme options
* Export transcription to PDF or DOCX


