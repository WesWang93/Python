#=========================================================================================
#Name: Trigram
#Author: Wesley Wang
#Date: 4/23/2018
#=========================================================================================

import random

def parse_file(filename):
    with open(filename) as infile:
        words = []
        for line in infile:
            if line.startswith("End of the Project Gutenberg"):
                break
            for char in ['/', '\\', '.', ',', ':', ';', '"', '?', '!', '-', '\'']:
                line = line.replace(char, '')
            words.extend(line.split())

    return words


def build_trigram(words):
    tris = {}
    for i in range(len(words)-2):
        first = words[i]
        second = words[i+1]
        third = words[i+2]
        pair = (first, second)
        tris.setdefault(pair, []).append(third)

    return tris

def make_new_text(trigram):
    pair = random.choice(list(trigram.keys()))
    sentence = []
    sentence.extend(pair)
    for i in range(10):
        followers = trigram[pair]
        sentence.append(random.choice(followers))
        pair = tuple(sentence[-2:])
    result = ' '.join(sentence).capitalize().replace(' i ', ' I ')+"."
    return result


if __name__ == "__main__":
    words = parse_file("sherlock.txt")
    trigram = build_trigram(words)
    print(make_new_text(trigram))