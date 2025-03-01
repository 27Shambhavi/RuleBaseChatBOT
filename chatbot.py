import nltk
import random
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download('punkt')
nltk.download("wordnet")
nltk.download("omw-1.4")

class Chatbot:
    def __init__(self):
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()

        # Define rules
        self.rules = {
            "greeting": ["hi", "hello", "hey", "yo"],
            "farewell": ["bye", "exit", "see you", "quit"],
            "joke": ["tell me a joke", "joke", "funny"],
            "name": ["what is your name", "who are you"],
            "how_are_you": ["how are you", "how are you doing"],
            "fav_color": ["what is your favourite colour"],
            "meaning_of_life": ["what is the meaning of life"],
            "real": ["are you real", "do you exist"],
            "weather": ["how is the weather", "what's the weather like"],
            "age": ["how old are you"],
            "hobby": ["what are your hobbies", "what do you like to do"],
            "learn": ["learns", "learning", "learned", "learn"],
        }

        self.responses = {
            "greeting": ["Hi! How can I assist you today?"],
            "farewell": ["Bye! Have a great day!"],
            "joke": ["I told my wife she should embrace her mistakes. She gave me a hug."],
            "name": ["I am Chattyy, your friendly chatbot!"],
            "how_are_you": ["I'm just a bot, but I'm doing great! How about you?"],
            "fav_color": ["I don't have a favorite, but blue seems nice!"],
            "meaning_of_life": ["42, according to Douglas Adams!"],
            "real": ["As real as your imagination!"],
            "weather": ["I'm not a weather bot, but I hope it's sunny!"],
            "age": ["I was created recently, so I'm quite young!"],
            "hobby": ["I love chatting with humans like you!"],
            "learn": ["Learning is a lifelong journey! What are you learning today?"],
        }

    def lemmatize(self, word):
        return self.lemmatizer.lemmatize(word, pos='v')

    def stem(self, word):
        return self.stemmer.stem(word)

    def process_input(self, user_input):
        input_tokens = word_tokenize(user_input.lower())
        lemma_input_tokens = [self.lemmatize(word) for word in input_tokens]

        for rule, phrases in self.rules.items():
            for phrase in phrases:
                phrase_tokens = word_tokenize(phrase.lower())
                lemma_phrase_tokens = [self.lemmatize(word) for word in phrase_tokens]
                if set(lemma_phrase_tokens).issubset(set(lemma_input_tokens)):
                    return rule
        return None

    def get_response(self, user_input):
        rule = self.process_input(user_input)
        if rule and rule in self.responses:
            return random.choice(self.responses[rule])
        return "I'm not sure how to respond to that. Could you rephrase?"

    def chat(self):
        print("Hello! I am your chatbot. Type 'exit' to leave.")
        
        while True:
            user_input = input("YOU: ").strip()
            if user_input.lower() in ['exit', 'bye', 'see you']:
                print("Chatbot: Goodbye! Take care!")
                break
            response = self.get_response(user_input)
            print(f'Chatbot: {response}')

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.chat()
