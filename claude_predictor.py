import anthropic

def get_signal_prediction(crash_data, api_key):
    client = anthropic.Anthropic(api_key=api_key)

    response = client.messages.create(
        model="claude-3-sonnet",  # <-- use this base model name
        max_tokens=100,
        temperature=0,
        system="You are a crash predictor bot. Only reply with BET or WAIT.",
        messages=[
            {
                "role": "user",
                "content": f"Based on the past crashes: {crash_data}, should the next round be BET or WAIT?"
            }
        ]
    )

    prediction_text = response.content[0].text.strip().upper()
    confidence = 90.0 if "BET" in prediction_text else 60.0

    return prediction_text, confidence
