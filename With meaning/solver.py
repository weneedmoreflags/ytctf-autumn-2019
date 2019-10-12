with open("cipher", "rt") as cipher:
    cipher_text = cipher.read()

with open("Message.txt", "rt") as message:
    message_text = message.read()

pairs = [
            (int(pair.split('.')[0]), int(pair.split('.')[1]))
            for pair in cipher_text.split()
        ]

flag = ""
message_rows = message_text.split('\n')
for row, column in pairs:
    flag += message_rows[row][column]

print(flag)
