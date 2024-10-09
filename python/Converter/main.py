
def binary_to_hex(binary:str):
  binary = ' '.join(format(ord(x), 'b') for x in binary)


def main():
  from_choice:str = input("What would you like to convert from: ").lower()
  to_choice:str = input("What would you like to convert to: ").lower()
  convert:str = input("What would you like to convert: ").lower()

  if(from_choice == "binary"):
    if(to_choice == "hex"):
      binary_to_hex(convert)

if(__name__ == "__main__"):
  main()