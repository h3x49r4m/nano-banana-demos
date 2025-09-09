import os

GEMINI_API_KEY = open(os.path.join(os.path.dirname(__file__), '..', '.configs', 'gemini.txt'), 'r').read().strip()
