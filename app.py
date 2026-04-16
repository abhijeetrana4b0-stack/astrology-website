from flask import Flask, render_template, request
import os

app = Flask(__name__)

def get_zodiac(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries ♈"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus ♉"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini ♊"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer ♋"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo ♌"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo ♍"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra ♎"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio ♏"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius ♐"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn ♑"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius ♒"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces ♓"
    return "Unknown"

def get_horoscope(sign):
    data = {
        "Aries ♈": "Aaj ka din energetic rahega 💪",
        "Taurus ♉": "Aaj aapko paisa mil sakta hai 💰",
        "Gemini ♊": "Communication strong rahega 🗣️",
        "Cancer ♋": "Family ke sath time spend karo ❤️",
        "Leo ♌": "Confidence high rahega 😎",
        "Virgo ♍": "Kaam me success milegi 📈",
        "Libra ♎": "Balance bana ke rakho ⚖️",
        "Scorpio ♏": "Secret planning successful hogi 🤫",
        "Sagittarius ♐": "Travel ka chance hai ✈️",
        "Capricorn ♑": "Hard work ka result milega 🏆",
        "Aquarius ♒": "New ideas aayenge 💡",
        "Pisces ♓": "Emotional day ho sakta hai 💙"
    }
    return data.get(sign, "")

@app.route('/', methods=['GET', 'POST'])
def home():
    zodiac = ""
    horoscope = ""

    if request.method == 'POST':
        dob = request.form['dob']
        year, month, day = map(int, dob.split('-'))
        zodiac = get_zodiac(day, month)
        horoscope = get_horoscope(zodiac)

    return render_template('index.html', zodiac=zodiac, horoscope=horoscope)

# 👇 IMPORTANT for Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
