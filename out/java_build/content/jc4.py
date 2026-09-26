# -*- coding: utf-8 -*-
BLOCKS = [
    ("part", "Section 6 - Code Review Notes: Pitfalls Spotted and Fixes",
     "An honest review pass over the corpus. None of these are stylistic nitpicks for their own "
     "sake - each one is a bug or a sharp edge that would fail a test case, and each fix is a "
     "technique worth absorbing. Reading other people's bugs (including your own past ones) is the "
     "fastest way to stop writing them."),

    ("h2", "The six findings that would fail test cases"),
    ("body",
     "**1. FirstKWords - wrong loop bound.** The loop condition is `i < k && i < str.length()`, but "
     "`i` indexes `words`, so the second guard must be `words.length` (character count vs word "
     "count). For inputs where the word count exceeds the character count the current guard never "
     "protects against `ArrayIndexOutOfBounds`. Also, `append(words[i] + \" \")` concatenates a "
     "String inside the loop - the exact habit the rest of the corpus avoids; use "
     "`append(words[i]).append(' ')`."),
    ("body",
     "**2. MergeTwoSortedArrays - wrong length used for the second array.** The second copy loop "
     "runs `for (int i = 0; i < arr1.length; i++) { list.add(arr2[i]); }` - `arr2` is indexed by "
     "`arr1`'s length, which only works because the demo inputs happen to be equal-length (and "
     "`newArr` is allocated but never used). Fix the bound to `arr2.length`. Also note the approach "
     "itself: concatenating and sorting is O((n+m) log(n+m)); the true merge walk of two already-"
     "sorted arrays is O(n+m) - worth knowing both."),
    ("body",
     "**3. LongestSubstringWithoutRepeatingCharacters - returns the debug value.** The method "
     "returns `set.toString()` (the current window's characters) instead of the window length or "
     "the best substring. The algorithm is right; the return line is a leftover. On a judge, that "
     "scores zero for a correct solution - always re-read the method's contract before "
     "submitting."),
    ("body",
     "**4. PairSumwithMaximumProduct - inverted pointer movement.** After sorting, when "
     "`currentSum < target` the code decrements `end`, which makes the sum *smaller* - moving away "
     "from the target forever. The standard walk moves `start` up when the sum is too small and "
     "`end` down when it is too large. As written, the demo input `{11, 1, 2, 8, 10, 11, 15, 7}` "
     "with target 18 produces an empty result and misses the answer pair `{8, 10}` (product 80):"),
    ("code",
     'if (currentSum == target) { ... start++; end--; }\n'
     'else if (currentSum < target) { end--; }   // WRONG: sum shrinks further\n'
     'else { start++; }                          // WRONG: sum grows further\n'
     '// Fix: < target -> start++;  > target -> end--;'),
    ("body",
     "**5. ChocolateDistribution - shortcut reads the unsorted array.** The `arr.length == m` early "
     "return computes `Math.abs(arr[0] - arr[m - 1])` *before* `Arrays.sort` runs. When the whole "
     "array is one group, the answer is `max - min`, which equals that expression only if the "
     "input was already sorted. Move the sort above the guard, and the shortcut becomes correct "
     "for free."),
    ("body",
     "**6. MatrixEvenOddSecondLargest - no guard for short partitions.** Reading index "
     "`size() - 2` throws `IndexOutOfBoundsException` when a parity partition has fewer than two "
     "elements (for example a one-element array has an empty odd partition). The fix is the "
     "corpus's own habit elsewhere: guard the small case first. Minor sibling: `.intValue()` after "
     "`get()` is redundant - auto-unboxing already yields an `int`."),

    ("h2", "Spec-ambiguity findings (verify against the problem statement)"),
    ("bullets", [
        "**LinkedListPalindrome** returns `false` for a size-1 list (`size() < 2`). A single "
        "element is conventionally a palindrome; if the judge says so, change the guard to "
        "`size() < 1` - or to an empty-list special case only.",
        "**LengthOfLastWord** returns `-1` when the input has no space (a single word). The usual "
        "contract is that a lone word's last word is itself, so the length should be returned. "
        "Side note: the method prints the substring as it goes - printing inside a worker method "
        "mixes responsibilities.",
        "**RemoveDuplicates** prints through a `HashSet`, so output order is hash order, not "
        "first-seen order. If the judge expects insertion order, `LinkedHashSet` preserves it "
        "with the same one-line API. The file's unused `HashMap`/`Map` imports are leftovers.",
        "**MostFrequentVowel** and **ReplaceMostFrequentCharacters** break frequency ties by "
        "'first max seen while iterating the HashMap' - hash order, hence unspecified. Add an "
        "explicit tie rule (smallest character wins) if output must be deterministic.",
        "**ReverseWords** declares `static void main` without `public` - some JDK launcher "
        "versions will not run it. `public static void main` costs nothing and runs everywhere.",
        "**StandardDeviation** does integer arithmetic throughout (mean and mean-square both "
        "divide with truncation). Fine when the expected output is integer-formatted, but the "
        "name says deviation - know that this prints MSD, not the true standard deviation.",
        "**EncodeCharacter** builds its answer with `insert(0, ...)` - O(n) per insert, O(n^2) "
        "overall. Append-then-reverse is the linear habit.",
        "**SumOfPrimesLessThanN** starts its candidate loop at 1; `isPrime(1)` is guaranteed "
        "`false`, so start at 2. Harmless, but it is the kind of half-wasted iteration worth "
        "noticing.",
    ]),
    ("callout", "The review lesson",
     "Every finding above is a *contract* failure, not an algorithm failure: a wrong loop bound, a "
     "leftover return, an inverted comparison, an unguarded index. The algorithms were all correct. "
     "In a judged round, re-reading your own method's signature, bounds and return statement is "
     "worth more than one more optimisation."),

    ("part", "Section 7 - Per-File Index",
     "The complete map of the corpus: every file, the concept it exercises, its key trick or API, "
     "and its complexity. Use it as a spaced-repetition index - pick a row, rewrite the solution "
     "from memory, then check the trick column."),

    ("h2", "Tier 1 index (19 files)"),
    ("table", {
        "caption": "Tier 1 - fundamentals",
        "headers": ["File", "Concept", "Key trick / API", "Complexity"],
        "widths": [0.24, 0.24, 0.38, 0.14],
        "rows": [
            ["BinaryToDecimal", "Base conversion", "Positional accumulator; charAt(i) - '0'", "O(n)"],
            ["CountOccurences", "Frequency counting", "HashMap + getOrDefault; entrySet scan", "O(n)"],
            ["DecimalToBinary", "Base conversion", "% 2 + append + reverse; zero guard", "O(log n)"],
            ["FibonacciSeries", "Iterative sequence", "Two rolling variables; long; stdout-capture tests", "O(n)"],
            ["FirstKWords", "String tokens", "split + StringBuilder (bound bug noted in Section 6)", "O(n)"],
            ["GooglyPrimeNumbers", "Primes + digits", "i * i <= n test; digit-sum helper", "O(sqrt n)"],
            ["LengthOfLastWord", "String scan", "trim + reverse scan + substring", "O(n)"],
            ["MaxInArray", "Single-pass max", "Seed from arr[0]; track index of max", "O(n)"],
            ["MissingNumber", "Closed-form sum", "Gauss n(n+1)/2 minus actual", "O(n)"],
            ["NthFibonacciTerm", "Recursion", "Base case n <= 2 (exponential - iterate instead)", "O(2^n)"],
            ["PalindromeInRange", "Palindrome numbers", "Reverse via % 10 / * 10; Arrays.asList tests", "O(range)"],
            ["RemoveDuplicates", "Deduplication", "HashSet (order caveat in Section 6)", "O(n)"],
            ["RootsOfQuadraticEquation", "Algebra", "Discriminant branches; cancellation-safe form", "O(1)"],
            ["StandardDeviation", "Statistics", "Integer mean/MSD; stdout-capture tests", "O(n)"],
            ["SumOfDistancesBetweenThreePoints", "Geometry", "sqrt/pow helper reuse", "O(1)"],
            ["SumOfDivisors", "Number theory", "Divisor pairs to sqrt(n); i != n/i guard", "O(sqrt n)"],
            ["SumOfNumbersDivisibleByBoth3And5", "Divisibility", "LCM collapse: % 15", "O(n)"],
            ["SumOfPrimesLessThanN", "Primes", "Trial division per candidate", "O(n sqrt n)"],
            ["Table", "Loops", "Fixed 10-iteration table + running sum", "O(1)"],
        ],
    }),

    ("h2", "Tier 2 index (21 files)"),
    ("table", {
        "caption": "Tier 2 - collections, sorting and strings",
        "headers": ["File", "Concept", "Key trick / API", "Complexity"],
        "widths": [0.30, 0.20, 0.36, 0.14],
        "rows": [
            ["AbsoluteDifference", "Filter count", "Math.abs window; -1 sentinel", "O(n)"],
            ["CountCarry", "Digit simulation", "Column-add carry propagation; || loop bound", "O(digits)"],
            ["EncodeCharacter", "Digit mapping", "Squares; insert(0) building (see Section 6)", "O(n^2)"],
            ["EquilibriumSum", "Prefix sums", "rightSum = total - left - cur; -1 sentinel", "O(n)"],
            ["IntersectionOfLists", "Set operations", "HashSet contains + remove-on-match", "O(n + m)"],
            ["IsAnagram", "Canonical form", "Sort char arrays; length guard first", "O(n log n)"],
            ["LongestWord", "String scan", "Max length + index over split words", "O(n)"],
            ["MaxExponentOf2", "Integer log2", "Halving count; tie-break to smaller value", "O(range log n)"],
            ["MaximumDifferenceBetweenSuccessiveElement", "Sort + scan", "Adjacent gap after sort", "O(n log n)"],
            ["MergeTwoSortedArrays", "Sorting", "Concat + Collections.sort (bound bug in Section 6)", "O((n+m) log)"],
            ["MostFrequentVowel", "Hashing", "Count map; indexOf vowel test (tie caveat)", "O(n)"],
            ["MoveHyphenstoFront", "String rebuild", "count + \"-\".repeat + filtered append", "O(n)"],
            ["NegativeStockPriceDays", "Adjacent scan", "Count arr[i+1] < arr[i]; length - 1 bound", "O(n)"],
            ["PasswordChecker", "Regex validation", "Look-ahead pattern; null short-circuit", "O(n)"],
            ["RearrangementOfBits", "Bit manipulation", "Integer.bitCount; (result << 1) | 1", "O(bits)"],
            ["ReplaceCharacter", "In-place string", "Mutual swap via if / else if on char[]", "O(n)"],
            ["ReplaceMostFrequentCharacters", "Hashing + greedy", "k rounds of max-frequency pick", "O(n + k·m)"],
            ["ReverseWords", "Tokenising", "trim + split + reverse-order append", "O(n)"],
            ["RhymeWords", "Grouping", "computeIfAbsent by suffix; toLowerCase", "O(n·L)"],
            ["SumatEvenIndicesoftheReversedArray", "Two pointers", "In-place swap reversal; index mapping insight", "O(n)"],
            ["SumOfBinaryDistance", "Base conversion", "Remainder building; 0->1 / 1->2 positional remap", "O(log n)"],
        ],
    }),

    ("h2", "Tier 3 index (12 files)"),
    ("table", {
        "caption": "Tier 3 - pointers, windows and simulations",
        "headers": ["File", "Concept", "Key trick / API", "Complexity"],
        "widths": [0.34, 0.20, 0.32, 0.14],
        "rows": [
            ["BulbSwitch", "Greedy simulation", "XOR carries flip state - O(n) not O(n^2)", "O(n)"],
            ["ChocolateDistribution", "Sort + window", "Width-m slide: arr[i+m-1] - arr[i]", "O(n log n)"],
            ["LinkedListPalindrome", "Linked list", "getFirst/getLast + removeFirst/removeLast", "O(n)"],
            ["LinkedLists", "LinkedList basics", "addFirst loop + enhanced-for", "O(n)"],
            ["LongestSubstringWithoutRepeatingCharacters", "Sliding window", "HashSet shrink from left", "O(n)"],
            ["MatrixEvenOddSecondLargest", "Partition + sort", "Parity split; second largest = size() - 2", "O(n log n)"],
            ["MaxFavouriteSong", "Fixed window", "Brute-force substring count (running count = O(n))", "O(n·k)"],
            ["PairSumwithMaximumProduct", "Sort + two pointers", "Converge on sum; track max product (pointer bug in Section 6)", "O(n log n)"],
            ["RemoveAdj", "Stack-like string", "delete(i, i+2) + Math.max(0, i-1) rewind", "O(n^2) worst"],
            ["SetMatrixZeros", "Matrix marking", "boolean[] row/col markers, two passes", "O(m·n)"],
            ["StringDecoder", "Run-length decode", "split(\"0\"); (char)('A' + len - 1)", "O(n)"],
            ["VowelPermutation", "Recursion + counting", "Consonant count -> factorial via recursion", "O(c)"],
        ],
    }),

    ("part", "Section 8 - Revision Checklist",
     "The compressed takeaway. Each line is one move that this corpus proves out; if you can write "
     "each one from memory in under a minute, every problem these files solve is within reach."),

    ("bullets", [
        "**Count:** `map.put(k, map.getOrDefault(k, 0) + 1)`; group with `computeIfAbsent`.",
        "**Sort and scan:** anagram (sort both), adjacent gap, width-m window, two-pointer pair "
        "search, second largest as `size() - 2`.",
        "**Walk two ends:** swap-reverse arrays; `removeFirst`/`removeLast` palindromes; converge "
        "pointers on a sorted target.",
        "**Window it:** variable window with a HashSet; fixed window with a running count.",
        "**Carry a prefix:** `rightSum = total - leftSum - arr[i]`; adjacent scans bound at "
        "`length - 1`.",
        "**Play with digits:** `% 10` and `/ 10`; `i * i <= n` primes and divisor pairs; `% 15` "
        "LCM; Gauss sums; halving = floor(log2).",
        "**Think in bits:** `Integer.bitCount`; `(x << 1) | 1` builds masks; XOR is a toggle "
        "state - never re-flip a prefix.",
        "**Build strings safely:** StringBuilder only; append-then-reverse; `delete(i, i+2)` + "
        "rewind for adjacent duplicates; `repeat(count)` for blocks.",
        "**Convert characters:** `charAt(i) - '0'` and `(char) ('A' + k - 1)`; `indexOf` as "
        "membership.",
        "**Guard the edges first:** zero, one element, empty, null, negatives - then the loop.",
        "**Return exactly the contract:** the specified sentinel (-1 vs 0), the specified format, "
        "no prompts, no trailing whitespace - and prove it with the stdout-capture test.",
    ]),
]
