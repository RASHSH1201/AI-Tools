from openai import OpenAI


def summarize_headlines(headlines, api_key):
    combined_text = "\n".join(headlines)
    prompt = f"Summarize the following news headlines:\n{combined_text}"

    # Create a client using your API key
    client = OpenAI(api_key=api_key)

    # Send the chat completion request
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    # Extract and return the summary
    return response.choices[0].message.content