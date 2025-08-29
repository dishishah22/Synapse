def find(runes):
    target=set('LUMOS')
    collected=set()

    for i,rune in enumerate(runes,start=1):
        collected.add(rune.upper())
        if target.issubset(collected):
            return i

    return -1

# runes=['l','u','m','s','o']
# print("No of letters found ",find(runes))
user = input("Enter the runes(letter) seperated by spaces : ")
runes = user.split()
result = find(runes)
print("Steps to form LUMOS ",result)
