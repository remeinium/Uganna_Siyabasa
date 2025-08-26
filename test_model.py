"""
Test script for loading and interacting with a FastText model.
Author: Remeinium AI (https://huggingface.co/Remeinium)

This script demonstrates:
- Loading a FastText model
- Retrieving vector representations for words
- Finding the most similar words
"""

import fasttext
import sys
from pathlib import Path

# Path to the FastText model (.bin)
# Update this path if your model is located elsewhere
MODEL_PATH = Path("UgannA_Siyabasa.bin")

def main():
    try:
        print("Loading FastText model...")
        model = fasttext.load_model(str(MODEL_PATH))
        print("Model loaded successfully!\n")

        # Example word to test
        word = "අම්මා"

        # --- Test 1: Word Vector ---
        try:
            vector = model[word]  # word lookup is supported
            print(f"Vector for '{word}' (size={len(vector)}):\n{vector}\n")
        except Exception:
            print(f"Word '{word}' not found in the model vocabulary.\n")

        # --- Test 2: Similar Words ---
        try:
            print(f"Top 10 words similar to '{word}':")
            similar_words = model.get_nearest_neighbors(word, k=10)
            for score, neighbor in similar_words:
                print(f"  {neighbor}: {score:.4f}")
        except Exception:
            print(f"Unable to compute nearest neighbors for '{word}'.\n")

    except Exception as e:
        print(f"Error loading model: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
