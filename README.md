# TS to MP3 Converter

A Python script to convert `.ts` video files to `.mp3` audio files, while preserving the original folder structure. The script also adds ID3 tags to the resulting MP3 files, setting the author, album, and title information automatically.

## Features

- Converts `.ts` files to `.mp3` using `ffmpeg`.
- Maintains the original folder structure in the output directory.
- Adds ID3 tags to the converted MP3 files:
  - **Author** is always set to "Autor Padrão".
  - **Album** is set based on the folder name (or "Diversos" for root directory).
  - **Title** is set to the original file name.
- Automatically overwrites existing MP3 files.

## Requirements

- Python 3.x
- ffmpeg installed and added to your system PATH.
- Python packages: `ffmpeg-python`, `mutagen`

You can install the required Python packages using:

```bash
pip install ffmpeg-python mutagen
