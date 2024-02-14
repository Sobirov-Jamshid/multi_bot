
import telebot
import threading

# Replace 'TOKEN_1', 'TOKEN_2', etc. with your actual bot tokens
TOKENS = [
    'token1',
    'token2',
    'token3',
    'token4',
    'token5',
    'token6',
    'token7',
    'token8',
    'token9',
    'token10',
    '...'
]
bots = []

# Create instances of TeleBot for each bot
for token in TOKENS:
    bot = telebot.TeleBot(token)
    bots.append(bot)

# Define handlers for each bot
def handle_message(bot, message):
    bot.send_message(message.chat.id, f"Hello from {bot.get_me().username}!")

for bot in bots:
    @bot.message_handler(func=lambda message: True)
    def message_handler(message, current_bot=bot):
        
        if message.chat.type == "private":
            print("# private chat message")
        if message.chat.type == "group":
            # group chat message
            print("# group")

        if message.chat.type == "supergroup":
            # supergroup chat message
            print("# supergroup")

        if message.chat.type == "channel":
            #channel chat message
            print("# Channel")

        handle_message(current_bot, message)
    
    @bot.channel_post_handler(func=lambda message: True)
    def channel_handler(message):
        print('channeldan', message.text)

# Define a function to run each bot
def run_bot(bot_instance):
    bot_instance.polling(none_stop=True)

# Create threads for each bot
threads = [threading.Thread(target=run_bot, args=(bot,)) for bot in bots]

# Start the threads
for thread in threads:
    thread.start()

try:
    # Keep the main thread running
    while True:
        pass
except KeyboardInterrupt:
    # Handle cleanup when the script is interrupted
    for bot in bots:
        bot.stop_polling()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()
