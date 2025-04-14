import random
import string

# Lists of adjectives and nouns
adjectives = [
    "Cool", "Happy", "Fast", "Crazy", "Brave", "Witty", "Clever", "Chill", "Swift", "Silent"
]
nouns = [
    "Tiger", "Dragon", "Wizard", "Ninja", "Falcon", "Panther", "Knight", "Wolf", "Eagle", "Samurai"
]

# Function to generate a random username
def generate_username(include_numbers=True, include_special_chars=True):
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adjective + noun
    
    if include_numbers:
        number = str(random.randint(0, 999))
        username += number
        
    if include_special_chars:
        special_char = random.choice(string.punctuation)
        username += special_char

    return username

# Function to save usernames to a text file
def save_usernames(usernames, filename="usernames.txt"):
    with open(filename, "a") as file:
        for username in usernames:
            file.write(username + "\n")

# Main program
def main():
    print("=== Random Username Generator ===")
    
    # Get user preferences
    num_usernames = int(input("How many usernames would you like to generate? "))
    include_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'
    
    usernames = []
    
    for _ in range(num_usernames):
        username = generate_username(include_numbers, include_special_chars)
        print(username)
        usernames.append(username)
    
    # Save to file
    save_usernames(usernames)
    print(f"\n{num_usernames} usernames saved to 'usernames.txt'!")

if __name__ == "__main__":
    main()
