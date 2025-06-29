import anthropic

def get_signal_prediction(crash_data, api_key):
    client = anthropic.Client(api_key=api_key)

    prompt = (
        "\n\nHuman: You are a crash predictor bot. "
        f"Based on the past crashes: {crash_data}, should the next round be BET or WAIT? "
        "Only reply with BET or WAIT.\n\nAssistant:"
    )

    response = client.completions.create(
        prompt=prompt,
        model="claude-v1.3",  # ✅ Correct model name for completions API
        max_tokens_to_sample=10
    )

    prediction_text = response.completion.strip().upper()
    confidence = 90.0 if "BET" in prediction_text else 60.0

    return prediction_text, confidence
