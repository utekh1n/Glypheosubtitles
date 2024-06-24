import os
import re

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def write_file(content, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def split_into_chunks(text, max_chunk_size=100):
    sentences = re.split(r'(?<=[.!?]) +', text)
    
    chunks = []
    current_chunk = ''

    for sentence in sentences:
        if len(current_chunk) + len(sentence) + 1 > max_chunk_size:
            chunks.append(current_chunk.strip())
            current_chunk = ''
        
        words = sentence.split(',')
        for word in words:
            word = word.strip()
            if len(current_chunk) + len(word) + 1 > max_chunk_size:
                chunks.append(current_chunk.strip())
                current_chunk = word
            else:
                if current_chunk:
                    current_chunk += ', ' + word
                else:
                    current_chunk = word

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def prepare_subtitle_file(input_file, output_file):
    text = read_file(input_file)

    chunks = split_into_chunks(text)

    final_content = '\n\n'.join(chunks)

    write_file(final_content, output_file)

input_file = '/Users/folder/play.txt' ##add here the file location
output_file = '/Users/folder/play_fin.txt'
prepare_subtitle_file(input_file, output_file)
