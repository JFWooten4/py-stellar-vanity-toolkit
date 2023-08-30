# Vanity Stellar Address Toolbox

## Requirements

- Python 3.x
- `stellar_sdk` library

## Usage

1. Run the script by executing the following command:

```bash
python3 generateVanity{DesiredType}.py
```

2. Enter your desired inputs.

3. View the result.

## Disclaimer

This script is for demonstration purposes only. Generating vanity public keys and using them for real-world applications can have security implications. Always exercise caution and follow best practices when working with cryptographic keys. The script focuses solely on finding valid keys for given vanity phrases. Use vanity keys responsibly and avoid them in production or sensitive environments. 

It is highly recommended that you add other non-vanity hardware signers on Stellar. Then set the master weight of any vanity accounts generated to zero. An example of how to do this is provided in `configureVanitySigners.py` and is provided without amy warrenty or representations.
