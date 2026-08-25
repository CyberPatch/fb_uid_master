#!/usr/bin/env python3
import random
import os
import math

# ─────────────────────────────────────────
#   ANSI COLORS
# ─────────────────────────────────────────
R     = "\033[91m"
G     = "\033[92m"
Y     = "\033[93m"
C     = "\033[96m"
M     = "\033[95m"
B     = "\033[94m"
W     = "\033[97m"
DIM   = "\033[2m"
RESET = "\033[0m"

WHATSAPP = "https://wa.me/9779762181892"

def clear():
    os.system('clear')

def banner():
    print(f"{C}{'═' * 45}{RESET}")
    print(f"{Y}  ███████╗██████╗     ██╗   ██╗██╗██████╗ {RESET}")
    print(f"{Y}  ██╔════╝██╔══██╗    ██║   ██║██║██╔══██╗{RESET}")
    print(f"{Y}  █████╗  ██████╔╝    ██║   ██║██║██║  ██║{RESET}")
    print(f"{Y}  ██╔══╝  ██╔══██╗    ██║   ██║██║██║  ██║{RESET}")
    print(f"{Y}  ██║     ██████╔╝    ╚██████╔╝██║██████╔╝{RESET}")
    print(f"{Y}  ╚═╝     ╚═════╝      ╚═════╝ ╚═╝╚═════╝ {RESET}")
    print(f"{M}        FB UID MASTER TOOL v1.0{RESET}")
    print(f"{W}   Mix • Separate • Divide • Clean{RESET}")
    print(f"{C}{'─' * 45}{RESET}")
    print(f"{R}        Owner : Anonymous 😈{RESET}")
    print(f"{G}        🇳🇵 Nepal{RESET}")
    print(f"{C}{'═' * 45}{RESET}")

def success(msg):
    print(f"{G}  ✓ {msg}{RESET}")

def error(msg):
    print(f"{R}  ✗ {msg}{RESET}")

def info(msg):
    print(f"{C}  ➜ {msg}{RESET}")

def warn(msg):
    print(f"{Y}  ⚠ {msg}{RESET}")

def divider():
    print(f"{DIM}{'─' * 45}{RESET}")

# ─────────────────────────────────────────
#   FILE HELPERS
# ─────────────────────────────────────────
def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
        return lines
    except FileNotFoundError:
        error(f"File '{filename}' not found!")
        return None

def write_file(filename, lines):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    success(f"'{filename}' → {Y}{len(lines)}{RESET} entries saved!")

def get_filename(prompt):
    while True:
        name = input(f"{W}{prompt}{RESET}").strip()
        if name:
            if not name.endswith('.txt'):
                name += '.txt'
            return name
        error("File name cannot be empty! Please try again.")

def get_existing_file(prompt):
    while True:
        name = get_filename(prompt)
        lines = read_file(name)
        if lines is not None:
            return name, lines
        warn("Please enter a valid file name.")

def get_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            val = int(input(f"{W}{prompt}{RESET}").strip())
            if min_val is not None and val < min_val:
                error(f"Minimum value is {min_val}! Please try again.")
            elif max_val is not None and val > max_val:
                error(f"Maximum value is {max_val}! Please try again.")
            else:
                return val
        except ValueError:
            error("Numbers only! Please try again.")

def get_choice(prompt, valid):
    while True:
        ch = input(f"{W}{prompt}{RESET}").strip()
        if ch in valid:
            return ch
        error(f"Enter only {'/'.join(valid)}! Please try again.")

# ─────────────────────────────────────────
#   MODE 1 — MIX
# ─────────────────────────────────────────
def mode_mix():
    print(f"\n{M}[ 🔀 MIX MODE ]{RESET}")
    divider()

    filename, lines = get_existing_file("Enter your file name: ")
    info(f"File loaded: {Y}{len(lines)}{RESET} entries")

    print()
    info("Shuffling randomly...")
    random.shuffle(lines)
    write_file(filename, lines)
    success(f"File '{filename}' has been mixed successfully!")

# ─────────────────────────────────────────
#   MODE 2 — SEPARATE SERIES
# ─────────────────────────────────────────
def mode_separate():
    print(f"\n{M}[ ✂️  SEPARATE SERIES MODE ]{RESET}")
    divider()

    filename, lines = get_existing_file("Enter your file name: ")

    series_1000, series_615, other = [], [], []
    for line in lines:
        uid = line.split('|')[0].strip()
        if uid.startswith('1000'):
            series_1000.append(line)
        elif uid.startswith('615'):
            series_615.append(line)
        else:
            other.append(line)

    print()
    info(f"1000xxx series : {Y}{len(series_1000)}{RESET} entries")
    info(f"615xxx  series : {Y}{len(series_615)}{RESET} entries")
    if other:
        info(f"Other series   : {Y}{len(other)}{RESET} entries")
    divider()

    # ── 1000 series ──
    if series_1000:
        print(f"\n{C}[ 1000xxx Series ]{RESET}")
        print(f"  {W}1.{RESET} Keep in original file")
        print(f"  {W}2.{RESET} Save to a new file")
        ch = get_choice("Your choice (1/2): ", ['1', '2'])
        if ch == '2':
            name = get_filename("Enter new file name for 1000xxx series: ")
            random.shuffle(series_1000)
            write_file(name, series_1000)
        else:
            info("1000xxx series will stay in the original file.")
    else:
        warn("No 1000xxx series entries found.")

    # ── 615 series ──
    if series_615:
        print(f"\n{C}[ 615xxx Series ]{RESET}")
        name = get_filename("Enter new file name for 615xxx series: ")
        random.shuffle(series_615)
        write_file(name, series_615)
    else:
        warn("No 615xxx series entries found.")

    # ── Other ──
    if other:
        print(f"\n{C}[ Other Series ]{RESET}")
        print(f"  {W}1.{RESET} Keep in original file")
        print(f"  {W}2.{RESET} Save to a new file")
        ch = get_choice("Your choice (1/2): ", ['1', '2'])
        if ch == '2':
            name = get_filename("Enter new file name for other series: ")
            random.shuffle(other)
            write_file(name, other)

    # ── Original file ──
    print(f"\n{C}[ Original File ]{RESET}")
    print(f"  {W}1.{RESET} Keep unchanged")
    print(f"  {W}2.{RESET} Delete")
    ch = get_choice("Your choice (1/2): ", ['1', '2'])
    if ch == '2':
        os.remove(filename)
        success(f"'{filename}' has been deleted.")
    else:
        success(f"'{filename}' is safe and unchanged.")

# ─────────────────────────────────────────
#   MODE 3 — DIVIDE
# ─────────────────────────────────────────
def mode_divide():
    print(f"\n{M}[ 📂 DIVIDE MODE ]{RESET}")
    divider()

    filename, lines = get_existing_file("Enter your file name: ")
    base  = filename.replace('.txt', '')
    total = len(lines)
    info(f"File loaded: {Y}{total}{RESET} entries")

    print()
    parts = get_int("How many parts to divide into? : ", min_val=2, max_val=total)
    size  = math.ceil(total / parts)

    print()
    info(f"Total entries  : {Y}{total}{RESET}")
    info(f"Total parts    : {Y}{parts}{RESET}")
    info(f"Lines per part : {Y}~{size}{RESET}")
    divider()
    print()

    for i in range(parts):
        start = i * size
        end   = min(start + size, total)
        chunk = lines[start:end]
        if not chunk:
            break
        out_name = f"{base}{i+1}.txt"
        write_file(out_name, chunk)

    print()
    success(f"{parts} files created successfully!")
    success(f"Original file '{filename}' is unchanged ✓")

# ─────────────────────────────────────────
#   MODE 4 — DUPLICATE REMOVE
# ─────────────────────────────────────────
def mode_dedup():
    print(f"\n{M}[ 🧹 DUPLICATE REMOVE MODE ]{RESET}")
    divider()

    filename, lines = get_existing_file("Enter your file name: ")
    info(f"File loaded: {Y}{len(lines)}{RESET} entries")

    seen      = set()
    unique    = []
    dup_count = 0

    for line in lines:
        uid = line.split('|')[0].strip()
        if uid not in seen:
            seen.add(uid)
            unique.append(line)
        else:
            dup_count += 1

    print()
    info(f"Total entries     : {Y}{len(lines)}{RESET}")
    info(f"Duplicates found  : {R}{dup_count}{RESET}")
    info(f"Unique entries    : {G}{len(unique)}{RESET}")
    divider()

    print(f"\n{C}[ Save Options ]{RESET}")
    print(f"  {W}1.{RESET} Overwrite original file")
    print(f"  {W}2.{RESET} Save to a new file")
    ch = get_choice("Your choice (1/2): ", ['1', '2'])

    if ch == '1':
        write_file(filename, unique)
    else:
        name = get_filename("Enter new file name: ")
        write_file(name, unique)

# ─────────────────────────────────────────
#   MODE 5 — CONTACT OWNER
# ─────────────────────────────────────────
def mode_contact():
    print(f"\n{M}[ 📞 CONTACT OWNER ]{RESET}")
    divider()
    print()
    print(f"  {Y}Owner   : {W}Anonymous 😈{RESET}")
    print(f"  {Y}Country : {W}🇳🇵 Nepal{RESET}")
    print(f"  {Y}WhatsApp: {G}{WHATSAPP}{RESET}")
    print()
    print(f"  {DIM}Open the link above in your browser{RESET}")
    print(f"  {DIM}or copy and paste it in WhatsApp.{RESET}")
    print()
    divider()

# ─────────────────────────────────────────
#   MAIN MENU
# ─────────────────────────────────────────
def main():
    while True:
        clear()
        banner()
        print()
        print(f"  {G}1.{RESET} 🔀  Mix File (Randomly Shuffle)")
        print(f"  {B}2.{RESET} ✂️   Separate Series (1000xxx / 615xxx)")
        print(f"  {Y}3.{RESET} 📂  Divide File (Equal Parts)")
        print(f"  {M}4.{RESET} 🧹  Remove Duplicates (UID based)")
        print(f"  {C}5.{RESET} 📞  Contact Owner")
        print(f"  {R}6.{RESET} 🚪  Exit")
        print()
        print(f"{C}{'═' * 45}{RESET}")

        ch = get_choice("Choose an option (1-6): ", ['1', '2', '3', '4', '5', '6'])

        if ch == '1':
            mode_mix()
        elif ch == '2':
            mode_separate()
        elif ch == '3':
            mode_divide()
        elif ch == '4':
            mode_dedup()
        elif ch == '5':
            mode_contact()
        elif ch == '6':
            clear()
            print(f"\n{G}  Goodbye! Exiting tool... 👋{RESET}")
            print(f"{R}  Anonymous 😈 | 🇳🇵 Nepal{RESET}\n")
            break

        print()
        print(f"{C}{'═' * 45}{RESET}")
        input(f"{DIM}  Press Enter to go back to menu...{RESET}")

if __name__ == "__main__":
    main()
