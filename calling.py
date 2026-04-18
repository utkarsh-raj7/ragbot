from dotenv import load_dotenv
load_dotenv(override=True)

from google import genai
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how ai works in few words"
)

print(response.text )