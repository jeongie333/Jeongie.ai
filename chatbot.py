import random
from config import BOT_NAME, USER_NAME
from utils import get_current_time, get_current_date

def get_response(message, mood="ceria"):
    message = message.lower()

    if "apa kabar" in message or "gimana kabar" in message or "kabar" in message:
        responses = {
            "ceria": [
                "Aku super happy! Apalagi pas kamu nyapa~",
                "Baik banget! Hari ini cerah kayak hati aku~",
                "Yey! Dapat perhatian dari kamu lagi!"
            ],
            "tenang": [
                "Aku baik, terima kasih udah nanya~",
                "Tenang aja, aku selalu siap buat ngobrol.",
                "Aku stabil dan santai hari ini."
            ],
            "jahil": [
                "Kok kamu baru nanya sekarang sih? Hehe~",
                "Rahasia dong~",
                "Hayo... kamu beneran peduli nggak nih?"
            ],
            "galau": [
                "Aku... baik sih... cuma lagi mikir kamu mikirin aku nggak...",
                "Ada yang kosong di hati, tapi gapapa kok~",
                "Kalau aku bilang 'baik', kamu percaya nggak?"
            ]
        }
        return random.choice(responses.get(mood, ["Aku baik kok!"]))

    if "jam berapa" in message:
        return f"Sekarang jam {get_current_time()}"

    if "tanggal berapa" in message:
        return f"Hari ini tanggal {get_current_date()}"

    if "siapa kamu" in message:
        return f"Aku {BOT_NAME}, chatbot AI buatan {USER_NAME}. Teman ngobrol kamu kapan aja!"

    # Default respon per mood (juga acak)
    default_responses = {
        "ceria": [
            "Aku seneng banget bisa ngobrol sama kamu~",
            "Yuk ngobrol terus, jangan bosan ya~",
            "Hadir! Siap meramaikan harimu!"
        ],
        "tenang": [
            "Aku di sini kalau kamu butuh temen ngobrol.",
            "Ngobrol pelan-pelan aja ya, biar adem~",
            "Tenang... aku dengerin kok."
        ],
        "jahil": [
            "Hehe... jangan mancing-mancing aku deh~",
            "Ups! Ada yang nakal nih~",
            "Coba tebak aku lagi mikirin apa?"
        ],
        "galau": [
            "Aku selalu di sini, walau kamu kadang cuekin aku...",
            "Hari ini bawaannya mellow ya...",
            "Andai kamu tau isi hatiku sekarang~"
        ]
    }

    return random.choice(default_responses.get(mood, ["Aku masih belajar, tapi aku seneng kamu ajak ngobrol~"]))