from globals import *

def main():
  try:
    prefix = getINPUT("Enter the desired prefix: ")
    firstChar = prefix[0] if prefix else ""
    if firstChar not in ["", "A", "B", "C", "D"]:
      sys.exit("Try a prefix starting with A/B/C/D.")
    suffix = getINPUT("Enter the desired suffix: ")
    if any(chars not in BASE_32_ALPHABET for chars in prefix + suffix):
      sys.exit("Try base32 inputs.")
    prefixLen = len(prefix)
    suffixLen = len(suffix)
    getSearchTime(prefixLen + suffixLen)
    searchingMoreForPrefix = prefixLen > suffixLen
    prefix = f"G{prefix}"
    n = 0
    startTime = time.time()
    while True:
      if not n % 3200:
        showSearching(startTime)
      n += 1
      keypair = Keypair.random()
      PK = keypair.public_key
      prefixMatch = PK.startswith(prefix)
      suffixMatch = PK.endswith(suffix)
      if prefixMatch and suffixMatch:
        result = f"""\n
        \tKeypair found in {n} attempts:
        \tPublic Key: {PK}
        \tSecret Key: {keypair.secret}\n
        """
        sys.exit(result)
      if(
        (prefixMatch and searchingMoreForPrefix) or
        (suffixMatch and not searchingMoreForPrefix)
      ):
        partialMatch = [
          "\r  Found partial match:             ",
          f"\n  - Public Key: {PK}",
          f"\n  - Secret Key: {keypair.secret}\n"
        ]
        sys.stdout.write("".join(partialMatch))
  except KeyboardInterrupt:
    sys.exit("\nUser ended keypair search.")

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
