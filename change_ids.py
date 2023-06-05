import os
import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def process_txt_file(filepath, id_mapping):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        video_id, song_name = line.strip().split("|", 1)
        if video_id not in id_mapping:
            id_mapping[video_id] = get_random_string(4)
        new_lines.append(id_mapping[video_id] + "|" + song_name + "\n")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

def process_ogg_files(directory, id_mapping):
    for filename in os.listdir(directory):
        if filename.endswith('.ogg'):
            base, ext = os.path.splitext(filename)
            if base in id_mapping:
                os.rename(os.path.join(directory, filename), os.path.join(directory, id_mapping[base] + ext))

id_mapping = {}
process_txt_file('노래목록.txt', id_mapping)
process_ogg_files('ogg_파일_디렉토리', id_mapping)