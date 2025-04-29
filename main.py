from config import BOT_NAME, USER_NAME
from chatbot import get_response
from utils import delay_print, print_bubble, show_typing
from utils import save_username, load_username
from utils import get_daily_quote, save_chat_log

MOOD = "ceria"

# Load nama user
name = load_username()
if not name:
    name = USER_NAME
    save_username(name)

# Sambutan awal
print_bubble(f"Halo! Aku {BOT_NAME}, chatbot AI buatan {USER_NAME}", sender="bot")
print_bubble("Selalu siap nemenin kamu kapan aja!", sender="bot")
print_bubble(f"Mood Jeongie sekarang: {MOOD}", sender="bot")
print_bubble("Ketik /mood untuk mengubah mood Jeongie", sender="bot")
print_bubble(f"Halo {name}! Aku senang banget bisa ketemu kamu lagi!", sender="bot")

# Mulai percakapan
while True:
    try:
        user_input = input(f"{USER_NAME}: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            response = f"Sampai jumpa lagi, {USER_NAME}!"
            print_bubble(response, sender="bot")
            save_chat_log(BOT_NAME, response)
            break

        elif user_input == "":
            continue

        elif user_input.lower() == "/mood":
            print_bubble("Pilih mood Jeongie: ceria / tenang / jahil / galau", sender="bot")
            new_mood = input(f"{USER_NAME} (pilih mood): ").strip().lower()
            if new_mood in ["ceria", "tenang", "jahil", "galau"]:
                MOOD = new_mood
                print_bubble(f"Oke! Mood Jeongie sekarang: {MOOD}", sender="bot")
            else:
                print_bubble("Mood itu belum aku kenal, pilih yang tersedia ya~", sender="bot")
            continue

        # Umum (tanpa mencetak input user)
        save_chat_log(USER_NAME, user_input)
        show_typing()
        response = get_response(user_input, mood=MOOD)
        print_bubble(response, sender="bot")
        save_chat_log(BOT_NAME, response)

    except Exception as e:
        print_bubble("Oops! Ada kesalahan di sistemku... Coba lagi ya!", sender="bot")