import sys
import os
from music21 import converter
from io import BytesIO
from openai import OpenAI

# Fetch OpenAI API key from environment variable and start client

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

def convert_abc_to_midi(abc_notation):
    # Convert ABC notation to a Score object
    score = converter.parse(abc_notation)

    # Clear out existing TimeSignature objects
    for element in score.flat.getElementsByClass('TimeSignature'):
        score.remove(element)

    # Convert Score object to MIDI
    midi_stream = score.write('midi')
    return midi_stream

def extract_chords(lines):
    timings, symbols = [], []
    for line in lines:
        # Split each line into its components
        _, timing, symbol = list(map(str, eval(line)))
        # Ignore chords with timing 0.0
        if float(timing) > 0:
            try:
                symbol = float(symbol)
                symbols.append(f'\n{symbol} ')
            except:
                if symbol == '<start>':
                    continue
                elif symbol == '<style>' or symbol == 'Tonality':
                    symbol = symbol.strip("<>")
                    symbol = symbol[0].upper() + symbol[1:]
                    symbols.append(f'{symbol}: ')
                elif symbol.startswith('Form_'):
                    symbols.append(f' ({symbol}) ')
                elif symbol == '|:':
                    symbols.append(f'{symbol} ')
                elif symbol == ':|':
                    symbols.append(f' {symbol}')
                elif symbol == '|':
                    symbols.append(f' {symbol}')
                elif symbol == '.' or symbol == '':
                    continue
                elif 1 <= len(symbol) <= 3: 
                    symbols.append(symbol)
                else:
                    symbols.append(symbol+' ')
    return ''.join(symbols)

def generate_abc_from_chords(chords):
    prompt = f"""Please give me a suitable melody \
for the below chord progression. Please plan it out beforehand, \
making sure to prevent excessive repetition, balancing fit to genre with \
sufficiently interesting structure so it's not plain or uninteresting. \
Don't edit the progression, stick to the timings and bar markings as given.\
\nAnswer in correctly formatted ABC text music format.\n\n{chords}"""
    chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo",
        )
    print("==PROMPT"+"="*70)
    print(prompt)
    content = chat_completion.choices[0].message.content.strip()
    print("==RESPONSE CONTENT"+"="*60)
    print(content)
    return content

if __name__ == "__main__":
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        genre = input_file.split('_')[-1].split('.')[0]  # e.g. 'Rock'
        with open(input_file, 'r') as f:
            lines = f.readlines()
        simplified_chords = extract_chords(lines)
        abc_notation = generate_abc_from_chords(''.join(lines))
        midi_stream = convert_abc_to_midi(abc_notation)
        print("==MIDI STREAM"+"="*70)
        print(midi_stream)
    else:
        print("Usage:")
        print("To convert simplified chords to MIDI: python script.py <input_file>")
        sys.exit(1)

