# Vanity Stellar Public Key Generator

This repository contains a Python script named `XLMgenerateVanityPublicKey.py` that generates a vanity Stellar public key. The script inserts a given vanity phrase into a random Stellar public key and tries different checksum digits to form a valid public key.

## Requirements

- Python 3.x
- `stellar_sdk` library (install using `pip install stellar_sdk`)

## Usage

1. Run the script by executing the following command:

```bash
python3 XLMgenerateVanityPublicKey.py
```

2. Type your desired phrase and press Enter.

3. View the result.

## Disclaimer

This script is for demonstration purposes only. Generating vanity public keys and using them for real-world applications can have security implications. Always exercise caution and follow best practices when working with cryptographic keys. The script focuses solely on finding a valid public key with the given phrase and does not retrieve or handle the corresponding private key. Use the generated vanity public key responsibly and avoid using it in production or sensitive environments.
