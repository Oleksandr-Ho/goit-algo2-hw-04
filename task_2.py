from trie import Trie, TrieNode

class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        """
        Знаходить найдовший спільний префікс для всіх слів із масиву strings.

        Параметри:
            strings (list): масив рядків.
        
        Повертає:
            str: найдовший спільний префікс. Якщо масив порожній або спільного префікса немає, повертається пустий рядок.
        
        Викидає:
            TypeError: якщо strings не є списком або хоча б один елемент не є рядком.
        """
        if not isinstance(strings, list):
            raise TypeError("Input must be a list of strings")
        for s in strings:
            if not isinstance(s, str):
                raise TypeError("All elements in the input list must be strings")
        if not strings:
            return ""

        # Очищуємо Trie, якщо в екземплярі вже є дані.
        self.root = TrieNode()
        self.size = 0

        # Вставляємо всі слова у Trie.
        for word in strings:
            self.put(word)

        # Обчислюємо найдовший спільний префікс за алгоритмом:
        # Рухаємось від кореня вниз, допоки вузол має рівно одного нащадка і не є кінцем якогось слова.
        prefix = ""
        current = self.root
        while len(current.children) == 1 and current.value is None:
            char, next_node = next(iter(current.children.items()))
            prefix += char
            current = next_node
        return prefix


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl", f"Expected 'fl', got {trie.find_longest_common_word(strings)}"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters", f"Expected 'inters', got {trie.find_longest_common_word(strings)}"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == "", f"Expected '', got {trie.find_longest_common_word(strings)}"

    # Перевірка обробки порожнього масиву
    trie = LongestCommonWord()
    assert trie.find_longest_common_word([]) == "", "Expected empty string for empty input"

    print("All tests passed.")
