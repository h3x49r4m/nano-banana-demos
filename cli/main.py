import argparse
from gemini_client import GeminiClient

def chat_mode():
    client = GeminiClient()
    client.chat()

def cmd_mode():
    parser = argparse.ArgumentParser(description='Generate images from a prompt file.')
    parser.add_argument('--prompt', type=str, required=True, help='Path to the prompt file.')
    args = parser.parse_args()

    with open(args.prompt, 'r') as f:
        prompt = f.readlines()

    client = GeminiClient()
    texts, images = client.respond([prompt])



if __name__ == '__main__':
    #chat_mode()
    cmd_mode()
