
import random
import os
from music21 import stream, note, tempo

# Step 1: Collect musical notes
music_notes = [
    60, 62, 64, 65, 67, 69, 71, 72,
    67, 65, 64, 62, 60, 64, 67, 72
]

# Step 2: Learn note patterns
patterns = {}

for i in range(len(music_notes) - 2):
    key = tuple(music_notes[i:i+2])
    next_note = music_notes[i+2]

    if key not in patterns:
        patterns[key] = []

    patterns[key].append(next_note)

print("Music patterns learned successfully!")

# Step 3: Generate new music
generated_notes = [60, 62]

for i in range(48):
    key = tuple(generated_notes[-2:])

    if key in patterns:
        next_note = random.choice(patterns[key])
    else:
        next_note = random.choice(music_notes)

    generated_notes.append(next_note)

# Step 4: Create MIDI music
output = stream.Stream()
output.append(tempo.MetronomeMark(number=100))

for pitch in generated_notes:
    new_note = note.Note(pitch)
    new_note.quarterLength = 0.5
    output.append(new_note)

# Step 5: Save music
output.write("midi", fp="generated_music.mid")

print("New music generated successfully!")
print("File saved as generated_music.mid")
