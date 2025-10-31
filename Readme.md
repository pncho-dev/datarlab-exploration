# 🌿 PastoBogotano — Agente Generador de Paisajes Sonoros de Bogotá

Este proyecto utiliza un **Agente LLM** con herramientas de audio para generar paisajes sonoros cortos, únicos y artísticos inspirados en la biodiversidad de Bogotá.  
El agente mezcla sonidos naturales (pájaros, insectos, viento, tinguas) y les aplica efectos creativos para producir piezas de 6 a 20 segundos llenas de textura y ambiente.

---

##  Estructura del Proyecto

project/
│── agentHierba.py # Script principal con el agente y la herramienta de mezcla de sonido
│── sounds/ # Carpeta con archivos .wav locales (necesaria)
│ ├── bird-bogota.wav
│ ├── insect.wav
│ ├── wind.wav
│ └── tinguas.wav
│── output/ # Aquí se guardan los paisajes generados
│── README.md
│── .gitignore



##  ¿Qué hace el agente?

El agente **PastoBogotano**:

- Habla poco; **se expresa con sonidos** 
- Selecciona qué elementos naturales incluir en cada paisaje  
- Superpone y mezcla audios con volúmenes y posiciones diferentes  
- Puede aplicar efectos artísticos como:  
  ✅ Eco  
  ✅ Inversión del audio  
  ✅ Alteración de velocidad/pitch  
- Genera un archivo `.mp3` único en la carpeta `output/`

---

##  Requisitos

###  Instalación de Dependencias

Este proyecto incluye un archivo `requirements.txt` con todas las librerías necesarias para ejecutar el agente generador de paisajes sonoros.

###  Instalar dependencias

Ejecuta el siguiente comando desde la raíz del proyecto:

```bash
pip install -r requirements.txt
```
### Requisito adicional: FFmpeg

pydub necesita FFmpeg instalado en tu sistema:

Windows (winget):

```bash
winget install ffmpeg
```

Si necesitas subir audios grandes al repositorio, utiliza Git LFS (Large File Storage):

```bash
git lfs install
git lfs track "*.wav"