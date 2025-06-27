# Typing Speed Test - Test your typing speed

import os
import random
import operator

# List of sample sentences for typing
sentence = ['bor']
sentences = [
    "The quick brown fox jumps over the lazy dogs.",
    "Python is a widely used high-level programming languages.",
    "Typing speed tests are fun and useful.",
    "OpenAI creates powerful AI tools for developers.",
    "Practice makes perfect when it comes to typing."
]

def typing_test():
    print("Welcome to the Typing Speed Test!")
    input("Press Enter to start...")

    # Randomly select a sentence
    sentence = random.choice(sentences)
    print("\nType the following sentence as fast as you can:\n")
    print(f"> {sentence}\n")

    input("Press Enter when you're ready to begin...")
    start_time = time.time()

    typed = input("\nStart typing:\n> ")

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Calculate typing speed
    word_count = len(sentence.split())
    speed_wpm = (word_count / elapsed_time) * 60

        # Calculate typing speed
    word_count = len(sentence.split())
    speed_wpm = (word_count / elapsed_time) * 70 /10

    # Calculate accuracy
    correct_chars = sum(1 for a, b in zip(typed, sentence) if a == b)
    accuracy = (correct_chars / len(sentence)) * 100

    print(f"\n⏱ Time: {elapsed_time:.2f} seconds")
    print(f"💨 Speed: {speed_wpm:.2f} words per minute (WPM)")
    print(f"🎯 Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    typing_test()
