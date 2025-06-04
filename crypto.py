# crypto_buddy.py

print("👋 Hi there! I'm CryptoBuddy — your AI-powered financial sidekick! 💸💚")
print("Let’s find you a green and growing crypto!")

# Sample cryptocurrency database
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8
    }
}

# Function to get user input


def get_user_query():
    return input("\n💬 Ask me anything about crypto (type 'exit' to quit): ").lower()

# Function to respond to user queries


def respond_to_query(query):
    if "sustainable" in query:
        best = max(
            crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(
            f"🌱 Try {best}! It’s eco-friendly and has strong long-term potential.")
    elif "trending" in query or "rising" in query:
        trending = [coin for coin in crypto_db if crypto_db[coin]
                    ["price_trend"] == "rising"]
        print(f"📈 These coins are on the rise: {', '.join(trending)}.")
    elif "long-term" in query or "growth" in query:
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] >= 7:
                print(
                    f"🚀 {coin} is trending up and has a top-tier sustainability score!")
                return
        print("🔍 Couldn't find a perfect match. Try a different question.")
    else:
        print("🤖 Sorry, I didn’t get that. Try asking about sustainability or trends.")

# Bonus: Recommend best overall pick


def best_overall():
    for coin, data in crypto_db.items():
        if data["price_trend"] == "rising" and data["market_cap"] in ["high", "medium"] and data["sustainability_score"] > 7:
            print(f"🏅 Overall top pick: {coin} — profitable and sustainable!")
            return

# Chat loop


def chatbot():
    while True:
        query = get_user_query()
        if query == "exit":
            print("👋 Bye! Remember: Crypto is risky—always do your own research.")
            break
        respond_to_query(query)
        best_overall()


chatbot()
