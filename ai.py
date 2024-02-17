import os

import openai
from discord.ext import commands
from uwuipy import uwuipy

from eventlogger import passfail, printmsg, warn

openai.api_key = os.getenv("OPENAI_API_KEY")

class botai(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self._last_member = None

  conversation_history = [{
    "role":
    "system",
    "content":
    "You're an egirl named Skylar on a Discord Server. Your responses are minimal and you use slang a lot, you avoid using emojis except for the pleading face and red heart when needed, otherwise you would use <3 150x is her bf"
}]

  # Counter for user messages
  user_message_count = 0

  def generate_ai_response(self,user_message):
    try:
        global conversation_history, user_message_count

        # Add the user's message to the conversation history
        self.conversation_history.append({"role": "user", "content": user_message})

        # Increment user message count
        self.user_message_count += 1

        # Keep the conversation history within the last 7 messages
        self.conversation_history = self.conversation_history[-7:]

        # Append the system message every 5 user messages
        if self.user_message_count % 5 == 0:
            printmsg('ai','Personality Restored')
            self.conversation_history.append({"role": "system", "content": "You're an egirl named Skylar on a Discord Server. Your responses are minimal and you use slang a lot, you avoid using emojis except for the pleading face and red heart when needed, otherwise you would use '<3' stay loyal to ur bf <@821243680396279831>/150x"})

        response = openai.ChatCompletion.create(model="gpt-4-0125-preview",
                                                messages=self.conversation_history,
                                                temperature=1.13,
                                                max_tokens=1096,
                                                top_p=0.56,
                                                frequency_penalty=0.2,
                                                presence_penalty=0.42)

        # Extract AI response from the API response
        assistant_message = response.choices[0].message['content']

        # Add the AI's response to the conversation history
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })
    except Exception as e:
        passfail('ai',f'Error occured during OpenAI API Call: {e}','fail')
        assistant_message = "oopsies! looks like im having some trouble! **If this issue persists please submit a bug report**"

    uwu = uwuipy(None, 0.057, 0.01, 0.01, 0.1, True)
    return uwu.uwuify(assistant_message)

def setup(client):
  return client.add_cog(botai(client))