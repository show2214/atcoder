import re

if __name__ == "__main__":
    target = input()
    result = re.fullmatch(r"(eraser|dreamer|erase|dream)+", target)
    print("YES" if result else "NO")
