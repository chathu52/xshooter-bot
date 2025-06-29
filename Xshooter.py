# Xshooter.py
import asyncio
import csv
import datetime
import os
import telegram
import os.path

from dotenv import load_dotenv
from claude_predictor import get_signal_prediction

# Load environment variables
load_dotenv()
TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
CLAUDE_API_KEY = os.environ["CLAUDE_API_KEY"]

# Initialize bot
bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

# CSV file to log all data
CSV_FILE = "xshooter_log.csv"

# Function to save to CSV
def log_to_csv(date, time, signal, crash_data, confidence):
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date", "Time", "Signal", "Crash Data", "Confidence"])
        row = [date, time, signal, "|".join(map(str, crash_data)), confidence]
        writer.writerow(row)

# Function to send message to Telegram
def send_signal_to_telegram(signal, confidence):
    message = f"""✈ *Xshooter Signal*
🔫 Signal: *{signal}*
📶 Confidence: *{confidence:.2f}%*"""

    async def send():
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message.strip(), parse_mode='Markdown')

    asyncio.run(send())  # Await the coroutine properly

# Dummy function to simulate crash round (you can replace with real input or Telegram button)
def run_xshooter():
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")
    signal = "BET"
    crash_data = ["1.1x", "1.2x", "✅", "x", "x"]

    # Get AI prediction
    prediction, confidence = get_signal_prediction(crash_data, CLAUDE_API_KEY)

    # Send to Telegram
    send_signal_to_telegram(prediction, confidence)

    # Save to CSV
    log_to_csv(date, time, prediction, crash_data, confidence)

# Run the logic
run_xshooter()
