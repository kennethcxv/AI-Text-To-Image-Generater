import openai

def get_image_url(api_key, prompt, n=1, size="1024x1024"):
    openai.api_key = api_key
    response = openai.Image.create(prompt=prompt, n=n, size=size)
    image_url = response['data'][0]['url']
    return image_url

if __name__ == "__main__":
    API_KEY = 'your-api-key-here'
    PROMPT = "Cat"
    SIZE = "1024x1024"

    image_url = get_image_url(API_KEY, PROMPT, size=SIZE)
    print(image_url)