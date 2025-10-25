phone = {
    "1": "One ",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
phone_number = input("Phone: ")
output = ""
for ch in phone_number:
   output +=(phone.get(ch, "Not Found") + " ")
print(output)
   