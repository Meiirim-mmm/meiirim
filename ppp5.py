if __name__ == "__main__":
    print_words = input("Ведите первую строку: ").lower()
    print_words2 = input("Ведите вторую строку: ").lower()
    print_words3 = input("Ведите третью строку: ").lower()

    print_words = print_words.replace(print_words2, print_words3)

    print(print_words)