import os
from pydub import AudioSegment

def convert_mp3_to_ogg(mp3_folder, ogg_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(ogg_folder):
        os.makedirs(ogg_folder)

    # List all files in the MP3 folder
    mp3_files = [f for f in os.listdir(mp3_folder) if f.endswith('.mp3')]

    for mp3_file in mp3_files:
        # Get the full path of the input MP3 file
        mp3_path = os.path.join(mp3_folder, mp3_file)

        # Load the MP3 file
        audio = AudioSegment.from_mp3(mp3_path)

        # Create the output OGG file path
        ogg_file = mp3_file.replace('.mp3', '.ogg')
        ogg_path = os.path.join(ogg_folder, ogg_file)

        # Convert MP3 to OGG
        audio.export(ogg_path, format='ogg')

        print(f"Converted {mp3_file} to {ogg_file}")

if __name__ == "__main__":
    # Input MP3 folder
    mp3_folder = "./put_here"

    # Output OGG folder
    ogg_folder = "./out_here"

    convert_mp3_to_ogg(mp3_folder, ogg_folder)