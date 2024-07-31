Transcription Program

Este es un programa de transcripción de audio a texto usando Python.

Requisitos

- Python 3.10
- Bibliotecas especificadas en `requirements.txt`

Instalación

1. Necesario instalar miniconda
   

3. Crea un entorno virtual y activa:

    conda create -n whisper -env python=3.10

    conda activate whisper-env
    

3. Instala las dependencias:
    -whisper pip install git+https://github.com/openai/whisper.git
    -Numpy pip install numpy==1.21.6
    -Torch pip install torch==2.0.1

4. Ejecuta el programa de transcripción:
   
   conda activate whisper-env
   python main.py
 
    
