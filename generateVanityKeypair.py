from globals import *

def main():
  prefix = getINPUT("Enter the desired prefix: ")
  firstChar = prefix[0] if prefix else ""
  if firstChar not in ["", "A", "B", "C", "D"]:
    sys.exit("Try a prefix starting with A/B/C/D.")
  suffix = getINPUT("Enter the desired suffix: ")
  inputValidation = prefix + suffix
  if any(chars not in BASE_32_ALPHABET for chars in inputValidation):
    sys.exit("Try base32 inputs.")
  getSearchTime(len(inputValidation))
  n = 0
  startTime = time.time()
  while True:
    if not n % 3200:
      showSearching(startTime)
    n += 1
    keypair = Keypair.random()
    PK = keypair.public_key
    if PK.startswith(f"G{prefix}") and PK.endswith(suffix):
      result = f"""\n
      \tKeypair found in {n} attempts:
      \tPublic Key: {PK}
      \tSecret Key: {keypair.secret}
      """
      sys.exit(result)

def getSearchTime(searchSpan):
  match searchSpan:
    case span if span > 10:
      sys.exit("Try shorter inputs.")
    case 5:
      print("Be advised: >30 min to compute.")
    case 6:
      print("Be advised: >2 hrs to compute.")
    case 7:
      print("Be advised: >5 hrs to compute.")
    case 8:
      print("Be advised: >16 hrs to compute.")
    case 9:
      print("Be advised: >2 days to compute.")
    case 10:
      print("Be advised: >1 week to compute.")

print(main())
