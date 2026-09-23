# 📚 Arsenii's LeetCode Solutions & Patterns (31 Solved)

Повна особиста база всіх 31 розв'язаних задач, згрупована за класичними темами та патернами (Blind 75 / NeetCode 150).

---

## 📁 Карта задач за темами

### 1. [Arrays & Hashing (11 задач)](./01_arrays_and_hashing/)
* [001_two_sum.py](./01_arrays_and_hashing/001_two_sum.py) — **Two Sum (Easy)**: Хеш-мапа за 1 прохід ($O(n)$).
* [009_palindrome_number.py](./01_arrays_and_hashing/009_palindrome_number.py) — **Palindrome Number (Easy)**: Математичне розгортання числа через `% 10` та `* 10`.
* [013_roman_to_integer.py](./01_arrays_and_hashing/013_roman_to_integer.py) — **Roman to Integer (Easy)**: Базове правило: менша цифра перед більшою віднімається.
* [049_group_anagrams.py](./01_arrays_and_hashing/049_group_anagrams.py) — **Group Anagrams (Medium)**: Хеш-мапа з ключем у вигляді відсортованого слова.
* [128_longest_consecutive_sequence.py](./01_arrays_and_hashing/128_longest_consecutive_sequence.py) — **Longest Consecutive Sequence (Medium)**: Пошук стартів ланцюжків через `set` за $O(n)$.
* [217_contains_duplicate.py](./01_arrays_and_hashing/217_contains_duplicate.py) — **Contains Duplicate (Easy)**: Перевірка через `len(nums) != len(set(nums))`.
* [238_product_of_array_except_self.py](./01_arrays_and_hashing/238_product_of_array_except_self.py) — **Product of Array Except Self (Medium)**: Префіксний та постфіксний добутки без ділення.
* [242_valid_anagram.py](./01_arrays_and_hashing/242_valid_anagram.py) — **Valid Anagram (Easy)**: Підрахунок частоти літер через `Counter`.
* [347_top_k_frequent_elements.py](./01_arrays_and_hashing/347_top_k_frequent_elements.py) — **Top K Frequent Elements (Medium)**: `Counter.most_common(k)`.
* [525_contiguous_array.py](./01_arrays_and_hashing/525_contiguous_array.py) — **Contiguous Array (Medium)**: Трюк `0 -> -1` + Prefix Sum через Hash Map.
* [1929_concatenation_of_array.py](./01_arrays_and_hashing/1929_concatenation_of_array.py) — **Concatenation of Array (Easy)**: Конкатенація списків `nums + nums`.

---

### 2. [Two Pointers (4 задачі)](./02_two_pointers/)
* [015_three_sum.py](./02_two_pointers/015_three_sum.py) — **3Sum (Medium)**: Сортування + рух двох вказівників назустріч ($O(n^2)$).
* [026_remove_duplicates_from_sorted_array.py](./02_two_pointers/026_remove_duplicates_from_sorted_array.py) — **Remove Duplicates from Sorted Array (Easy)**: Швидкий і повільний палець (in-place перезапис).
* [088_merge_sorted_array.py](./02_two_pointers/088_merge_sorted_array.py) — **Merge Sorted Array (Easy)**: Три вказівники з кінця в початок, щоб не затирати корисні числа.
* [125_valid_palindrome.py](./02_two_pointers/125_valid_palindrome.py) — **Valid Palindrome (Easy)**: Зустрічні пальці з ігноруванням пунктуації та пробілів.

---

### 3. [Sliding Window (2 задачі)](./03_sliding_window/)
* [003_longest_substring_without_repeating_characters.py](./03_sliding_window/003_longest_substring_without_repeating_characters.py) — **Longest Substring (Medium)**: Вікно з `set`, де лівий край підтягується при дублікаті.
* [121_best_time_to_buy_and_sell_stock.py](./03_sliding_window/121_best_time_to_buy_and_sell_stock.py) — **Best Time to Buy and Sell Stock (Easy)**: Однопрохідний трекінг мінімальної ціни.

---

### 4. [Stack (1 задача)](./04_stack/)
* [020_valid_parentheses.py](./04_stack/020_valid_parentheses.py) — **Valid Parentheses (Easy)**: Стек відкритих дужок і перевірка закриваючих пар.

---

### 5. [Binary Search (2 задачі)](./05_binary_search/)
* [004_median_of_two_sorted_arrays.py](./05_binary_search/004_median_of_two_sorted_arrays.py) — **Median of Two Sorted Arrays (Hard)**: Бінарний пошук розрізу (partition) по меншому масиву за $O(\log(\min(m, n)))$.
* [704_binary_search.py](./05_binary_search/704_binary_search.py) — **Binary Search (Easy)**: Класичний поділ відрізка навпіл ($O(\log n)$).

---

### 6. [Linked List (4 задачі)](./05_linked_list/)
* [002_add_two_numbers.py](./05_linked_list/002_add_two_numbers.py) — **Add Two Numbers (Medium)**: Додавання в стовпчик з переносом `carry`.
* [021_merge_two_sorted_lists.py](./05_linked_list/021_merge_two_sorted_lists.py) — **Merge Two Sorted Lists (Easy)**: Злиття двох списків через Dummy Head.
* [141_linked_list_cycle.py](./05_linked_list/141_linked_list_cycle.py) — **Linked List Cycle (Easy)**: Алгоритм черепахи і зайця Флойда (Fast & Slow pointers).
* [206_reverse_linked_list.py](./05_linked_list/206_reverse_linked_list.py) — **Reverse Linked List (Easy)**: Розгортання списку через три вказівники: `prev`, `curr`, `nxt`.

---

### 7. [Trees & DFS (5 задач)](./07_trees/)
* [100_same_tree.py](./07_trees/100_same_tree.py) — **Same Tree (Easy)**: Рекурсивне порівняння вузлів двох дерев.
* [104_maximum_depth_of_binary_tree.py](./07_trees/104_maximum_depth_of_binary_tree.py) — **Maximum Depth of Binary Tree (Easy)**: Рекурсивний розрахунок висоти дерева.
* [110_balanced_binary_tree.py](./07_trees/110_balanced_binary_tree.py) — **Balanced Binary Tree (Easy)**: Перевірка різниці висот піддерев $\le 1$.
* [226_invert_binary_tree.py](./07_trees/226_invert_binary_tree.py) — **Invert Binary Tree (Easy)**: Рекурсивне віддзеркалення лівого і правого нащадків.
* [543_diameter_of_binary_tree.py](./07_trees/543_diameter_of_binary_tree.py) — **Diameter of Binary Tree (Easy)**: Максимальний шлях між двома листками через DFS.

---

### 8. [Heap / Priority Queue (2 задачі)](./08_heap_priority_queue/)
* [703_kth_largest_element_in_a_stream.py](./08_heap_priority_queue/703_kth_largest_element_in_a_stream.py) — **Kth Largest in a Stream (Easy)**: Min-Heap фіксованого розміру `k`.
* [1046_last_stone_weight.py](./08_heap_priority_queue/1046_last_stone_weight.py) — **Last Stone Weight (Easy)**: Симуляція гри камінців через Max-Heap (значення з мінусом у heapq).

---

### 9. [Palindromes (1 задача)](./04_palindromes/)
* [005_longest_palindromic_substring.py](./04_palindromes/005_longest_palindromic_substring.py) — **Longest Palindromic Substring (Medium)**: Розширення від центру (Expand Around Center) для парних і непарних довжин.

---

### 10. [Backtracking (1 задача)](./06_backtracking/)
* [017_letter_combinations_of_a_phone_number.py](./06_backtracking/017_letter_combinations_of_a_phone_number.py) — **Letter Combinations of a Phone Number (Medium)**: Ітеративне розширення ("снігова куля") та рекурсивний бектрекінг.

---

## 🚀 Як запускати:
Будь-який файл повністю автономний та містить готові тести:
```bash
python3 05_binary_search/004_median_of_two_sorted_arrays.py
python3 07_trees/226_invert_binary_tree.py
python3 08_heap_priority_queue/1046_last_stone_weight.py
```
