#!/usr/bin/env python3

import argparse
import hashlib
import zlib
from pathlib import Path


def read_git_object(path):
    """Descomprime un objeto Git y devuelve tipo y contenido."""
    data = Path(path).read_bytes()
    raw = zlib.decompress(data)

    header, content = raw.split(b"\x00", 1)
    obj_type, size = header.decode().split(" ", 1)

    if int(size) != len(content):
        raise ValueError("El tamaño del objeto no coincide con su cabecera")

    return obj_type, content


def show_commit(content):
    print("[+] Tipo: commit\n")

    text = content.decode(errors="replace")

    for line in text.splitlines():
        print(line)


def show_tree(content):
    print("[+] Tipo: tree\n")

    offset = 0

    while offset < len(content):
        space = content.index(b" ", offset)
        mode = content[offset:space].decode()

        null = content.index(b"\x00", space)
        name = content[space + 1:null].decode(errors="replace")

        sha = content[null + 1:null + 21].hex()

        print(f"{mode} {sha} {name}")

        offset = null + 21


def show_blob(content):
    print("[+] Tipo: blob\n")
    print(content.decode(errors="replace"))


def main():
    parser = argparse.ArgumentParser(
        description="Analizador genérico de objetos Git comprimidos"
    )

    parser.add_argument(
        "object",
        help="Archivo de objeto Git extraído desde .git/objects"
    )

    args = parser.parse_args()

    obj_type, content = read_git_object(args.object)

    print(f"[+] Archivo: {args.object}")
    print(f"[+] Tipo:    {obj_type}")
    print(f"[+] Tamaño:  {len(content)} bytes\n")

    if obj_type == "commit":
        show_commit(content)

    elif obj_type == "tree":
        show_tree(content)

    elif obj_type == "blob":
        show_blob(content)

    elif obj_type == "tag":
        print(content.decode(errors="replace"))

    else:
        print("[!] Tipo de objeto no reconocido")
        print(content)


if __name__ == "__main__":
    main()
