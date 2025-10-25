def emojis_mapping(message):
    emojis = {
    ":)": "😃 ",
    ":(": "😔",
    "$": "🤑"
}
    words = message.split()
    output = ""
    for word in words:
        output +=emojis.get(word, word) + " "
    return output


message = input("message: ")
print(emojis_mapping(message))