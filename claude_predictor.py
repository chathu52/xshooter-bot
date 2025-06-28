import anthropic
from config import CLAUDE_API_KEY

client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)

def ask_claude(prompt):
    try:
        response = client.messages.create(
            model="claude-3-opus-20240229",  # or use 'claude-3-sonnet-20240229'
            max_tokens=1000,
            temperature=0.7,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.content[0].text
    except Exception as e:
        return f"Error from Claude: {str(e)}"
