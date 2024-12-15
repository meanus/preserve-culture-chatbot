import nltk
from nltk.stem import WordNetLemmatizer

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Define festival data
festivals = {
    "diwali": {
        "description": "Diwali is the Hindu festival of lights, celebrated over five days. It symbolizes the triumph of light over darkness and good over evil.",
        "origin": "Diwali is believed to have originated from the legend of Rama and Sita. When Rama returned to Ayodhya after a 14-year exile, the people of Ayodhya lit diyas to illuminate his path.",
        "details": [
            "Diwali is celebrated on the 15th day of the Kartik month in the Hindu calendar.",
            "It is a major festival in Hinduism, Jainism, and Sikhism.",
            "During Diwali, people decorate their homes with lights, candles, and diyas.",
            "They also worship the goddess Lakshmi, the deity of wealth and prosperity."
        ]
    },
    "holi": {
        "description": "Holi is the Hindu festival of colors, celebrated over two days. It marks the arrival of spring and the victory of good over evil.",
        "origin": "Holi is believed to have originated from the legend of Hiranyakashyap and his son Prahlad. Hiranyakashyap forbade Prahlad from worshipping Vishnu, but Prahlad continued to do so. Hiranyakashyap tried to kill Prahlad, but he was saved by Vishnu.",
        "details": [
            "Holi is celebrated on the full moon day in the month of Phalguna in the Hindu calendar.",
            "It is a major festival in Hinduism, celebrated with great enthusiasm and fervor.",
            "During Holi, people throw colored powders and liquids at each other, symbolizing the colors of spring.",
            "They also light bonfires, known as Holika Dahan, to mark the victory of good over evil."
        ]
    },
    "eid al-fitr": {
        "description": "Eid al-Fitr is a significant festival in Islam, marking the end of Ramadan, the Islamic holy month of fasting.",
        "origin": "Eid al-Fitr is believed to have originated in the 7th century, when the Prophet Muhammad received a revelation from Allah to celebrate the end of Ramadan.",
        "details": [
            "Eid al-Fitr is celebrated on the first day of the month of Shawwal in the Islamic calendar.",
            "It is a day of feasting, gift-giving, and charity.",
            "During Eid al-Fitr, Muslims gather for congregational prayers, known as Salat al-Eid.",
            "They also visit family and friends, exchange gifts, and engage in acts of charity."
        ]
    }
}

# Function to generate chatbot responses for festivals
def generate_response(festival_name):
    festival_name = festival_name.lower()
    if festival_name in festivals:
        return festivals[festival_name]["description"]
    else:
        return "Sorry, I'm not familiar with that festival."

def provide_details(festival_name):
    festival_name = festival_name.lower()
    if festival_name in festivals:
        return "\n".join(festivals[festival_name]["details"])
    else:
        return "Sorry, I'm not familiar with that festival."

def provide_origin(festival_name):
    festival_name = festival_name.lower()
    if festival_name in festivals:
        return festivals[festival_name]["origin"]
    else:
        return "Sorry, I'm not familiar with that festival."

# Dance-related data
dances = {
    "bharatanatyam": {
        "history": "Bharatanatyam is one of the oldest classical dance forms of India, originating from Tamil Nadu. It is a temple dance performed as an offering to the deities.",
        "state": "Tamil Nadu"
    },
    "kathak": {
        "history": "Kathak is a classical dance form from North India. It originated as a storytelling dance performed in temples and later evolved in the courts of Mughal emperors.",
        "state": "Uttar Pradesh"
    },
    "odissi": {
        "history": "Odissi is a classical dance from Odisha. It is known for its graceful movements and sculpturesque poses, and it has its roots in ancient temple dance.",
        "state": "Odisha"
    },
    "kathakali": {
        "history": "Kathakali is a traditional dance-drama from Kerala. It combines dance, music, and acting to tell stories from Hindu mythology, often focusing on the divine.",
        "state": "Kerala"
    }
}

# Function to display dance-related information
def learn_about_dance():
    print("\nIndia has many classical dance forms, including Bharatanatyam, Kathak, Odissi, and Kathakali.")
    print("Each dance has its unique style and cultural significance.")
    
    dance_choice = input("\nWhich dance would you like to learn about? (Bharatanatyam/Kathak/Odissi/Kathakali): ").lower()

    if dance_choice in dances:
        print("\n" + dances[dance_choice]["history"])
        state = dances[dance_choice]["state"]
        print(f"The dance is primarily performed in {state}.")
        
        # Ask if the user wants to know more about the dance history
        response = input("\nWould you like to know more about the history of this dance? (yes/no): ")
        if response.lower() == "yes":
            print("\n" + dances[dance_choice]["history"])

        # Ask if the user wants to know which state the dance is performed in
        response = input("\nWould you like to know where this dance is performed? (yes/no): ")
        if response.lower() == "yes":
            print(f"\nThis dance is performed in {state}.")
    else:
        print("Sorry, I'm not familiar with that dance form.")

# Attire-related data
attires = {
    "saree": {
        "history": "The saree is a traditional Indian garment worn by women. It consists of a long piece of cloth, usually around 5-9 yards, that is draped elegantly around the body.",
        "states": ["Tamil Nadu", "Karnataka", "Maharashtra", "Uttar Pradesh", "West Bengal"],
        "materials": ["silk", "cotton", "georgette", "chiffon"]
    },
    "salwar kameez": {
        "history": "Salwar kameez is a traditional outfit for women consisting of a tunic (kameez), paired with loose-fitting pants (salwar) and a scarf or shawl (dupatta).",
        "states": ["Punjab", "Delhi", "Rajasthan", "Kashmir"],
        "materials": ["cotton", "silk", "georgette", "chiffon"]
    },
    "dhoti": {
        "history": "The dhoti is a traditional garment worn by men in India. It is a long piece of cloth wrapped around the waist and knotted at the waist, typically worn during formal occasions.",
        "states": ["Maharashtra", "Tamil Nadu", "Bengal", "Kerala"],
        "materials": ["cotton", "silk"]
    },
    "kurta-pajama": {
        "history": "Kurta-pajama is a traditional outfit worn by men in India. The kurta is a tunic, and the pajama is a loose-fitting trouser.",
        "states": ["Delhi", "Punjab", "Uttar Pradesh", "Haryana"],
        "materials": ["cotton", "silk", "linen"]
    }
}

# Function to display attire-related information
def learn_about_attire():
    print("\nIndia's traditional attire includes sarees, salwar kameez, dhotis, and kurta-pajamas.")
    print("Each region has its unique styles, fabrics, and designs.")
    
    attire_choice = input("\nWhich attire would you like to learn about? (Saree/Salwar Kameez/Dhoti/Kurta-Pajama): ").lower()

    if attire_choice in attires:
        print("\n" + attires[attire_choice]["history"])
        print(f"This attire is typically worn in the following states: {', '.join(attires[attire_choice]['states'])}.")
        print(f"Common materials used for making this attire include: {', '.join(attires[attire_choice]['materials'])}.")
        
        # Ask if the user wants to know where the attire is worn
        response = input("\nWould you like to know where this attire is worn in more detail? (yes/no): ")
        if response.lower() == "yes":
            print(f"\nThis attire is primarily worn in the states: {', '.join(attires[attire_choice]['states'])}.")
        
        # Ask if the user wants to know about the materials used
        response = input("\nWould you like to know the materials used to make this attire? (yes/no): ")
        if response.lower() == "yes":
            print(f"\nMaterials used: {', '.join(attires[attire_choice]['materials'])}.")
    else:
        print("Sorry, I'm not familiar with that attire.")

# Food-related data
def learn_about_food():
    print("\nIndian cuisine is known for its spices and flavors. Popular dishes include biryani, dosa, samosas, and butter chicken.")
    print("Each region offers unique and delicious specialties.")

    # Ask if the user wants to know where the foods are prepared
    response = input("\nWould you like to know where these foods are typically prepared? (yes/no): ")
    if response.lower() == "yes":
        print("\nHere are some regions where specific foods are prepared:")
        print("Biryani - Hyderabad, Lucknow, Kolkata")
        print("Dosa - Tamil Nadu, Karnataka")
        print("Samosas - Across India, especially in Delhi and Mumbai")
        print("Butter Chicken - Punjab, Delhi")

# Languages-related data
def learn_about_languages():
    print("\nIndia is a linguistically diverse country with over 120 major languages spoken across the country.")
    print("Some of the main languages spoken in India include Hindi, Bengali, Telugu, Marathi, Tamil, Urdu, and Gujarati.")
    
    # Ask if the user wants to know about the main languages
    response = input("\nWould you like to know more about the main languages of India? (yes/no): ")
    if response.lower() == "yes":
        print("\nHere are some of the main languages spoken in India:")
        print("1. Hindi - Widely spoken in North India and recognized as the official language of India.")
        print("2. Bengali - Primarily spoken in West Bengal and Bangladesh.")
        print("3. Telugu - A Dravidian language spoken in Andhra Pradesh and Telangana.")
        print("4. Marathi - Spoken mainly in Maharashtra.")
        print("5. Tamil - Spoken in Tamil Nadu and Sri Lanka.")
        print("6. Urdu - Widely spoken in Jammu & Kashmir, Uttar Pradesh, and Delhi.")
        print("7. Gujarati - Spoken in Gujarat and among the Indian diaspora worldwide.")

# Main program loop
print("Welcome to the Indian Culture Chatbot!")
while True:
    print("\nWhat would you like to learn about?")
    print("1. Festivals")
    print("2. Dance")
    print("3. Attire")
    print("4. Food")
    print("5. Languages")
    choice = input("Enter the number of your choice: ")
    
    if choice == "1":
        # Learn about festivals
        while True:
            print("\nWhich festival would you like to learn about?")
            print("1. Diwali")
            print("2. Holi")
            print("3. Eid al-Fitr")
            festival_choice = input("Enter the number of your choice: ")

            if festival_choice == "1":
                festival_name = "diwali"
            elif festival_choice == "2":
                festival_name = "holi"
            elif festival_choice == "3":
                festival_name = "eid al-fitr"
            elif festival_choice =="no":
                break
            else:
                print("Invalid choice. Please try again.")
                continue

            print("\n" + generate_response(festival_name))

            response = input("\nWould you like to know more details about this festival? (yes/no): ")
            if response.lower() == "yes":
                print("\nDetails:")
                print(provide_details(festival_name))
            else:
                break

            response = input("\nWould you like to know about the origin of this festival? (yes/no): ")
            if response.lower() == "yes":
                print("\nOrigin:")
                print(provide_origin(festival_name))
            else:
                break

            response = input("\nWould you like to learn about another festival? (yes/no): ")
            if response.lower() == "no":
                break

    elif choice == "2":
        # Learn about dance
        learn_about_dance()

    elif choice == "3":
        # Learn about attire
        learn_about_attire()

    elif choice == "4":
        # Learn about food
        learn_about_food()

    elif choice == "5":
        # Learn about languages
        learn_about_languages()

    else:
        print("Invalid choice. Please try again.")
        continue
    
    response = input("\nWould you like to learn about something else? (yes/no): ")
    if response.lower() == "no":
        print("Thank you for using the Indian Culture Chatbot! Goodbye!")