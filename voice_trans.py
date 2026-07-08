import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import pygame
import time
import os

# Initialize pygame mixer
pygame.mixer.init()


# -----------------------------
# Speak translated text
# -----------------------------
def speak(text, lang):

    filename = "voice.mp3"

    tts = gTTS(text=text, lang=lang)
    tts.save(filename)

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.music.unload()

    os.remove(filename)


# -----------------------------
# Speech Recognition
# -----------------------------
def speech_to_text():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("\nSpeak in English...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        audio = recognizer.listen(source)

    try:

        text = recognizer.recognize_google(
            audio,
            language="en-GB"
        )

        print("You said:", text)

        return text

    except sr.UnknownValueError:
        print("Could not understand speech.")

    except sr.RequestError:
        print("Internet connection required.")

    return ""


# -----------------------------
# Translation
# -----------------------------
def translate_text(text, target_language):

    translated = GoogleTranslator(
        source="auto",
        target=target_language
    ).translate(text)

    print("Translated Text:", translated)

    return translated


# -----------------------------
# Language Menu
# -----------------------------
def choose_language():

    languages = {

        "1": ("Hindi", "hi"),
        "2": ("Tamil", "ta"),
        "3": ("Telugu", "te"),
        "4": ("Bengali", "bn"),
        "5": ("Marathi", "mr"),
        "6": ("Gujarati", "gu"),
        "7": ("Malayalam", "ml"),
        "8": ("Punjabi", "pa"),
        "9": ("French", "fr"),
        "10": ("Spanish", "es"),
        "11": ("German", "de"),
        "12": ("Japanese", "ja"),
        "13": ("Chinese", "zh-CN")

    }

    print("\n========== Languages ==========\n")

    for key, value in languages.items():
        print(f"{key}. {value[0]}")

    print()

    choice = input("Enter your choice: ")

    if choice in languages:
        return languages[choice][1]

    print("Invalid choice! Defaulting to Hindi.")

    return "hi"


# -----------------------------
# Main Program
# -----------------------------
def main():

    print("===================================")
    print(" AI Voice Translator ")
    print("===================================")

    language = choose_language()

    text = speech_to_text()

    if text:

        translated = translate_text(text, language)

        print("\nSpeaking Translation...\n")

        speak(translated, language)

        print("Done!")


if __name__ == "__main__":
    main()