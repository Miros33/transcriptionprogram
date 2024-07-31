import whisper
import os

# Cargar el modelo de Whisper
model = whisper.load_model("large")

# Función para transcribir el audio
def transcribe_audio(audio_path):
    try:
        # Realizar la transcripción con detección automática de idiomas
        result = model.transcribe(audio_path, verbose=True)
        return result["text"]
    except Exception as e:
        print(f"Error en la transcripción de {audio_path}: {str(e)}")
        return None

if __name__ == "__main__":
    audio_folder_path = "./"
    audio_files = [f for f in os.listdir(audio_folder_path) if f.endswith('.wav')]

    for audio_file in audio_files:
        print(f"Procesando archivo: {audio_file}")
        audio_file_path = os.path.join(audio_folder_path, audio_file)
        
        # Transcribir el audio con detección automática de idioma
        transcription_auto = transcribe_audio(audio_file_path)

        if transcription_auto is not None:
            print('-' * 50)
            print("Transcripción con detección automática de idioma:")
            print(transcription_auto)
        else:
            print("No se pudo transcribir el archivo correctamente con detección automática de idioma.")















