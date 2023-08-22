import time

# print(f"a")
# time.sleep(0.5)

# print(f"\033[Fb")
# time.sleep(0.5)

# print(f"\033[Fc")
# time.sleep(0.5)

# print(f"d\033[F")
# time.sleep(0.5)

def overwrite_previous(string, s2="meow?"):
    time.sleep(0.5)
    print("\033[A\033[F")
    print(f"{string}")
    print(f"{s2}")

print('a\na')
overwrite_previous('b')
overwrite_previous('c', '::')
overwrite_previous('d', ':3')