# Simple spam detection program
# The program scans an email message and assigns a spam score
# based on common spam words and phrases.

def get_spam_keywords():
    # 30 common spam words/phrases
    return [
        "free",
        "win",
        "winner",
        "cash",
        "prize",
        "urgent",
        "limited time",
        "act now",
        "click here",
        "risk free",
        "guaranteed",
        "congratulations",
        "exclusive deal",
        "buy now",
        "cheap",
        "credit card",
        "earn money",
        "extra income",
        "million dollars",
        "no cost",
        "offer expires",
        "trial",
        "claim now",
        "investment",
        "weight loss",
        "miracle",
        "luxury",
        "hot singles",
        "password",
        "verify account"
    ]


def scan_message(message, keywords):
    spam_score = 0
    found_words = []

    lower_message = message.lower()

    for word in keywords:
        count = lower_message.count(word)
        if count > 0:
            spam_score += count
            found_words.append((word, count))

    return spam_score, found_words


def rate_spam(score):
    if score == 0:
        return "Very unlikely to be spam"
    elif score <= 3:
        return "Low chance of spam"
    elif score <= 7:
        return "Moderate chance of spam"
    elif score <= 12:
        return "High chance of spam"
    else:
        return "Very likely spam"


def main():
    print("Spam Detection Program")
    print("----------------------")

    message = input("Enter an email message:\n")

    keywords = get_spam_keywords()
    score, found = scan_message(message, keywords)
    rating = rate_spam(score)

    print("\nSpam Score:", score)
    print("Likelihood:", rating)

    if found:
        print("\nSpam words/phrases detected:")
        for word, count in found:
            print(f"- '{word}' found {count} time(s)")
    else:
        print("\nNo spam keywords detected.")


main()
