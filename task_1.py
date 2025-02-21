from trie import Trie, TrieNode

class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        """
        Рахує кількість слів, що закінчуються на заданий шаблон.
        Якщо pattern не є рядком – викликається TypeError.
        """
        if not isinstance(pattern, str):
            raise TypeError(
                f"Illegal argument for count_words_with_suffix: pattern = {pattern} must be a string"
            )
        count = 0

        def dfs(node, path):
            nonlocal count
            if node.value is not None:
                word = "".join(path)
                if word.endswith(pattern):
                    count += 1
            for char, child in node.children.items():
                path.append(char)
                dfs(child, path)
                path.pop()

        dfs(self.root, [])
        return count

    def has_prefix(self, prefix) -> bool:
        """
        Перевіряє, чи існує хоча б одне слово, що починається з даного префікса.
        Якщо prefix не є рядком – викликається TypeError.
        """
        if not isinstance(prefix, str):
            raise TypeError(
                f"Illegal argument for has_prefix: prefix = {prefix} must be a string"
            )
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]

        # Рекурсивно перевіряємо наявність слова в піддереві; зупинка при першій знахідці що покращує роботу з великими даними !.
        def dfs(node):
            if node.value is not None:
                return True
            for child in node.children.values():
                if dfs(child):
                    return True
            return False

        return dfs(current)


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1       # "apple"
    assert trie.count_words_with_suffix("ion") == 1     # "application"
    assert trie.count_words_with_suffix("a") == 1       # "banana"
    assert trie.count_words_with_suffix("at") == 1      # "cat"

    # Перевірка наявності префікса
    assert trie.has_prefix("app") is True     # "apple", "application"
    assert trie.has_prefix("bat") is False
    assert trie.has_prefix("ban") is True     # "banana"
    assert trie.has_prefix("ca") is True      # "cat"

    print("All tests passed.")
