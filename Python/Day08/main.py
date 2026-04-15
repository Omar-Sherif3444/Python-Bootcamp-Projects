# def greet():
#     print("hello ")
#     print("shady ")
#     print("academya")
#
# greet()
#*************************************************
# def greet_with_name(name):
#     print("hello "+name )
#     print("how is your day?,"+name)
#     print("what do you want to do?,"+name)
#
# name=input("Enter Your Name:\n")
# greet_with_name(name)

# def life_in_weeks(age):
#     weeks = (90 - age) * 52
#     return weeks
#
# age = int(input("Enter your age: "))
# weeks = life_in_weeks(age)
#
# print("You have " + str(weeks) + " weeks left.")

# def greet2(name,location):
#     print(f"hello {name}")
#     print(f"what is it like in  {location}")
# name=input("what is your name?\n")
# location=input("enter your location\n")
# greet2(name,location)
#
# def greet3(name,location):
#     print(f"hello {name}")
#     print(f"what is it like in {location}")
#
# greet3(location="cairo",name="smoozie")

# def calculate_love_score(name1, name2):
#     t_count = r_count = u_count = e_count = 0
#     l_count = o_count = v_count = 0
#
#     combined_names = (name1 + name2).upper()
#
#     for letter in combined_names:
#         if letter == 'T':
#             t_count += 1
#         elif letter == 'R':
#             r_count += 1
#         elif letter == 'U':
#             u_count += 1
#         elif letter == 'E':
#             e_count += 1
#         elif letter == 'L':
#             l_count += 1
#         elif letter == 'O':
#             o_count += 1
#         elif letter == 'V':
#             v_count += 1
#
#     total1 = t_count + r_count + u_count + e_count
#     total2 = l_count + o_count + v_count + e_count
#
#     love_score = int(str(total1) + str(total2))
#     return love_score
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt ,type 'decode' to decrypt:\n ").lower()
text = input("enter your message: \n").lower()
shift = int(input("Type the shift number:\n"))

# def encrypt(original_text, shift_amount):
#     encrypted_text = ""
#     if direction == "encode":
#         for letter in original_text:
#             position = alphabet.index(letter)
#             if position + shift_amount < 26:
#                 encrypted_letter = alphabet[position + shift_amount]
#                 encrypted_text += encrypted_letter
#             else:
#                 print("invalid shift amount")
#                 return
#         print(encrypted_text)
#
# def decrypt(original_text, shift_amount):
#     decrypted_text = ""
#     if direction == 'decode':
#         for letter in original_text:
#             position = alphabet.index(letter)
#             if position - shift_amount >= 0:
#                 decrypted_letter = alphabet[position - shift_amount]
#                 decrypted_text += decrypted_letter
#             else:
#                 print("invalid shift amount")
#                 return
#         print(decrypted_text)
#
# encrypt(text, shift)
# decrypt(text, shift)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char.isalpha():
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}\n")

run = True
while run:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  if shift > 26:
    shift = shift % shift == 0

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  choice = input("Do you want to run this program again?\nType 'yes' or 'no': ")
  if choice == 'no':
    run = False
    print("Goodbye.")