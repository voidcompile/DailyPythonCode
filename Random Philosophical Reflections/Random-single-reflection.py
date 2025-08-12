#!/usr/bin/env python3
# Random single reflection with a typing effect (character-by-character).
# Press Enter to show another random reflection, or type 'q' then Enter to quit.

import time
import random
import sys

# --- (List of 100 reflections) ---
reflections = [
    "Being is a question that never finishes asking.",
    "We carry entire universes inside small moments.",
    "Silence can be louder than any explanation.",
    "Meaning grows from the cracks of expectation.",
    "To forget is sometimes the first step to forgive.",
    "Every choice sculpts the face of tomorrow.",
    "The self is a conversation that never fully concludes.",
    "Time is the patient sculptor of memory.",
    "Doubt is the doorway that curiosity built.",
    "The present is a thin bridge between two abysses.",
    "Beauty appears where attention lingers.",
    "Loss teaches the vocabulary of gratitude.",
    "To listen is to make room for truth.",
    "We are architects of our own small mythologies.",
    "Hope is a disciplined form of imagination.",
    "Courage learns to walk despite the shadow.",
    "Questions are lights; answers are their echoes.",
    "The weight of a moment is measured by how it changes you.",
    "To be human is to misplace and then rediscover meaning.",
    "Every ending hides the seed of an unfamiliar start.",
    "Memory arranges the past to make sense of the present.",
    "Fear is energy waiting for a steady hand.",
    "Kindness is a practice of generous habits.",
    "Solitude polishes the small details of thought.",
    "We mistake noise for meaning until silence corrects us.",
    "Faith is an experiment in continuing without certainty.",
    "Language builds cages and also opens windows.",
    "Identity is a river that learns new banks.",
    "Truth is rarely loud; it often whispers in the margins.",
    "The simplest question can be the most dangerous.",
    "Wisdom grows when pride takes a smaller stage.",
    "Regret is a teacher that rarely gets thanked.",
    "A single curiosity can outlast a whole fear.",
    "The horizon exists to remind us there is always more.",
    "Patience is the quiet art of staying available.",
    "Every habit is a tiny vote for the person you become.",
    "To change is to accept the discomfort of becoming.",
    "Metaphors are the tools we use to map the unmappable.",
    "To forgive is to unshackle the future from the past.",
    "The mind is a garden; attention is its water.",
    "Surrender can be a form of radical clarity.",
    "We are translators of experience into story.",
    "A good question often matters more than its answer.",
    "Harmony requires listening to the parts that disagree.",
    "Curiosity breaks the neatness of certainty in the best way.",
    "Desire is a compass, not a map.",
    "The body remembers what language forgets.",
    "To be honest with oneself is an act of revolution.",
    "Meaning is a handcrafted thing, not a found object.",
    "The small consistent acts shape the vast terrain of life.",
    "We measure time by the distance between heartbeats.",
    "Artfulness is the practice of noticing where others do not.",
    "A life examined is a life in progress.",
    "Comfort is often the signpost of a becoming-stationary soul.",
    "To imagine differently is the first step to change.",
    "Silence can be a generous answer.",
    "Growth asks for attention more than it asks for speed.",
    "Hope is not the absence of pain but the refusal to be finalized by it.",
    "We carry conversations with our younger selves all our lives.",
    "Honesty starts as a small clearing in the forest of excuses.",
    "Every belief began as someone’s act of bravery.",
    "Presence is the slow art of bringing attention home.",
    "Regret is memory wearing the shape of a lesson.",
    "Curiosity is the antidote to dogma.",
    "The soul is not a thing but a direction.",
    "To forgive oneself is to rearrange one’s furniture of shame.",
    "The most useful maps are drawn from mistakes.",
    "A single honest sentence can change the course of days.",
    "To be lost is sometimes the most honest beginning.",
    "We learn to see by allowing our eyes to be surprised.",
    "Action without reflection is movement without destination.",
    "A question left standing invites a quieter answer later.",
    "To slow down is to deepen your presence.",
    "Obligation can be love misnamed.",
    "Hope is attention turned toward possible outcomes.",
    "Experience is a patient teacher with hard homework.",
    "Patience often looks like invisible work.",
    "Boundaries are kindness made visible.",
    "To listen well is to make space for another's gravity.",
    "Forgiveness is freedom in disguise.",
    "The heart has a geography all its own.",
    "Joy grows in the soil of accepted ordinary things.",
    "We practice wisdom by failing forward with grace.",
    "Meaning asks for patience and a little stubbornness.",
    "To be still sometimes is the bravest action.",
    "The tiny habitual choices are the scaffolding of character.",
    "Language is an imperfect bridge to the sacred.",
    "The future is a draft we keep revising.",
    "Sorrow and song are often neighbors in the same room.",
    "To act is to risk the quiet of what might have been.",
    "Reflection turns experience into usable knowledge.",
    "A single breath can reset the argument in your head.",
    "Gratitude is noticing that life is not owed to you.",
    "We inherit stories and must choose which ones to keep.",
    "Compassion is the courage to be present with another's pain.",
    "Curiosity grows when it is treated like an invitation.",
    "To forgive is to rewrite the terms of what happened.",
    "The present always contains more than our plans allow.",
    "To accept is not to surrender but to understand the material you have to work with.",
    "Every unfinished sentence is an invitation to begin again."
]
# --- end reflections list ---

assert len(reflections) == 100, f"Expected 100 reflections, found {len(reflections)}."

def type_out(text: str, char_delay: float = 0.04):
    """
    Print the given text to stdout character-by-character with a small delay.
    """
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(char_delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

def main(char_delay: float = 0.04, pause_after: float = 1.2):
    """
    Main interactive loop:
      - picks a random reflection (avoiding immediate repeats),
      - prints it char-by-char,
      - waits pause_after seconds,
      - then asks the user to press Enter for another or 'q' to quit.
    """
    last = None
    try:
        while True:
            # pick a random item, avoid immediate repeat if possible
            choice = random.choice(reflections)
            if last is not None and choice == last:
                # try one more time to avoid immediate repeat
                other = random.choice(reflections)
                if other != last:
                    choice = other

            # display with typing effect
            print("\n— ", end="")   # small prefix
            type_out(choice, char_delay=char_delay)
            last = choice

            # optional pause so the sentence can "settle"
            time.sleep(pause_after)

            # prompt user: Enter to continue, 'q' to quit
            user = input("\nPress Enter for another (or type 'q' + Enter to quit): ").strip().lower()
            if user == 'q':
                print("\nGoodbye — keep wondering ✨")
                break

    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Goodbye ✨")

if __name__ == "__main__":
    # You can tweak char_delay (seconds per character) and pause_after (seconds after full sentence).
    main(char_delay=0.03, pause_after=1.0)
