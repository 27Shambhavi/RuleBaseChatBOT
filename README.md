# Rule-Based Chatbot

## Overview
This is a simple rule-based chatbot that responds to user inputs based on predefined rules. It uses **Natural Language Processing (NLP)** techniques such as tokenization, stemming, and lemmatization to improve response matching.

## Features
- Responds to greetings, farewells, and common queries.
- Uses **NLTK** for text processing.
- Supports **lemmatization and stemming** for better understanding.
- Handles unknown responses gracefully.
- Allows users to exit by typing 'exit', 'bye', or 'see you'.

## Installation
### Prerequisites
Ensure you have Python installed (preferably **Python 3.7+**).

### Steps
1. Clone or download this repository.
2. Install required dependencies using:
   ```bash
   pip install nltk
   ```
3. Run the chatbot:
   ```bash
   python enhanced_chatbot.py
   ```

## Usage
- Start the chatbot by running the script.
- Type a message (e.g., "hello", "tell me a joke").
- The chatbot will respond accordingly.
- Type 'exit' to quit the conversation.

## Example Interaction
```
YOU: Hello
Chatbot: Hi! How can I assist you today?

YOU: What is the weather like?
Chatbot: I'm not a weather bot, but I hope it's sunny!

YOU: Bye
Chatbot: Goodbye! Take care!
```

## Future Improvements
- Adding AI-based responses using machine learning.
- Integrating external APIs (e.g., weather, news).
- Enhancing conversation flow with memory and context tracking.

## License
This project is open-source. Feel free to modify and improve it!

