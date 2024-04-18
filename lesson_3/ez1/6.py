str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

'Dino' in str1
'Dino' in str2

#7
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]

flintstones.append('Dino')

#8
flintstones.extend(["Dino", "Hoppy"])

#9 
advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as

print(advice.split("house")[0])

#10
advice = "Few things in life are as important as house training your pet dinosaur."

print(advice.replace("important", "urgent"))