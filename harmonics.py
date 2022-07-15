import os
import sys
import json

# Constants
pitches = [ "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B" ]

# Classes
class Note:

    def __init__(self, name, octave, freq ):
        self.name = name
        self.octave = octave
        self.frequency = freq
        self.period = self.calc_period()
        return

    def calc_period(self):
        x = round((self.frequency % 1),2)
        return (1/x) if x != 0 else 1

    def __repr__(self):
        _d = self.__dict__
        _d["frequency"] = round(self.frequency,2)
        _d["period"] = round(self.period,2)
        return json.dumps(_d)

# Functions
def calc_pitch_change():
    return pow(2,(1/12))

def generate_notes( octaves ):
    """ Generate a list of notes starting from C up to B in the given number of Octaves """
    notes = []
    fstep = calc_pitch_change()
    j = 0
    for i in range(0,octaves):
        for pitch in pitches:
            note = Note(pitch,i,pow(fstep,j))
            j += 1
            notes.append(note)
    
    data = "["
    for note in notes:
        data += f"{note},\n"
    data += "]"
    return data

# Run the actual script
if __name__ == "__main__":
    if len(sys.argv[1:]) < 1:
        print("Expected 1 argument, octave count.")
    else:
        octaves = int(sys.argv[1])
        print(generate_notes(octaves))