text = input("Input: ")
vowels = "aeiouAEIOU"
for v in vowels:
    text = text.replace(v, "")
print(text)

