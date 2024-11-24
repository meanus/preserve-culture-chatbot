import tkinter as tk
from tkinter import scrolledtext
from final_chatbot import generate_response  # Import the chatbot functions
from PIL import Image, ImageTk  # Import PIL for image handling

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cultural Festival Chatbot")
        self.root.geometry("450x650")
        self.root.resizable(False, False)

        # Create a frame for the welcome screen
        self.welcome_frame = tk.Frame(self.root, bg="#FF9933")
        self.welcome_frame.pack(fill=tk.BOTH, expand=True)
        
        # Load and set an image as background for the welcome screen
        self.set_background_image(self.welcome_frame, r"C:\Users\MANAS KEDIA\Desktop\culture\moh.png")  # Specify your image path here
        
        # Welcome message
        welcome_message = "🙏 Welcome to Indian Culture Chatbot 🙏\n\nClick on Continue to explore!"
        welcome_label = tk.Label(self.welcome_frame, text=welcome_message, font=("Helvetica", 16), bg="#FF9933", fg="white", justify="center")
        welcome_label.pack(anchor="n", pady=10)

        # Add "Continue" button to proceed to chatbot
        continue_button = tk.Button(self.welcome_frame, text="Continue", font=("Helvetica", 14), bg="#138808", fg="white", command=self.open_chatbot)
        continue_button.pack(side="bottom", pady=20)

        # Create a frame for the chatbot interface (initially hidden)
        self.chat_frame = tk.Frame(self.root, bg="#ffffff")
        self.chat_frame.pack_forget()  # Hide the chat frame initially
        
        # Create the scrollable chat box for conversation display
        self.chat_box = scrolledtext.ScrolledText(self.chat_frame, wrap=tk.WORD, state=tk.DISABLED, font=("Helvetica", 12), height=15, bg="#ffffff", fg="black", bd=0, padx=10, pady=10)
        self.chat_box.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

        # Frame for user input and send button with green background
        self.input_frame = tk.Frame(self.chat_frame, bg="#138808")
        self.input_frame.pack(padx=10, pady=10, fill=tk.X)

        # Entry widget for user input inside a frame to simulate rounded corners
        self.input_field_frame = tk.Frame(self.input_frame, bg="#ffffff", bd=0, relief="flat", highlightthickness=1, highlightcolor="#a2dff7", width=10)
        self.input_field_frame.pack(side=tk.LEFT, padx=10, pady=5, fill=tk.X, expand=True)

        # Create the Entry widget (send box)
        self.input_field = tk.Entry(self.input_field_frame, font=("Helvetica", 12), width=30, relief="flat", fg="black", bg="#ffffff", bd=0, highlightthickness=0)
        self.input_field.pack(side=tk.LEFT, padx=10, pady=5, fill=tk.X, expand=True)

        # Send button with rounded corners and light orange color
        self.send_button = tk.Button(self.input_frame, text="Send", font=("Helvetica", 12), command=self.send_message, bg="#FF9933", fg="white", relief="flat", padx=20, pady=8, bd=0)
        self.send_button.pack(side=tk.RIGHT, padx=10, pady=5)

    def set_background_image(self, frame, image_path):
        # Load the image using Pillow
        img = Image.open(image_path)
        img = img.resize((450, 650), Image.Resampling.LANCZOS)  # Resize the image to fit the window
        photo = ImageTk.PhotoImage(img)

        # Create a label with the image as the background
        background_label = tk.Label(frame, image=photo)
        background_label.image = photo  # Keep a reference to the image
        background_label.place(relwidth=1, relheight=1)  # Make the label cover the entire frame

    def open_chatbot(self):
        # Hide the welcome screen and show the chatbot screen
        self.welcome_frame.pack_forget()  # Hide the welcome frame
        self.chat_frame.pack(fill=tk.BOTH, expand=True)  # Show the chat frame
        
        # Start the chatbot conversation
        self.start_conversation()

    def start_conversation(self):
        # Display initial greeting and options in the chat window
        self.display_message("Hello! I am your Cultural Festival Chatbot.\nWhat would you like to learn about?", "Bot")
        self.display_message("1. Festivals\n2. Dance\n3. Attire\n4. Food\n5. Languages", "Bot")

    def send_message(self):
        # Get the user's message
        user_message = self.input_field.get().strip()

        if user_message:
            self.display_message(user_message, "You")  # Display user message

            # Get chatbot response (connect to your chatbot logic)
            response = generate_response(user_message)

            # Display chatbot response after user message
            self.display_message(response, "Bot")

        # Clear the input field for the next message
        self.input_field.delete(0, tk.END)

    def display_message(self, message, sender):
        # Enable the chat box to insert text
        self.chat_box.config(state=tk.NORMAL)

        # Add the sender's message to the chat box
        self.chat_box.insert(tk.END, f"{sender}: {message}\n\n")

        # Disable the chat box again to prevent manual editing
        self.chat_box.config(state=tk.DISABLED)

        # Scroll to the bottom of the chat window
        self.chat_box.yview(tk.END)

# Create the main window
root = tk.Tk()

# Instantiate and run the chatbot GUI
chatbot_app = ChatbotGUI(root)

# Start the Tkinter main loop
root.mainloop()
