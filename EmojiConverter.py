def emoji_converter(message):
    words = message.split(' ')
    output = ''
    emojis = {
        ":)": "🙂",
        ":(": "😥",
        ":D": "😀"
    }

    for word in words:
        output += emojis.get(word, word) + " "

    print(output)
