# Glypheosubtitles
The program helps you to divide your play into chunks with 100 characters or less. You will have a .txt output file that you will have to check manually, but it always will take you less time than separate the text into chunks by hand.

# For separation with Keywords

Features

Keyword Handling: Keywords denote character dialogues and are treated specially.
Chunk Splitting: Text is split into chunks of up to 100 characters without splitting words.
Proper Formatting: Chunks are formatted to ensure no awkward word placement.
Usage

Function Definitions
is_keyword(text):

Checks if a given text starts with any of the predefined keywords followed by a colon.
Keywords are specific roles in the play.
should_move_to_next_chunk(word):

Determines if a word should prompt moving to the next chunk based on its length and presence of specific symbols.
split_into_chunks(line, max_length=100):

Splits a line of text into chunks, ensuring no chunk exceeds 100 characters.
Handles keywords by starting new chunks appropriately.
format_chunks(chunks):

Formats chunks by ensuring keywords are followed by a newline.
Handles special formatting for dialogues.
ensure_valid_endings(chunks):

Adjusts chunks to ensure valid sentence endings, moving small words to the next chunk if necessary.
adjust_chunk_endings(chunks):

Further adjusts chunk endings to prevent short words or symbols from being left at the end.
Script Workflow
Read Input File:

Reads the content of the input text file.
Split into Lines:

Splits the content into lines and processes each line.

Chunk Processing:

Splits lines into chunks, formats them, and ensures valid endings.
Write Output File:

Writes the processed chunks to the output file.

# For separation without keywords 

Features

Sentence Handling: Splits text based on sentences to maintain coherence.
Comma Handling: Splits sentences at commas if needed to fit within the character limit.
Chunk Splitting: Ensures chunks do not exceed 100 characters.
Usage

Function Definitions
read_file(file_path):

Reads the content of a file and returns it as a string.
write_file(content, file_path):

Writes the given content to a file.
split_into_chunks(text, max_chunk_size=100):

Splits the text into chunks, ensuring no chunk exceeds 100 characters.
Uses sentences as the primary unit for splitting, and commas as secondary.
Script Workflow
Read Input File:

Reads the content of the input text file.
Split into Chunks:

Splits the text into chunks based on sentences and commas.
Write Output File:

Writes the processed chunks to the output file, separated by double newlines.
