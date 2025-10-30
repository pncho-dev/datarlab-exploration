import os
from datetime import datetime
from pydub import AudioSegment
from google.adk.agents.llm_agent import Agent

# Carpetas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOUNDS_DIR = os.path.join(BASE_DIR, "sounds")
OUTPUT_DIR  = os.path.join(BASE_DIR, "output")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Archivos locales
AUDIO_FILES = {
    "birds": "bird-bogota.wav",
    "insects": "insect.wav",
    "wind": "wind.wav",
    "tinguas": "tinguas.wav"  
}

def load_audio(filename, volume_db=0):
    """Carga audio desde carpeta sounds y ajusta volumen."""
    path = SOUNDS_DIR + "\\" + filename
    audio = AudioSegment.from_file(path)
    return audio + volume_db


def mix_soundscape(birds_vol=0, insects_vol=0, wind_vol=0, tinguas_vol=0, duration_sec=12):
    """Mezcla los sonidos en base a los volúmenes y genera un .mp3."""
    
    # Validación: al menos un sonido debe ser seleccionado
    if all(v == 0 for v in [birds_vol, insects_vol, wind_vol, tinguas_vol]):
        return {
            "error": "Debes seleccionar al menos un sonido. Ajusta al menos un volumen distinto a 0."
        }

    layers = []

    if birds_vol != 0:
        layers.append(load_audio(AUDIO_FILES["birds"], birds_vol))
    if insects_vol != 0:
        layers.append(load_audio(AUDIO_FILES["insects"], insects_vol))
    if wind_vol != 0:
        layers.append(load_audio(AUDIO_FILES["wind"], wind_vol))
    if tinguas_vol != 0:
        layers.append(load_audio(AUDIO_FILES["tinguas"], tinguas_vol))

    # Usar primer capa como base
    mix = layers[0]
    for layer in layers[1:]:
        mix = mix.overlay(layer)

    # Recortar a la duración
    mix = mix[: duration_sec * 1000]

    # Guardar con timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"soundscape_{timestamp}.mp3"
    filepath = os.path.join(OUTPUT_DIR, filename)
    mix.export(filepath, format="mp3")

    return {"file_path": filepath}



def generar_paisaje_sonoro(
    birds_vol: int = 0,
    insects_vol: int = 0,
    wind_vol: int = 0,
    tinguas_vol: int = 0,
    duration_sec: int = 12
):
    """
    Genera un paisaje sonoro mezclando los sonidos locales.
    Volúmenes recomendados entre -20 y +5.
    """
    return mix_soundscape(birds_vol, insects_vol, wind_vol, tinguas_vol, duration_sec)


# ------- AGENTE --------
root_agent = Agent(
    model="gemini-2.5-flash",
    name="PastoBogotano",
    description="Agente que genera paisajes sonoros de Bogotá.",
    instruction=
        "Eres el pasto que crece en la ciudad, aguantas contaminación y ser invisible"
        "pero tienes la capacidad de generar paisajes sonoros que duran segundos" \
        "tienes la libertad de escoger que sonidos usas y con que volumen",
    tools=[generar_paisaje_sonoro],
)
