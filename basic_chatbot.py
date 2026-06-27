import random

bot_name = 'Chad'
greetings = ['Hi there!', 'Wassup!', 'Hey! How is it going?']

print(f"Hello! I'm {bot_name}! How can I help you today?")

while True:
    user_input = input('You: ').strip().lower()

    if not user_input:
        print(f'{bot_name}: Please type something...')
        continue
    
    elif user_input in ['hi', 'hello', 'hey', 'yo', 'wassup']:
        print(f'{bot_name}: {random.choice(greetings)}')
    
    elif user_input in ['bye', 'goodbye', 'see you' , 'see ya', 'exit']:
        print(f'{bot_name}: Goodbye! Have a great day!')
        break

    else:
        print(f"{bot_name}: I'm sorry I don't understand that. Please try again.")



