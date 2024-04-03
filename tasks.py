import re

def read_file(filename):
    """Функція для зчитування вмісту файлу і повернення тексту."""
    with open(filename, 'r') as file:
        return file.read()

def split_text(text):
    """Функція для розділення тексту на слова та речення."""
    words = re.findall(r'\b\w+\b', text)
    sentences = re.split(r'[.!?]+', text)
    sentences = [sentence for sentence in sentences if sentence.strip()]
    return words, sentences

def count_words_and_sentences(words, sentences):
    """Функція для підрахунку кількості слів та речень."""
    return len(words), len(sentences)

def main():
    filename = "index.txt"  # Шлях до файлу
    text = read_file(filename)
    words, sentences = split_text(text)
    word_count, sentence_count = count_words_and_sentences(words, sentences)
    print("Кількість слів у файлі:", word_count)
    print("Кількість речень у файлі:", sentence_count)

if __name__ == "__main__":
    main()
