import re

if __name__ == "__main__":
    S = input()

    regex_pattern = r'(?<=[qwrtypsdfghjklzxcvbnm])[AEIOUaeiou]{2,}(?=[qwrtypsdfghjklzxcvbnm])'

    string_match = re.findall(regex_pattern, S)

    print("\n".join(string_match) if string_match else "-1")
