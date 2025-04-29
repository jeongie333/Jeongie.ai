import time
import sys
import random
import os
from datetime import datetime
from time import sleep
from colorama import Fore, Style, init
init(autoreset=True)

CYAN = "\033[96m"
RESET = "\033[0m"

def delay_print(text, delay=0.5):
    for line in text.split('\n'):
        print(line)
        time.sleep(delay)

def print_bubble(message, sender="bot", user_name="STAR", delay=0.03):
    timestamp = datetime.now().strftime("[%H:%M]")
    if sender == "user":
        print(f"{timestamp} {user_name}: [{message}]")
    else:
        # Nama Jeongie saja yang diwarnai
        colored_name = f"{CYAN}Jeongie{RESET}"
        bubble_prefix = f"{timestamp} {colored_name}: ["
        sys.stdout.write(bubble_prefix)
        sys.stdout.flush()
        type_text(message, delay)
        print("]")

def show_typing(delay=1.5):
    message = f"{CYAN}Jeongie is typing...{RESET}"
    sys.stdout.write(message)
    sys.stdout.flush()
    time.sleep(delay)
    sys.stdout.write("\r" + " " * len(message) + "\r")  # Hapus teks
    sys.stdout.flush()

def type_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline setelah selesai ngetik

def get_current_time():
    return datetime.now().strftime("Sekarang pukul %H:%M WIB")

def get_current_date():
    now = datetime.now()
    hari = now.strftime("%A")
    indo_day = {
        "Monday": "Senin", "Tuesday": "Selasa", "Wednesday": "Rabu",
        "Thursday": "Kamis", "Friday": "Jumat",
        "Saturday": "Sabtu", "Sunday": "Minggu"
    }
    hari_indo = indo_day.get(hari, hari)
    tanggal = now.strftime("%d %B %Y")
    return f"Hari ini hari {hari_indo}, tanggal {tanggal}"

def save_username(name, filename="user_data.txt"):
    with open(filename, "w") as f:
        f.write(name.strip())

def load_username(filename="user_data.txt"):
    try:
        with open(filename, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def get_daily_quote():
    quotes = [
        "Kamu hebat karena kamu tetap bertahan sejauh ini.",
        "Hari ini adalah peluang baru untuk menjadi versi terbaik dari dirimu.",
        "Kamu nggak sendiri. Jeongie di sini buat kamu.",
        "Langkah kecil hari ini bisa jadi lompatan besar nanti.",
        "Jangan lupa istirahat. Energi kamu juga berhak dipulihkan.",
        "Nggak harus sempurna, cukup kamu terus bergerak."
    ]
    today = datetime.now().strftime("%Y-%m-%d")
    seed = int(today.replace("-", ""))
    random.seed(seed)
    return random.choice(quotes)
    
def get_chat_log_filename():
    today = datetime.now().strftime("%Y-%m-%d")
    return f"chat_logs/chat_{today}.txt"

def save_chat_log(sender, message):
    filename = get_chat_log_filename()
    os.makedirs("chat_logs", exist_ok=True)
    with open(filename, "a", encoding="utf-8") as file:
        time = datetime.now().strftime("%H:%M")
        file.write(f"[{time}] {sender.upper()}: {message}\n")
        
