# LeetCode Solutions

Solutions to LeetCode problems organized by topic and pattern.

---

## Problems by Topic

### 1. [Arrays & Hashing](./01_arrays_and_hashing/)
* [Two Sum](./01_arrays_and_hashing/001_two_sum.py) (Easy) - One-pass hash map
* [Palindrome Number](./01_arrays_and_hashing/009_palindrome_number.py) (Easy) - Base-10 digit reversal
* [Roman to Integer](./01_arrays_and_hashing/013_roman_to_integer.py) (Easy) - Subtractive notation
* [Group Anagrams](./01_arrays_and_hashing/049_group_anagrams.py) (Medium) - Hash map with sorted string key
* [Longest Consecutive Sequence](./01_arrays_and_hashing/128_longest_consecutive_sequence.py) (Medium) - Hash set sequence start check
* [Contains Duplicate](./01_arrays_and_hashing/217_contains_duplicate.py) (Easy) - Set length comparison
* [Product of Array Except Self](./01_arrays_and_hashing/238_product_of_array_except_self.py) (Medium) - Prefix and postfix products
* [Valid Anagram](./01_arrays_and_hashing/242_valid_anagram.py) (Easy) - Character count with Counter
* [Top K Frequent Elements](./01_arrays_and_hashing/347_top_k_frequent_elements.py) (Medium) - Frequency count with Counter
* [Contiguous Array](./01_arrays_and_hashing/525_contiguous_array.py) (Medium) - Prefix sum with 0 mapped to -1
* [Concatenation of Array](./01_arrays_and_hashing/1929_concatenation_of_array.py) (Easy) - List concatenation

### 2. [Two Pointers](./02_two_pointers/)
* [3Sum](./02_two_pointers/015_three_sum.py) (Medium) - Sort and two pointers
* [Remove Duplicates from Sorted Array](./02_two_pointers/026_remove_duplicates_from_sorted_array.py) (Easy) - Fast and slow pointers
* [Merge Sorted Array](./02_two_pointers/088_merge_sorted_array.py) (Easy) - Three pointers from the end
* [Valid Palindrome](./02_two_pointers/125_valid_palindrome.py) (Easy) - Two pointers inwards

### 3. [Sliding Window](./03_sliding_window/)
* [Longest Substring Without Repeating Characters](./03_sliding_window/003_longest_substring_without_repeating_characters.py) (Medium) - Sliding window with hash set
* [Best Time to Buy and Sell Stock](./03_sliding_window/121_best_time_to_buy_and_sell_stock.py) (Easy) - One-pass minimum tracking

### 4. [Stack](./04_stack/)
* [Valid Parentheses](./04_stack/020_valid_parentheses.py) (Easy) - Stack matching

### 5. [Binary Search](./05_binary_search/)
* [Median of Two Sorted Arrays](./05_binary_search/004_median_of_two_sorted_arrays.py) (Hard) - Binary search on partition
* [Binary Search](./05_binary_search/704_binary_search.py) (Easy) - Classic binary search

### 6. [Linked List](./05_linked_list/)
* [Add Two Numbers](./05_linked_list/002_add_two_numbers.py) (Medium) - Column addition with carry
* [Merge Two Sorted Lists](./05_linked_list/021_merge_two_sorted_lists.py) (Easy) - Pointer merging with dummy head
* [Linked List Cycle](./05_linked_list/141_linked_list_cycle.py) (Easy) - Floyd's cycle detection
* [Reverse Linked List](./05_linked_list/206_reverse_linked_list.py) (Easy) - Iterative pointer reversal

### 7. [Trees](./07_trees/)
* [Same Tree](./07_trees/100_same_tree.py) (Easy) - Recursive comparison
* [Maximum Depth of Binary Tree](./07_trees/104_maximum_depth_of_binary_tree.py) (Easy) - DFS height
* [Balanced Binary Tree](./07_trees/110_balanced_binary_tree.py) (Easy) - Bottom-up height check
* [Invert Binary Tree](./07_trees/226_invert_binary_tree.py) (Easy) - Recursive swap
* [Diameter of Binary Tree](./07_trees/543_diameter_of_binary_tree.py) (Easy) - DFS max path

### 8. [Heap / Priority Queue](./08_heap_priority_queue/)
* [Kth Largest Element in a Stream](./08_heap_priority_queue/703_kth_largest_element_in_a_stream.py) (Easy) - Min-heap of size k
* [Last Stone Weight](./08_heap_priority_queue/1046_last_stone_weight.py) (Easy) - Max-heap with negated values

### 9. [Palindromes](./04_palindromes/)
* [Longest Palindromic Substring](./04_palindromes/005_longest_palindromic_substring.py) (Medium) - Expand around center

### 10. [Backtracking](./06_backtracking/)
* [Letter Combinations of a Phone Number](./06_backtracking/017_letter_combinations_of_a_phone_number.py) (Medium) - Iterative expansion and recursion

---

## Running Tests

Each file includes test cases and can be run directly:

```bash
python3 01_arrays_and_hashing/001_two_sum.py
```
