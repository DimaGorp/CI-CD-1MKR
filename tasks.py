import re
from typing import List, Tuple

def read_file(filename: str) -> str:
    """Функція для зчитування вмісту файлу і повернення тексту."""
    with open(filename, 'r') as file:
        return file.read()

def split_text(text: str) -> Tuple[List[str], List[str]]:
    """Функція для розділення тексту на слова та речення."""
    words = re.findall(r'\b\w+\b', text)
    
    # Розділяємо текст на речення за всіма можливими символами, які можуть завершувати речення
    sentences = re.split(r'(?<=[.!?])\s*', text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

    # Розділяємо кожне речення на слова
    final_sentences = []
    for sentence in sentences:
        final_sentences.append(sentence)
    
    return words, final_sentences

def count_words_and_sentences(words: List[str], sentences: List[str]) -> Tuple[int, int]:
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