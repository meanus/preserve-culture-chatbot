def generate_response(user_message):
    # Lowercase the message to make matching case insensitive
    user_message = user_message.lower()

    # Respond based on what the user asked about
    if "festival" in user_message:
        return "Which festival would you like to know about? (e.g., Diwali, Holi, Eid, Navratri)"
    elif "diwali" in user_message:
        return get_festival_info("diwali")
    elif "holi" in user_message:
        return get_festival_info("holi")
    elif "eid" in user_message:
        return get_festival_info("eid")
    elif "navratri" in user_message:
        return get_festival_info("navratri")
    elif "dance" in user_message:
        return "What type of dance would you like to know about? (e.g., Bharatnatyam, Kathak, Odissi)"
    elif "bharatnatyam" in user_message:
        return get_dance_info("bharatnatyam")
    elif "kathak" in user_message:
        return get_dance_info("kathak")
    elif "odissi" in user_message:
        return get_dance_info("odissi")
    elif "food" in user_message:
        return "What type of food would you like to know about? (e.g., Biryani, Dosa, Samosa)"
    elif "biryani" in user_message:
        return get_food_info("biryani")
    elif "dosa" in user_message:
        return get_food_info("dosa")
    elif "samosa" in user_message:
        return get_food_info("samosa")
    elif "attire" in user_message:
        return "What type of attire would you like to know about? (e.g., Sari, Kurta, Sherwani)"
    elif "sari" in user_message:
        return get_attire_info("sari")
    elif "kurta" in user_message:
        return get_attire_info("kurta")
    elif "sherwani" in user_message:
        return get_attire_info("sherwani")
    elif "languages" in user_message:
        return "What language would you like to know about? (e.g., Hindi, Tamil, Bengali)"
    elif "hindi" in user_message:
        return get_language_info("hindi")
    elif "tamil" in user_message:
        return get_language_info("tamil")
    elif "bengali" in user_message:
        return get_language_info("bengali")
    else:
        return "Sorry, I didn't understand that. Can you please be more specific?"

def get_festival_info(festival):
    festival_data = {
        "diwali": "Diwali is the festival of lights, celebrated by Hindus, Sikhs, Jains, and Buddhists. It signifies the victory of light over darkness.",
        "holi": "Holi is the festival of colors, celebrated by Hindus to mark the arrival of spring.",
        "eid": "Eid is a Muslim festival marking the end of Ramadan, known for feasts and charity.",
        "navratri": "Navratri is a Hindu festival that celebrates the goddess Durga. It's a time for fasting, prayer, and dance."
    }
    return festival_data.get(festival, "Sorry, I don't have information on that festival.")

def get_dance_info(dance):
    dance_data = {
        "bharatnatyam": "Bharatnatyam is a classical dance form originating from Tamil Nadu, known for its graceful movements.",
        "kathak": "Kathak is a classical dance form from North India, known for its storytelling and footwork.",
        "odissi": "Odissi is a classical dance from Odisha, known for its fluid movements and temple-inspired poses."
    }
    return dance_data.get(dance, "Sorry, I don't have information on that dance style.")

def get_food_info(food):
    food_data = {
        "biryani": "Biryani is a flavorful rice dish with meat or vegetables, commonly made in India and Pakistan.",
        "dosa": "Dosa is a thin, crispy pancake made from rice and lentil batter, popular in South India.",
        "samosa": "Samosa is a fried pastry filled with spiced potatoes, peas, and sometimes meat, commonly served as a snack."
    }
    return food_data.get(food, "Sorry, I don't have information on that food item.")

def get_attire_info(attire):
    attire_data = {
        "sari": "A sari is a traditional Indian garment worn by women, consisting of a long piece of cloth draped elegantly.",
        "kurta": "A kurta is a loose-fitting tunic worn by both men and women, typically paired with trousers or leggings.",
        "sherwani": "A sherwani is a formal coat worn by men, often during weddings and other celebrations."
    }
    return attire_data.get(attire, "Sorry, I don't have information on that attire.")

def get_language_info(language):
    language_data = {
        "hindi": "Hindi is one of the most widely spoken languages in India, written in the Devanagari script.",
        "tamil": "Tamil is a Dravidian language spoken primarily in Tamil Nadu and Sri Lanka.",
        "bengali": "Bengali is spoken in the Indian state of West Bengal and Bangladesh, written in the Bengali script."
    }
    return language_data.get(language, "Sorry, I don't have information on that language.")
