# claude_predictor.py

import anthropic

def get_signal_prediction(crash_data, api_key):
    # Initialize Claude client
    client = anthropic.Client(api_key=api_key)

    # Proper Claude-compatible prompt formatting
    prompt = (
        "\n\nHuman: You are a crash predictor bot. "
        f"Based on the past crashes: {crash_data}, should the next round be BET or WAIT? "
        "Only reply with BET or WAIT.\n\nAssistant:"
    )

    # Make API call
    response = client.completions.create(
        prompt=prompt,
        model="claude-2",
        max_tokens_to_sample=10  # Reduced for stricter responses
    )

    # Parse response and normalize
    prediction_text = response.completion.strip().upper()

    # Basic confidence estimation (you can improve this later)
    confidence = 90.0 if "BET" in prediction_text else 60.0

    return prediction_text, confidence
