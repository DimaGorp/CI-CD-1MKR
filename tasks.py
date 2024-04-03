import re
def read_file(filename):
    """Функція для зчитування вмісту файлу і повернення тексту."""
    with open(filename, 'r') as file:
        return file.read()

def main():
    filename = "index.txt"  # Шлях до файлу
    text = read_file(filename)
    print(text)

if __name__ == "__main__":
    main()
