def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    counted_words = count_words(file_contents)
    counted_characters = count_characters(file_contents)
    print_report(counted_words, counted_characters, f.name)

def count_words(text):
    return len(text.split())

def count_characters(text):
    chars = {}
    for ch in text:
        ch = ch.lower()
        if ch in chars:
            chars[ch] = chars[ch] + 1
        else:
            chars[ch] = 1
    return chars

def print_report(counted_words, counted_characters, file_name):
    print(f"--- Begin report of {file_name} ---")
    print(f"{counted_words} words found in the document")
    print()

    counted_characters_list = []
    for ch, times in counted_characters.items():
        if ch.isalpha():
            counted_characters_list.append({"character":ch, "times":times})

    counted_characters_list.sort(reverse=True, key=sort_on)
    
    for cur in counted_characters_list:
        ch = cur["character"]
        times = cur["times"]
        print(f"The '{ch}' character was found {times} times")
        
    print("--- End report ---")

def sort_on(dict):
    return dict["times"]

main()
