# Coding Questions - Tier 1

This repository contains solutions to various fundamental coding problems I have solved today. Below is a summary of each problem, the core concepts used, and the approach taken to solve them.

## 📝 Problem Summaries

### 1. [Binary To Decimal](./Tier_1/BinaryToDecimal.java)
- **Concept:** Numeral System Conversion
- **Approach:** Iterates through the given binary string character by character. For each character, the decimal value is updated by multiplying the running total by `2` and adding the integer value of the current binary character (`char - '0'`).

### 2. [Decimal To Binary](./Tier_1/DecimalToBinary.java)
- **Concept:** Numeral System Conversion
- **Approach:** Uses a `while` loop to repeatedly divide the decimal number by `2`. The remainder (`% 2`) is appended to a `StringBuilder`. Finally, the string builder is reversed to yield the correct binary string representation.

### 3. [Fibonacci Series](./Tier_1/FibonacciSeries.java)
- **Concept:** Fibonacci Sequence (Iterative)
- **Approach:** Prints the first $N$ terms of the Fibonacci sequence by tracking just the `firstTerm` and `secondTerm`. The next term is calculated by adding the two variables, updating them iteratively to keep the space complexity to $O(1)$.

### 4. [Nth Fibonacci Term](./Tier_1/NthFibonacciTerm.java)
- **Concept:** Recursion
- **Approach:** Computes the $N$-th Fibonacci term recursively using the recurrence relation `nthFib(n) = nthFib(n-1) + nthFib(n-2)`. A base case correctly returns `1` for values of $n \le 2$.

### 5. [Googly Prime Numbers](./Tier_1/GooglyPrimeNumbers.java)
- **Concept:** Primes & Digit Operations
- **Approach:** A "Googly Prime" is defined here as a number that is prime, and whose sum of digits is also prime. The approach extracts the digits using modulo (`% 10`) and division (`/ 10`) operators. Primality is efficiently checked by testing factors up to $\sqrt{N}$.

### 6. [Palindrome In Range](./Tier_1/PalindromeInRange.java)
- **Concept:** Palindromic Numbers
- **Approach:** Iterates through a specified range of integers. A helper method computes the reverse of the number mathematically (using `% 10` to get the last digit and `* 10` to build the reversed number). If the original and reversed numbers match, it's a palindrome.

### 7. [Roots Of Quadratic Equation](./Tier_1/RootsOfQuadraticEquation.java)
- **Concept:** Algebraic Math (Quadratic Formula)
- **Approach:** Calculates the discriminant ($b^2 - 4ac$). Based on the discriminant, the program branches out to handle real distinct roots, repeated roots, and complex (imaginary) roots. It also elegantly handles numerical stability edge cases and linear edge cases (where $a=0$).

### 8. [Sum Of Divisors](./Tier_1/SumOfDivisors.java)
- **Concept:** Mathematical Factors
- **Approach:** Iterates $i$ from $1$ up to $\sqrt{N}$ to find divisors efficiently. Whenever $N \% i == 0$, it adds both $i$ and $N / i$ to the sum, avoiding counting the square root twice if it is a perfect square. This yields an $O(\sqrt{N})$ time complexity.

### 9. [Sum Of Numbers Divisible By Both 3 And 5](./Tier_1/SumOfNumbersDivisibleByBoth3And5.java)
- **Concept:** Divisibility Rules & LCM
- **Approach:** Iterates from $1$ up to $N$. Instead of checking both `% 3 == 0` and `% 5 == 0`, it optimizes the check to `% 15 == 0` (the Least Common Multiple of $3$ and $5$), accumulating a running sum for matches.

### 10. [Sum Of Primes Less Than N](./Tier_1/SumOfPrimesLessThanN.java)
- **Concept:** Prime Number Aggregation
- **Approach:** Iterates from $1$ to $N-1$ maintaining a running sum. Leverages a helper function that checks if a number is prime in $O(\sqrt{N})$ time.

### 11. [Table](./Tier_1/Table.java)
- **Concept:** Loops & Basic Arithmetic
- **Approach:** Uses a standard `for` loop from $1$ to $10$ to display the multiplication table of a given number $N$, and continuously accumulates the multiples into a `sum` variable to print the total at the end.

### 12. [Count Occurences](./Tier_1/CountOccurences.java)
- **Concept:** Hash Maps & Frequency Counting
- **Approach:** Uses a `HashMap` to iterate over an array of numbers. For each element, it checks if it is already present; if not, it defaults to 0, adding 1 to the occurrence count. Finally, it iterates over the map's entry set to print frequencies.

### 13. [First K Words](./Tier_1/FirstKWords.java)
- **Concept:** String Manipulation & Splitting
- **Approach:** Splits the given string on space `" "` into an array of words. It then loops up to $K$ (or the length of the words array, whichever is smaller) and appends each word into a `StringBuilder` separated by a space.

### 14. [Length Of Last Word](./Tier_1/LengthOfLastWord.java)
- **Concept:** String Traversal (Reverse)
- **Approach:** Trims the input string to remove trailing spaces, then iterates backward from the end of the string. Upon finding the first space character, it extracts the substring and returns its length, effectively isolating the last word.

### 15. [Max In Array](./Tier_1/MaxInArray.java)
- **Concept:** Linear Array Traversal
- **Approach:** Initializes `currentMax` with the first element of the array. It loops from the second element onward, updating `currentMax` (and `indexMax`) whenever a larger element is encountered, resulting in an $O(N)$ lookup.

### 16. [Missing Number](./Tier_1/MissingNumber.java)
- **Concept:** Arithmetic Series Sum
- **Approach:** Calculates the expected mathematical sum of the first $N$ numbers using the formula $N \times (N + 1) / 2$. Then, it iteratively sums the elements actually present in the array and returns the absolute difference.

### 17. [Remove Duplicates](./Tier_1/RemoveDuplicates.java)
- **Concept:** Sets for Uniqueness
- **Approach:** Traverses the integer array and adds each element to a `HashSet`. Since a set only stores unique values, this effectively filters out all duplicate numbers in $O(N)$ time. The resulting elements are then printed.

### 18. [Standard Deviation](./Tier_1/StandardDeviation.java)
- **Concept:** Statistical Math (Mean and Variance)
- **Approach:** Calculates the arithmetic mean (average) by summing all elements and dividing by the length. Next, it calculates the Mean Squared Deviation (MSD) by summing the squared difference of each element from the mean, then dividing by the array length.

### 19. [Sum Of Distances Between Three Points](./Tier_1/SumOfDistancesBetweenThreePoints.java)
- **Concept:** Euclidean Distance Geometry
- **Approach:** Defines a helper method to calculate Euclidean distance ($\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$) using `Math.pow` and `Math.sqrt`. Computes the distance for each pair of the three coordinate points and accumulates the sum.

# Coding Questions - Tier 2

This tier contains problems involving strings, arrays, bit manipulation, number operations, and validation.

## Problem Summaries

### 1. [Absolute Difference](./Tier_2/AbsoluteDifference.java)
- **Concept:** Arrays and absolute difference
- **Approach:** Counts values whose absolute difference from a target number is less than or equal to the given difference. Returns `-1` if no values match.

### 2. [Count Carry](./Tier_2/CountCarry.java)
- **Concept:** Digit manipulation
- **Approach:** Adds two numbers digit by digit and counts the number of carry operations.

### 3. [Encode Character](./Tier_2/EncodeCharacter.java)
- **Concept:** Number and string manipulation
- **Approach:** Squares each digit of a number and builds the encoded result in the original order.

### 4. [Is Anagram](./Tier_2/IsAnagram.java)
- **Concept:** Strings and sorting
- **Approach:** Sorts the characters of both strings and compares the sorted results.

### 5. [Longest Word](./Tier_2/LongestWord.java)
- **Concept:** String traversal
- **Approach:** Splits a sentence into words and returns the longest word. The first word is retained when lengths are equal.

### 6. [Maximum Exponent of 2](./Tier_2/MaxExponentOf2.java)
- **Concept:** Loops and number operations
- **Approach:** Iterates through a range and selects the number with the greatest value returned by `countTwos()`.

### 7. [Most Frequent Vowel](./Tier_2/MostFrequentVowel.java)
- **Concept:** Hash maps and frequency counting
- **Approach:** Counts character frequencies and returns the vowel with the highest frequency.

### 8. [Move Hyphens to Front](./Tier_2/MoveHyphenstoFront.java)
- **Concept:** String manipulation
- **Approach:** Counts the hyphens, places them at the beginning, and appends all other characters afterward.

### 9. [Password Checker](./Tier_2/PasswordChecker.java)
- **Concept:** Regular expressions and validation
- **Approach:** Validates password length, uppercase letters, digits, whitespace, slashes, and leading characters using a regular expression.

### 10. [Rearrangement of Bits](./Tier_2/RearrangementOfBits.java)
- **Concept:** Bit manipulation
- **Approach:** Counts the set bits using `Integer.bitCount()` and creates a number containing the same number of consecutive `1` bits.

### 11. [Replace Character](./Tier_2/ReplaceCharacter.java)
- **Concept:** Character arrays
- **Approach:** Swaps occurrences of two characters throughout a string.

### 12. [Replace Most Frequent Characters](./Tier_2/ReplaceMostFrequentCharacters.java)
- **Concept:** Hash maps and frequency analysis
- **Approach:** Finds the `k` most frequent characters and replaces them with a specified character.

### 13. [Reverse Words](./Tier_2/ReverseWords.java)
- **Concept:** String manipulation
- **Approach:** Splits a sentence into words and prints them in reverse order.

### 14. [Rhyme Words](./Tier_2/RhymeWords.java)
- **Concept:** Hash maps and string suffixes
- **Approach:** Groups words by their final `rhymeLength` characters and prints groups containing at least two words.

### 15. [Sum of Binary Distance](./Tier_2/SumOfBinaryDistance.java)
- **Concept:** Binary representation
- **Approach:** Converts a number to binary, maps `0` to `1` and `1` to `2`, and returns the sum of the mapped values.

# Coding Questions - Tier 3

This tier contains problems involving sorting, linked lists, sliding windows, matrices, and string reduction.

## Problem Summaries

### 1. [Chocolate Distribution](./Tier_3/ChocolateDistribution.java)
- **Concept:** Sorting and sliding windows
- **Approach:** Sorts packet quantities and checks each group of `m` consecutive packets to find the minimum difference between the largest and smallest amounts.

### 2. [Linked List Palindrome](./Tier_3/LinkedListPalindrome.java)
- **Concept:** Linked lists
- **Approach:** Compares and removes the first and last elements repeatedly to determine whether the list reads the same in both directions.

### 3. [Linked Lists](./Tier_3/LinkedLists.java)
- **Concept:** Linked list insertion
- **Approach:** Inserts values at the beginning of a `LinkedList` using `addFirst()`, then traverses and prints the list.

### 4. [Longest Substring Without Repeating Characters](./Tier_3/LongestSubstringWithoutRepeatingCharacters.java)
- **Concept:** Sliding window and hash sets
- **Approach:** Uses a moving window and a `HashSet` to track unique characters while searching for the longest substring without repeated characters.

### 5. [Maximum Favourite Song](./Tier_3/MaxFavouriteSong.java)
- **Concept:** Sliding window and string traversal
- **Approach:** Examines every substring of length `k` and returns the maximum number of `a` characters found in any window.

### 6. [Pair Sum with Maximum Product](./Tier_3/PairSumwithMaximumProduct.java)
- **Concept:** Sorting and two pointers
- **Approach:** Sorts the array and searches for pairs whose sum equals the target while comparing their products.

### 7. [Remove Adjacent Equal Characters](./Tier_3/RemoveAdj.java)
- **Concept:** String reduction and `StringBuilder`
- **Approach:** Removes adjacent equal character pairs and moves backward when necessary so newly formed pairs are also checked.

### 8. [Set Matrix Zeros](./Tier_3/SetMatrixZeros.java)
- **Concept:** Matrix traversal
- **Approach:** Intended to set entire rows and columns to zero when a matrix element is zero. Implementation is still in progress.

### 9. [Bulb Switch](./Tier_3/BulbSwitch.java)
- **Concept:** Array traversal and state changes
- **Approach:** Intended to calculate the minimum switches needed to reach the required bulb state. Implementation is still in progress.
