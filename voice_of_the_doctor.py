#Step1: setup text to speech tts model(gtts&eleven labs)
import os
from gtts import gTTS
from dotenv import load_dotenv
load_dotenv()
def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)


input_text="Hi this is Shouryaman"
text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")  

#elevenLabs
#
#import os
#from elevenlabs import generate, save, set_api_key



# ✅ Set the API key from .env
#set_api_key(os.getenv("ELEVENLABS_API_KEY"))

#def text_to_speech_with_elevenlabs(input_text, output_filepath):
 #   audio = generate(
  #      text=input_text,
   #     voice="Aria",
    #   output_format="mp3_22050_32"
   # )
    #save(audio, output_filepath)

#text_to_speech_with_elevenlabs(input_text, "elevenlabs_testing.mp3")
#step 2: use the model for text output to voice
import subprocess
import platform

def text_to_speech_with_gtts(input_text, output_filepath):
    if not input_text or not input_text.strip():
        print("⚠ Empty text passed to TTS. Skipping generation.")
        return None

    language = "en"

    try:
        # Generate speech
        audioobj = gTTS(
            text=input_text.strip(),
            lang=language,
            slow=False
        )
        audioobj.save(output_filepath)

        # Auto-play audio (optional)
        os_name = platform.system()
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # or 'mpg123', 'ffplay'
        else:
            raise OSError("Unsupported operating system")

        return output_filepath

    except Exception as e:
        print(f"❌ Error in TTS generation or playback: {e}")
        return None