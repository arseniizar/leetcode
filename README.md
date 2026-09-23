# 📚 LeetCode Solutions & Patterns

Особиста база розібраних задач, згрупована за фундаментальними алгоритмічними патернами.

---

## 📁 Структура репозиторію

### 1. [Arrays & Hashing (Масиви та Хешування)](./01_arrays_and_hashing/)
* [001_two_sum.py](./01_arrays_and_hashing/001_two_sum.py) — **Two Sum (Easy)**: Пошук пари через словник за 1 прохід ($O(n)$).
* [009_palindrome_number.py](./01_arrays_and_hashing/009_palindrome_number.py) — **Palindrome Number (Easy)**: Математичне розгортання числа через `% 10` та `* 10`.
* [013_roman_to_integer.py](./01_arrays_and_hashing/013_roman_to_integer.py) — **Roman to Integer (Easy)**: Базове правило: менша цифра перед більшою віднімається, інакше додається.
* [128_longest_consecutive_sequence.py](./01_arrays_and_hashing/128_longest_consecutive_sequence.py) — **Longest Consecutive Sequence (Medium)**: Пошук стартів ланцюжків через `set` за $O(n)$ без сортування.
* [525_contiguous_array.py](./01_arrays_and_hashing/525_contiguous_array.py) — **Contiguous Array (Medium)**: Трюк `0 -> -1` + Prefix Sum через Hash Map.
* [1929_concatenation_of_array.py](./01_arrays_and_hashing/1929_concatenation_of_array.py) — **Concatenation of Array (Easy)**: Подвоєння списку `nums + nums` vs виділення фіксованого розміру `[0] * 2n`.

---

### 2. [Two Pointers (Два Вказівники)](./02_two_pointers/)
* [015_three_sum.py](./02_two_pointers/015_three_sum.py) — **3Sum (Medium)**: Сортування + рух двох вказівників назустріч із пропуском дублікатів ($O(n^2)$).
* [026_remove_duplicates_from_sorted_array.py](./02_two_pointers/026_remove_duplicates_from_sorted_array.py) — **Remove Duplicates from Sorted Array (Easy)**: Швидкий і повільний палець (in-place перезапис).
* [088_merge_sorted_array.py](./02_two_pointers/088_merge_sorted_array.py) — **Merge Sorted Array (Easy)**: Три вказівники з кінця в початок (інверсія), щоб не затирати корисні числа.

---

### 3. [Sliding Window (Ковзне Вікно)](./03_sliding_window/)
* [003_longest_substring_without_repeating_characters.py](./03_sliding_window/003_longest_substring_without_repeating_characters.py) — **Longest Substring (Medium)**: Правий край розширює вікно, лівий підтягується при виявленні дубліката в `set`.
* [121_best_time_to_buy_and_sell_stock.py](./03_sliding_window/121_best_time_to_buy_and_sell_stock.py) — **Best Time to Buy and Sell Stock (Easy)**: Однопрохідний трекінг мінімальної ціни минулого дня.

---

### 4. [Palindromes (Паліндроми)](./04_palindromes/)
* [005_longest_palindromic_substring.py](./04_palindromes/005_longest_palindromic_substring.py) — **Longest Palindromic Substring (Medium)**: Чому не Sliding Window; розширення від центру для парних і непарних довжин ($O(n^2)$).

---

### 5. [Linked List (Зв'язані Списки)](./05_linked_list/)
* [002_add_two_numbers.py](./05_linked_list/002_add_two_numbers.py) — **Add Two Numbers (Medium)**: Додавання в стовпчик з переносом `carry`, патерн Dummy Head.

---

### 6. [Backtracking / Combinations](./06_backtracking/)
* [017_letter_combinations_of_a_phone_number.py](./06_backtracking/017_letter_combinations_of_a_phone_number.py) — **Letter Combinations of a Phone Number (Medium)**: Ітеративне множення комбінацій ("снігова куля") та рекурсивний Backtracking.

---

## 🚀 Як запускати тести:
Будь-який файл можна запустити напряму через термінал:
```bash
python3 01_arrays_and_hashing/001_two_sum.py
python3 02_two_pointers/015_three_sum.py
python3 03_sliding_window/003_longest_substring_without_repeating_characters.py
```
Кожен файл має вбудований блок `if __name__ == "__main__":` з тестовими кейсами та перевірками!
