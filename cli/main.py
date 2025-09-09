from gemini_client import GeminiClient


def test_text_to_image(client):
    prompt = open('prompts/infographics/dynamic_systems_cartoon_prompt.txt', 'r').readlines() 
    texts, images = client.respond([prompt])


if __name__ == '__main__':

    client = GeminiClient()
    
    test_text_to_image(client)
    #client.chat()
