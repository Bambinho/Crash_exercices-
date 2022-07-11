
def show_messages(messages):
	while messages:
		message=messages.pop()
		print(f"{message}")
		sent_message.append(message)


text_messages=['I am sending this message for you','to let you know that I am applying for a job','that I saw posting','in your website']
sent_message=[]


show_messages(text_messages[:])
print(sent_message)
print(text_messages)
print("\n\n")
show_messages(text_messages)

print(sent_message)
print(text_messages)