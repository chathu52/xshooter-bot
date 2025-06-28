# xshooter.py
import csv
import datetime
import telegram
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, CLAUDE_API_KEY
from claude_predictor import get_signal_prediction

# Initialize bot
bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

# CSV file to log all data
CSV_FILE = "xshooter_log.csv"

# Function to save to CSV
def log_to_csv(date, time, signal, levels, confidence):
    row = [date, time, signal] + levels + [f"{confidence}%"]
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(row)

# Function to send message to Telegram
def send_signal(signal, confidence, prediction):
    message = f"""
🎯 Signal: {signal}
📊 Confidence: {confidence}%
🧠 Next Prediction: {prediction}
"""
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message.strip())

# Dummy function to simulate crash round (replace this with real input or integration)
def run_xshooter():
    # Simulate data row
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")
    signal = "BET"
    crash_data = ["✅", "✅", "✅", "❌", "❌"]

    # Get AI prediction
    prediction, confidence = get_signal_prediction(crash_data, CLAUDE_API_KEY)

    # Log to CSV
    log_to_csv(date, time, signal, crash_data, confidence)

    # Send signal to Telegram
    send_signal(signal, confidence, prediction)

# Run once
if __name__ == "__main__":
    run_xshooter()
