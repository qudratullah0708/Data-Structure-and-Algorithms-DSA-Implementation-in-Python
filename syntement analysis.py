pip install openai
import openai

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = 'your-api-key'

def analyze_sentiment(text):
    # Using GPT-3.5 engine
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Analyze the sentiment of the following text: '{text}'",
        max_tokens=150,
        temperature=0.7,  # Adjust temperature for randomness in responses
        stop=None  # Disable the default stop sequence
    )

    # Extracting sentiment from the generated text
    sentiment = response['choices'][0]['text'].strip().lower()

    return sentiment

# Example usage
input_text = "I really enjoyed the movie. The plot was engaging, and the acting was fantastic!"
result = analyze_sentiment(input_text)

print(f"Sentiment: {result}")
