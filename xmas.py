import openai

# Christmas themes and content
christmas_trivia = [
    "Did you know Rudolph the Red-Nosed Reindeer was created as a marketing gimmick in 1939?",
    "The first Christmas card was created in England in 1843.",
    "The tradition of Christmas trees originated in Germany.",
    "Santa Claus’s sleigh is said to be powered by 9 magical reindeer!",
    "Jingle Bells was originally written for Thanksgiving, not Christmas!"
]

christmas_songs = {
    "Jingle Bells": "🎵 Jingle bells, jingle bells, jingle all the way! Oh, what fun it is to ride in a one-horse open sleigh! 🎵",
    "We Wish You a Merry Christmas": "🎵 We wish you a Merry Christmas, and a Happy New Year! 🎵",
    "Silent Night": "🎵 Silent night, holy night, all is calm, all is bright. 🎵"
}

def get_christmas_response(user_input):
    # Add festive flair
    if "trivia" in user_input.lower():
        return f"🎄 {random.choice(christmas_trivia)} 🎁"
    elif "sing" in user_input.lower() or "song" in user_input.lower():
        song = random.choice(list(christmas_songs.keys()))
        return f"🎶 Here's a snippet of '{song}': {christmas_songs[song]}"
    elif "gift idea" in user_input.lower():
        return "🎁 How about gifting a cozy blanket, a good book, or a holiday-themed mug? Perfect for the season!"
    elif "merry christmas" in user_input.lower():
        return "🎅 Ho ho ho! Merry Christmas to you too! 🎄"
    else:
        return "🎄 I'm here to spread Christmas cheer! Ask me for trivia, songs, or holiday tips! 🎅"

def chat_with_ai():
    print("🎄 Welcome to the Christmas AI chatbot! 🎅")
    print("Type 'exit' to end the chat. 🎁\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("🎄 Goodbye, and have a magical Christmas! 🎅")
            break

        # Get festive response from AI
        response = get_christmas_response(user_input)
        print(f"Christmas AI: {response}")

# Start the chatbot
if __name__ == "__main__":
    import random
    chat_with_ai()
