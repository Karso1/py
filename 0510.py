# Python program to perform string operations on a user's name
# Accept user name
name = input("Enter your name: ")

# (1) Display first n characters from left
n = int(input("Enter how many characters you want to display from the left: "))
print("First", n, "characters:", name[:n])

# (2) Count number of vowels in the name
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in name if char in vowels)
print("Number of vowels in your name:", vowel_count)

# (3) Reverse the name
reversed_name = name[::-1]
print("Your name reversed is:", reversed_name)
