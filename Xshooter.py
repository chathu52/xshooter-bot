import datetime
import asyncio
import os
import csv
import os.path

from config import CLAUDE_API_KEY, TELEGRAM_CHAT_ID
from claude_predictor import get_signal_prediction  # Or adjust to your structure

CSV_FILE = "xshooter_log.csv"

async def send():
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")

    # Dummy crash data (replace with actual input)
    crash_data = ["1.2x", "1.3x", "1.1x", "1.5x", "1.2x"]

    # Retry Claude API up to 3 times
    for i in range(3):
        try:
            prediction, confidence = get_signal_prediction(crash_data, CLAUDE_API_KEY)
            break
        except Exception as e:
            if i < 2:
                await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=f"⚠️ Retrying Claude... attempt {i+1}")
                await asyncio.sleep(2)
            else:
                await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text="❌ Claude API failed after 3 attempts.")
                raise e

    # Format and send Telegram signal message
    message = f"✈️ *Xshooter Signal*\n\n*Signal:* {prediction}\n*Confidence:* {confidence:.2f}%"
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message.strip(), parse_mode='Markdown')

    # Log to CSV
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date", "Time", "Signal", "Crash Data", "Confidence"])
        row = [date, time_str, prediction, "|".join(map(str, crash_data)), confidence]
        writer.writerow(row)
