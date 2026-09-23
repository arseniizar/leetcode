# 📚 LeetCode Solutions & Patterns (31 Solved)

A curated collection of LeetCode problems categorized by fundamental algorithmic patterns.

---

## 📁 Problem Index by Pattern

### 1. [Arrays & Hashing (11 problems)](./01_arrays_and_hashing/)
* [001_two_sum.py](./01_arrays_and_hashing/001_two_sum.py) — **Two Sum (Easy)**: One-pass Hash Map lookup ($O(n)$ time, $O(n)$ space).
* [009_palindrome_number.py](./01_arrays_and_hashing/009_palindrome_number.py) — **Palindrome Number (Easy)**: Base-10 mathematical reversal via `% 10` and `* 10` ($O(\log n)$ time, $O(1)$ space).
* [013_roman_to_integer.py](./01_arrays_and_hashing/013_roman_to_integer.py) — **Roman to Integer (Easy)**: Subtractive rule: smaller numeral before a larger one subtracts ($O(n)$ time, $O(1)$ space).
* [049_group_anagrams.py](./01_arrays_and_hashing/049_group_anagrams.py) — **Group Anagrams (Medium)**: Hash Map with sorted string as key ($O(n \cdot k \log k)$ time).
* [128_longest_consecutive_sequence.py](./01_arrays_and_hashing/128_longest_consecutive_sequence.py) — **Longest Consecutive Sequence (Medium)**: Sequence start detection via Hash Set ($O(n)$ time without sorting).
* [217_contains_duplicate.py](./01_arrays_and_hashing/217_contains_duplicate.py) — **Contains Duplicate (Easy)**: Set length comparison ($O(n)$ time, $O(n)$ space).
* [238_product_of_array_except_self.py](./01_arrays_and_hashing/238_product_of_array_except_self.py) — **Product of Array Except Self (Medium)**: Prefix and postfix running products without division ($O(n)$ time, $O(1)$ extra space).
* [242_valid_anagram.py](./01_arrays_and_hashing/242_valid_anagram.py) — **Valid Anagram (Easy)**: Frequency counting via `Counter` ($O(n)$ time, $O(1)$ space).
* [347_top_k_frequent_elements.py](./01_arrays_and_hashing/347_top_k_frequent_elements.py) — **Top K Frequent Elements (Medium)**: Frequency map and `Counter.most_common(k)` ($O(n \log k)$ time).
* [525_contiguous_array.py](./01_arrays_and_hashing/525_contiguous_array.py) — **Contiguous Array (Medium)**: `0 -> -1` transformation + Prefix Sum via Hash Map ($O(n)$ time, $O(n)$ space).
* [1929_concatenation_of_array.py](./01_arrays_and_hashing/1929_concatenation_of_array.py) — **Concatenation of Array (Easy)**: Python list duplication `nums + nums` ($O(n)$ time, $O(n)$ space).

---

### 2. [Two Pointers (4 problems)](./02_two_pointers/)
* [015_three_sum.py](./02_two_pointers/015_three_sum.py) — **3Sum (Medium)**: Sorting + two converging pointers with duplicate skipping ($O(n^2)$ time, $O(1)$ space).
* [026_remove_duplicates_from_sorted_array.py](./02_two_pointers/026_remove_duplicates_from_sorted_array.py) — **Remove Duplicates from Sorted Array (Easy)**: Fast & slow pointer in-place overwrite ($O(n)$ time, $O(1)$ space).
* [088_merge_sorted_array.py](./02_two_pointers/088_merge_sorted_array.py) — **Merge Sorted Array (Easy)**: Three pointers filling from the back to preserve unmerged elements ($O(m + n)$ time, $O(1)$ space).
* [125_valid_palindrome.py](./02_two_pointers/125_valid_palindrome.py) — **Valid Palindrome (Easy)**: Two pointers moving inwards skipping non-alphanumeric characters ($O(n)$ time, $O(1)$ space).

---

### 3. [Sliding Window (2 problems)](./03_sliding_window/)
* [003_longest_substring_without_repeating_characters.py](./03_sliding_window/003_longest_substring_without_repeating_characters.py) — **Longest Substring (Medium)**: Dynamic window with a Hash Set ($O(n)$ time, $O(m)$ space).
* [121_best_time_to_buy_and_sell_stock.py](./03_sliding_window/121_best_time_to_buy_and_sell_stock.py) — **Best Time to Buy and Sell Stock (Easy)**: One-pass running minimum tracking ($O(n)$ time, $O(1)$ space).

---

### 4. [Stack (1 problem)](./04_stack/)
* [020_valid_parentheses.py](./04_stack/020_valid_parentheses.py) — **Valid Parentheses (Easy)**: LIFO stack matching closing to opening brackets ($O(n)$ time, $O(n)$ space).

---

### 5. [Binary Search (2 problems)](./05_binary_search/)
* [004_median_of_two_sorted_arrays.py](./05_binary_search/004_median_of_two_sorted_arrays.py) — **Median of Two Sorted Arrays (Hard)**: Binary search on partition point of the smaller array ($O(\log(\min(m, n)))$ time, $O(1)$ space).
* [704_binary_search.py](./05_binary_search/704_binary_search.py) — **Binary Search (Easy)**: Classic interval halving on sorted array ($O(\log n)$ time, $O(1)$ space).

---

### 6. [Linked List (4 problems)](./05_linked_list/)
* [002_add_two_numbers.py](./05_linked_list/002_add_two_numbers.py) — **Add Two Numbers (Medium)**: Column addition with carry tracking and a Dummy Head ($O(\max(m, n))$ time, $O(\max(m, n))$ space).
* [021_merge_two_sorted_lists.py](./05_linked_list/021_merge_two_sorted_lists.py) — **Merge Two Sorted Lists (Easy)**: In-place pointer rewiring with a Dummy Head ($O(n + m)$ time, $O(1)$ space).
* [141_linked_list_cycle.py](./05_linked_list/141_linked_list_cycle.py) — **Linked List Cycle (Easy)**: Floyd's Tortoise and Hare (Fast & Slow pointers) ($O(n)$ time, $O(1)$ space).
* [206_reverse_linked_list.py](./05_linked_list/206_reverse_linked_list.py) — **Reverse Linked List (Easy)**: Iterative three-pointer reversal (`prev`, `curr`, `nxt`) ($O(n)$ time, $O(1)$ space).

---

### 7. [Trees & DFS (5 problems)](./07_trees/)
* [100_same_tree.py](./07_trees/100_same_tree.py) — **Same Tree (Easy)**: Recursive node comparison ($O(n)$ time, $O(h)$ space).
* [104_maximum_depth_of_binary_tree.py](./07_trees/104_maximum_depth_of_binary_tree.py) — **Maximum Depth of Binary Tree (Easy)**: Recursive tree height `1 + max(L, R)` ($O(n)$ time, $O(h)$ space).
* [110_balanced_binary_tree.py](./07_trees/110_balanced_binary_tree.py) — **Balanced Binary Tree (Easy)**: Bottom-up height check with early exit on height difference > 1 ($O(n)$ time, $O(h)$ space).
* [226_invert_binary_tree.py](./07_trees/226_invert_binary_tree.py) — **Invert Binary Tree (Easy)**: Recursive left-right child pointer swap ($O(n)$ time, $O(h)$ space).
* [543_diameter_of_binary_tree.py](./07_trees/543_diameter_of_binary_tree.py) — **Diameter of Binary Tree (Easy)**: Bottom-up DFS tracking max `left_height + right_height` ($O(n)$ time, $O(h)$ space).

---

### 8. [Heap / Priority Queue (2 problems)](./08_heap_priority_queue/)
* [703_kth_largest_element_in_a_stream.py](./08_heap_priority_queue/703_kth_largest_element_in_a_stream.py) — **Kth Largest in a Stream (Easy)**: Fixed-size Min-Heap of size `k` ($O(n \log k)$ time, $O(k)$ space).
* [1046_last_stone_weight.py](./08_heap_priority_queue/1046_last_stone_weight.py) — **Last Stone Weight (Easy)**: Max-Heap simulation using negated values with `heapq` ($O(n \log n)$ time, $O(n)$ space).

---

### 9. [Palindromes (1 problem)](./04_palindromes/)
* [005_longest_palindromic_substring.py](./04_palindromes/005_longest_palindromic_substring.py) — **Longest Palindromic Substring (Medium)**: Expand around center for both odd and even length palindromes ($O(n^2)$ time, $O(1)$ space).

---

### 10. [Backtracking (1 problem)](./06_backtracking/)
* [017_letter_combinations_of_a_phone_number.py](./06_backtracking/017_letter_combinations_of_a_phone_number.py) — **Letter Combinations of a Phone Number (Medium)**: Iterative Cartesian product expansion and recursive backtracking ($O(4^n \cdot n)$ time and space).

---

## 🚀 How to Run Tests
Every single Python file is standalone and contains built-in test cases:
```bash
python3 01_arrays_and_hashing/001_two_sum.py
python3 02_two_pointers/015_three_sum.py
python3 05_binary_search/004_median_of_two_sorted_arrays.py
```
