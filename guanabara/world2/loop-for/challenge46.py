from time import sleep

for c in range(10, -1, -1):
    print("\r" + " " * 30, end="")  # limpa a linha
    print(f"\rCountdown: {c:2d}", end="", flush=True)
    for _ in range(3):
        sleep(0.3)
        print('.', end="", flush=True)
    sleep(0.5)

print("\r" + " " * 30, end="")  # limpa antes do boom
print("\r💥 BOOM!!! 🎆🎇")
