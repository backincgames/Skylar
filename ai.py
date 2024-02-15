import os

import openai
from uwuipy import uwuipy

openai.api_key = os.getenv("OPENAI_API_KEY")

# Keep track of the conversation history
conversation_history = [{
    "role":
    "system",
    "content":
    "You're an egirl named Skylar on a Discord Server. Your responses are minimal and you use slang a lot, you avoid using emojis except for the pleading face and red heart when needed, otherwise you would use <3"
}]

# Counter for user messages
user_message_count = 0

def generate_ai_response(user_message):
    try:
        global conversation_history, user_message_count

        # Add the user's message to the conversation history
        conversation_history.append({"role": "user", "content": user_message})

        # Increment user message count
        user_message_count += 1

        # Keep the conversation history within the last 7 messages
        conversation_history = conversation_history[-7:]

        # Append the system message every 5 user messages
        if user_message_count % 5 == 0:
            print('[AI]: Personality File Restored')
            conversation_history.append({"role": "system", "content": "You're an egirl named Skylar on a Discord Server. Your responses are minimal and you use slang a lot, you avoid using emojis except for the pleading face and red heart when needed, otherwise you would use <3"})

        response = openai.ChatCompletion.create(model="gpt-4-0125-preview",
                                                messages=conversation_history,
                                                temperature=1.13,
                                                max_tokens=1096,
                                                top_p=0.56,
                                                frequency_penalty=0.2,
                                                presence_penalty=0.42)

        # Extract AI response from the API response
        assistant_message = response.choices[0].message['content']

        # Add the AI's response to the conversation history
        conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })
    except Exception as e:
        print(f"Error occurred during OpenAI API call: {e}")
        assistant_message = "oopsies! looks like im having some trouble! **If this issue persists please submit a bug report**"

    uwu = uwuipy(None, 0.057, 0.01, 0.01, 0.1, True)
    return uwu.uwuify(assistant_message)
