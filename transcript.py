import os
import whisper
import ffmpeg

def extract_audio(video_path, audio_path="audio.wav"):
    """Extrahiert die Audiospur aus einem Video."""
    os.system(f"ffmpeg -i {video_path} -acodec pcm_s16le -ar 16000 {audio_path}")
    return audio_path

def transcribe_audio(audio_path):
    """Transkribiert die Audiodatei mit OpenAI Whisper."""
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["text"]

if __name__ == "__main__":
    video_file = "/Users/fouadghazal/Downloads/Warum fasten wir im Ramadan_ Eine Erklärung für Kinder لماذا نصوم رمضان؟ إجابة للاطفال.mp4"
    audio_file = extract_audio(video_file)
    text = transcribe_audio(audio_file)
    
    print("\n--- Transkribierter Text ---\n")
    print(text)
    
    # Speichere den transkribierten Text in einer Datei
    with open("transcript.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("\nDer transkribierte Text wurde in 'transcript.txt' gespeichert.")
