from stellar_sdk import Network, Signer, Server, TransactionBuilder
from stellar_sdk.exceptions import *
from globals import *

disclaimer = """
Use this script to revoke master keypair access while adding high threshold signers.

You need to fund the master account before running this script via create_account_op.
You must send enough to cover reserves for all new signers, presently 0.5 XLM each.

Default configuration sets all new signers to weight 1 and account weights to 0/0/0.

THIS SCRIPT WILL SUBMIT A LIVE SIGNED TRANSACTION TO THE PUBLIC STELLAR NETWORK
THAT WILL DISABLE ACCOUNT ACCESS FROM THE GIVEN MASTER KEYPAIR UPON SUCCESS.

DISCLAIMER:
This script can modify the configuration of your Stellar account,
including adding signers to your account. 

If you provide incorrect public keys or public keys you do not control,
you may lose access to your account and funds permanently.
Only use this script if you fully understand its consequences and
are certain about the public keys you're adding as signers.

The author of this script and the platform providing it take no responsibility
for any loss or damage that may arise from the use of this script.
Use it at your own risk and only on accounts you control and have properly verified.

Before running this script, make sure you have backed up the secret keys of any and all
new signers for the master account and understand the potential outcomes.
See https://developers.stellar.org/docs/encyclopedia/signatures-multisig.

If you have any doubts or concerns, do not proceed with running this script.
"""
server = Server("https://horizon.stellar.org")

def main():
  if getINPUT(f"{disclaimer}\nDo you agree with the terms? (Y/n): ") != "Y":
    sys.exit("User cancelled.")
  secretKey = getINPUT("Enter vanity account secret key: ")
  try:
    masterKeypair = Keypair.from_secret(secretKey)
  except Ed25519SecretSeedInvalidError:
    sys.exit("Try a valid secret key.")
  try:
    masterAccount = server.load_account(masterKeypair.public_key)
  except NotFoundError:
    sys.exit("Try funding the account.")
  
  numSigners = getINPUT(f"Replace master keypair with how many signers? ")
  if not (numSigners.isdigit() and int(numSigners)):
    sys.exit("Try a valid number of signers.")
  signerPKs = []
  for n in range(0, int(numSigners)):
    signerPKs.append(getINPUT(f"Enter signer public key #{n+1}: "))
  firstSigner = signerPKs[0]
  remainingSigners = signerPKs[1:] if len(signerPKs) != 1 else []
  inputValidation = {firstSigner}
  for PKs in remainingSigners:
    if PKs in inputValidation:
      sys.exit("Try using unique signers.")
    inputValidation.add(PKs)
  transaction = TransactionBuilder(
    masterAccount,
    network_passphrase = Network.PUBLIC_NETWORK_PASSPHRASE,
    base_fee = server.fetch_base_fee() * 5
  ).append_set_options_op(
    master_weight = 0,
    low_threshold = 0,
    med_threshold = 0,
    high_threshold = 0,
    signer = getSigner(firstSigner)
  )
  for PKs in remainingSigners:
    transaction.append_set_options_op(
      signer = getSigner(PKs)
    )
  transaction = (
    transaction
    .add_text_memo("Update signers 🔐")
    .set_timeout(3600)
    .build()
  )
  transaction.sign(masterKeypair)
  if getINPUT("Would you like to review the transaction? (Y/n): ") == "Y":
    print(f"\nTransaction XDR:\n{transaction.to_xdr()}\n\nReview at https://laboratory.stellar.org/#xdr-viewer\n")
  if "Y" != getINPUT(f"Submit transaction? (Y/n): "):
    sys.exit("User cancelled.")
  try:
    response = server.submit_transaction(transaction)
    print(response)
  except Exception as e:
    print(str(e))

def getSigner(PK):
  try:
    return Signer.ed25519_public_key(
      account_id = PK,
      weight = 1
    )
  except Ed25519PublicKeyInvalidError:
    sys.exit("Try a valid public key")

main()
