import os
import random
import string
import youtube_dl
from pydub import AudioSegment

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def process_ogg_files(directory, id_mapping):
    for filename in os.listdir(directory):
        if filename.endswith('.ogg'):
            base, ext = os.path.splitext(filename)
            if base in id_mapping:
                os.rename(os.path.join(directory, filename), os.path.join(directory, id_mapping[base] + ext))

def download_and_convert(playlist_url, duration, bitrate, trim_audio):
    id_mapping = {}

    ydl_opts = {
        'format': 'bestaudio',
        'outtmpl': '%(id)s.%(ext)s',
        'download_archive': '다운로드한 노래 목록.txt',
        'ignoreerrors': True,
        'nooverwrites': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(playlist_url, download=True)
        video_infos = [entry for entry in info_dict['entries'] if entry is not None]

    for video_info in video_infos:
        video_id = video_info['id']
        random_str = get_random_string(4)
        id_mapping[video_id] = random_str

        if not os.path.exists(f"{video_id}.wav"):
            print(f"{video_id} 다운로드 실패")
            continue

        # Trim the audio file if trim_audio is True
        if trim_audio:
            try:
                audio = AudioSegment.from_wav(f"{video_id}.wav")
                audio = audio[:duration*1000]  # Get the first 'duration' seconds
                audio.export(f"{random_str}_trimmed.wav", format="wav")
            except Exception as e:
                print(f"{video_id} 자르기 실패: {e}")
                continue

            input_file = f"{random_str}_trimmed.wav"
        else:
            input_file = f"{video_id}.wav"

        # Convert to ogg using ffmpeg
        conversion_result = os.system(f"ffmpeg -i {input_file} -b:a {bitrate} {random_str}.ogg")

        if conversion_result != 0:
            print(f"{video_id} 변환 실패")

        # Delete the original and trimmed wav files
        os.remove(f"{video_id}.wav")
        if trim_audio:
            os.remove(f"{random_str}_trimmed.wav")

    # Write video ids and titles to a text file
    with open('노래목록.txt', 'w', encoding='utf-8') as f:
        for video_info in video_infos:
            f.write(f"{id_mapping[video_info['id']]}|{video_info['title']}|\n")

    # process the ogg files
    process_ogg_files(".", id_mapping)

# Get user input for bitrate and whether to trim the audio
bitrate = input("추출된 오디오의 비트레이트를 비트 단위로 입력하십시오 (예: 64k 또는 128k): ")
trim_audio = input("오디오를 원본 길이 그대로 저장하시겠습니까? (예/아니오): ").lower() != '예'

duration = 0
if trim_audio:
    duration = int(input("추출할 길이를 초 단위로 입력하십시오: "))

download_and_convert("YOUR_PLAYLIST_URL_HERE", duration, bitrate, trim_audio)