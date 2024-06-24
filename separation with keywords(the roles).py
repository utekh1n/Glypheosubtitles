def prepare_subtitle_file(input_file, output_file):
    keywords = [
        "Голос", "Кри", "Ви", "Са", "Све", ##put here the roles that u have in your play
        "Ле", "На",
    ]

    def is_keyword(text):
        return any(text.startswith(keyword + ':') for keyword in keywords)

    def should_move_to_next_chunk(word):
        symbols = "!@#$%^&*()-_=+[{]}|;:',<.>/?"
        return len(word) <= 3 or (len(word) == 4 and word[-1] in symbols)

    def split_into_chunks(line, max_length=100):
        words = line.split()
        chunks = []
        current_chunk = ''

        for word in words:
            if is_keyword(word) and current_chunk:
                chunks.append(current_chunk.strip())
                current_chunk = word + ' '
            elif len(current_chunk) + len(word) + 1 <= max_length:
                current_chunk += word + ' '
            else:
                if should_move_to_next_chunk(word):
                    if current_chunk:
                        chunks.append(current_chunk.strip())
                    current_chunk = word + ' '
                else:
                    current_chunk += word + ' '
                    if len(current_chunk.strip()) > max_length:
                        chunks.append(current_chunk.strip())
                        current_chunk = ''

        if current_chunk:
            chunks.append(current_chunk.strip())

        return chunks

    def format_chunks(chunks):
        formatted_chunks = []
        for chunk in chunks:
            if is_keyword(chunk):
                parts = chunk.split(':', 1)
                formatted_chunks.append(parts[0] + ':\n' + parts[1].strip())
            else:
                formatted_chunks.append(chunk)
        return formatted_chunks

    def ensure_valid_endings(chunks):
        valid_chunks = []
        i = 0
        while i < len(chunks):
            chunk = chunks[i]
            words = chunk.split()
            if len(words) > 0 and should_move_to_next_chunk(words[-1]):
                if i + 1 < len(chunks):
                    chunks[i + 1] = words[-1] + ' ' + chunks[i + 1]
                    chunk = ' '.join(words[:-1]).strip()
            valid_chunks.append(chunk)
            i += 1
        return valid_chunks

    def adjust_chunk_endings(chunks):
        adjusted_chunks = []
        for chunk in chunks:
            while True:
                if len(chunk) < 6:
                    break
                if chunk[-1].isspace():
                    chunk = chunk.rstrip()
                last_word = chunk.split()[-1]
                if should_move_to_next_chunk(last_word):
                    chunk = chunk.rsplit(' ', 1)[0]
                    if adjusted_chunks:
                        adjusted_chunks[-1] += ' ' + last_word
                    else:
                        adjusted_chunks.append(last_word)
                else:
                    break
            adjusted_chunks.append(chunk)
        return adjusted_chunks

    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    lines = content.split('\n')
    chunks = []

    for line in lines:
        if line.strip():
            line_chunks = split_into_chunks(line)
            formatted_chunks = format_chunks(line_chunks)
            chunks.extend(formatted_chunks)

    chunks = ensure_valid_endings(chunks)
    chunks = adjust_chunk_endings(chunks)

    with open(output_file, 'w', encoding='utf-8') as file:
        for i, chunk in enumerate(chunks):
            if i > 0:
                file.write('\n\n')
            file.write(chunk)

input_file = '/Users/folder/play.txt' ##add here the file location
output_file = '/Users/folder/play_fin.txt'
prepare_subtitle_file(input_file, output_file)
