# -*- coding: utf-8 -*-
BLOCKS = [
    ("part", "Section 3 - Concepts and Techniques Catalogue",
     "This section walks through every algorithmic concept the corpus uses, from base conversion to "
     "sliding windows. Each concept names the files that use it, shows the core idiom as it actually "
     "appears in the code, and states the complexity the technique achieves - so it can double as a "
     "pattern-revision sheet."),

    ("h2", "Number base conversion (both directions)"),
    ("body",
     "Three files convert between bases, and each uses a different half of the standard toolkit. "
     "`BinaryToDecimal` consumes a binary string left to right with the positional accumulator - "
     "multiply the running value by the base, add the next digit. `DecimalToBinary` and "
     "`SumOfBinaryDistance` go the other way: repeatedly divide by 2, collect remainders, and "
     "reverse at the end."),
    ("code",
     '// binary -> decimal (left to right)\n'
     'decimal = decimal * 2 + (binary.charAt(i) - \'0\');\n\n'
     '// decimal -> binary (right to left, then reverse)\n'
     'while (decimal > 0) {\n'
     '    rsl.append(decimal % 2);\n'
     '    decimal /= 2;\n'
     '}\n'
     'return rsl.reverse().toString();'),
    ("callout", "Trick - char to digit",
     "`binary.charAt(i) - '0'` converts the character '1' to the integer 1 by subtracting code "
     "points. The inverse trick appears in `StringDecoder`: `(char) ('A' + len - 1)` maps a run "
     "length to a letter. Both avoid any parsing library."),
    ("body",
     "`DecimalToBinary` also shows the zero guard: `if (decimal == 0) return \"0\";` before the loop, "
     "because a `while (n > 0)` loop would otherwise return an empty string. Every `while (n > 0)` "
     "digit loop in the corpus carries this same implicit edge case."),

    ("h2", "Digit manipulation: the % 10 and / 10 pair"),
    ("body",
     "Six files extract digits without ever converting to a string: `n % 10` peels the last digit, "
     "`n /= 10` drops it. `GooglyPrimeNumbers` sums digits, `PalindromeInRange` builds the reversed "
     "number (`reverse = reverse * 10 + digit`), `CountCarry` simulates column addition digit by "
     "digit, `EncodeCharacter` squares each digit, and `MaxExponentOf2` counts how many times a "
     "number can be halved - which is floor(log2 n), the exponent of the largest power of 2 dividing "
     "the search range."),
    ("code",
     '// CountCarry: simulate adding two numbers column by column\n'
     'while (num1 != 0 || num2 != 0) {\n'
     '    int sum = currentCarry + num1 % 10 + num2 % 10;\n'
     '    if (sum > 9) { currentCarry = 1; carryCount++; }\n'
     '    else currentCarry = 0;\n'
     '    num1 /= 10; num2 /= 10;\n'
     '}'),
    ("body",
     "`CountCarry` shows the digit-loop refinement worth remembering: the loop condition is `num1 != "
     "0 || num2 != 0` (either), not `and` - otherwise unequal-length numbers stop early. And the "
     "carry is *propagated* into the next column before being reset, which is the whole simulation."),
    ("callout", "Trick - max exponent of 2 without logs",
     "`countTwos(n)` divides by 2 until zero and counts the divisions: no `Math.log`, no floating "
     "point, no off-by-one. It is the integer-only way to get floor(log2 n) and it is safe for every "
     "positive int."),

    ("h2", "Number theory: primes, divisors and the sqrt(n) loop"),
    ("body",
     "Three files do number theory, and all three use the same optimisation: loop only to the square "
     "root, expressed overflow-safely as `i * i <= n` rather than `i <= Math.sqrt(n)`. "
     "`GooglyPrimeNumbers` and `SumOfPrimesLessThanN` use it for primality tests; `SumOfDivisors` "
     "extends it to the divisor-pair method - when `i` divides `n`, both `i` and `n / i` are "
     "divisors, so add both and guard against counting the square root twice with `i != n / i`."),
    ("code",
     'for (int i = 1; i <= Math.sqrt(n); i++) {\n'
     '    if (n % i == 0) {\n'
     '        sum += i;\n'
     '        if (i != n / i) sum += n / i;  // avoid double-count\n'
     '    }\n'
     '}'),
    ("body",
     "Two smaller number-theory moves: `SumOfNumbersDivisibleByBoth3And5` collapses 'divisible by 3 "
     "and 5' into a single `i % 15 == 0` check (15 is the LCM), and `MissingNumber` uses the Gauss "
     "formula `n * (n + 1) / 2` so the missing value is one subtraction instead of a search."),
    ("callout", "Trick - LCM collapse",
     "Whenever a condition says 'divisible by A and B', check divisibility by LCM(A, B) instead. "
     "One modulo instead of two, and it reads as the mathematical statement it is."),

    ("h2", "Hashing: counting, grouping and membership"),
    ("body",
     "The HashMap counting idiom was covered in Section 2; the *decisions* around it are what make it "
     "a technique. Three distinct uses appear:"),
    ("bullets", [
        "**Frequency counting** (`CountOccurences`, `MostFrequentVowel`, "
        "`ReplaceMostFrequentCharacters`) - build the count map, then scan entries for the answer. "
        "The scan compares `entry.getValue()` against a running max and pulls `entry.getKey()` as "
        "the answer.",
        "**Grouping** (`RhymeWords`) - key by derived property (the last `rhymeLength` characters, "
        "lower-cased), value is the list of matching words; groups with `size() >= 2` are the "
        "rhyme families.",
        "**Membership and dedup** (`RemoveDuplicates`, `IntersectionOfLists`, "
        "`LongestSubstringWithoutRepeatingCharacters`) - a HashSet answers 'seen it?' in O(1). "
        "`IntersectionOfLists` adds one refinement: after matching, it `remove`s the element so each "
        "set entry matches at most once.",
    ]),
    ("callout", "Trick - indexOf as a membership test",
     "`\"aeiouAEIOU\".indexOf(ch) != -1` is the corpus's vowel test: no Set, no loop, one line. For a "
     "fixed tiny alphabet it beats a HashSet on clarity, and the same string doubles for both cases "
     "at once."),
    ("body",
     "One caveat the corpus itself demonstrates: `HashMap` iteration order is unspecified. "
     "`MostFrequentVowel` breaks ties with 'first max wins' during `entrySet()` iteration, so which "
     "vowel it returns on a tie depends on the map's internal hashing. If deterministic output "
     "matters, use a `TreeMap` (sorted keys) or `LinkedHashMap` (insertion order), or add an explicit "
     "tie-break rule."),

    ("h2", "Sorting deep dive: four patterns built on Arrays.sort"),
    ("body",
     "Sorting is the highest-leverage library call in the corpus: five problems become almost trivial "
     "once the data is ordered. Four distinct sort-then-act patterns appear:"),
    ("h3", "Pattern 1 - sort to compare canonically (anagram check)"),
    ("body",
     "`IsAnagram` sorts both strings' char arrays; two words are anagrams exactly when the sorted "
     "forms are equal. The cheap length guard up front (`s.length() != t.length()`) skips all work "
     "for the obvious mismatch. Cost: O(n log n) against the O(n) counting alternative - chosen here "
     "because the sorted comparison is three lines and hard to get wrong."),
    ("h3", "Pattern 2 - sort then scan neighbours (minimum adjacent gap)"),
    ("body",
     "`MaximumDifferenceBetweenSuccessiveElement` answers 'maximum difference between successive "
     "elements' by sorting first: after sorting, the answer is the largest gap between *adjacent* "
     "sorted values, a single O(n) scan. This is the classic realisation that 'successive' means "
     "'neighbouring in sorted order', not 'consecutive in the input'."),
    ("code",
     'Arrays.sort(arr);\n'
     'int maxDiff = 0;\n'
     'for (int i = 0; i < arr.length - 1; i++) {\n'
     '    maxDiff = Math.max(maxDiff, Math.abs(arr[i+1] - arr[i]));\n'
     '}'),
    ("h3", "Pattern 3 - sort then slide a window (chocolate distribution)"),
    ("body",
     "`ChocolateDistribution` sorts the packets, then every window of `m` consecutive sorted values "
     "is a candidate group; the answer is the minimum of `arr[i + m - 1] - arr[i]` across all "
     "windows. Sorting guarantees each window is the tightest possible group containing its values, "
     "so no other combination can beat it. The loop runs `i <= arr.length - m` - the window "
     "arithmetic that keeps the last full window in range."),
    ("h3", "Pattern 4 - sort then converge two pointers (pair sum)"),
    ("body",
     "`PairSumwithMaximumProduct` sorts, then walks `start` and `end` inward comparing "
     "`arr[start] + arr[end]` with the target, tracking the maximum product among matches. Section "
     "3.5 covers the two-pointer mechanics - the sorting here is what makes the sum comparison "
     "actionable (move the pointer that moves the sum toward the target)."),
    ("callout", "Trick - sort changes what is adjacent",
     "Three of these four patterns share one idea: after sorting, 'next to each other' becomes "
     "meaningful. Gaps, windows and pairs all become local scans. If a problem mentions closest, "
     "smallest-range, or most-balanced grouping, try `Arrays.sort` first and re-read the problem in "
     "sorted space."),
    ("body",
     "`MatrixEvenOddSecondLargest` adds a variant: `Collections.sort` on two `ArrayList`s after "
     "splitting by index parity, then reading the second largest directly as index `size() - 2`. "
     "Sorting turns 'second largest' into a subscript - no second-scan bookkeeping needed. (The "
     "single-scan alternative tracks `max` and `secondMax` in one pass; see the checklist in Section "
     "6.)"),

    ("h2", "Two pointers and sliding windows"),
    ("body",
     "Four pointer arrangements appear, increasing in sophistication:"),
    ("table", {
        "caption": "Pointer patterns in the corpus",
        "headers": ["Pattern", "Files", "Mechanics", "Complexity"],
        "widths": [0.24, 0.26, 0.34, 0.16],
        "rows": [
            ["Converging pointers", "PairSumwithMaximumProduct",
             "start/end walk inward; move the side that moves the sum toward the target", "O(n log n) with sort"],
            ["Both-ends swap", "SumatEvenIndicesoftheReversedArray",
             "swap arr[left] and arr[right], step inward - in-place array reversal", "O(n) time, O(1) space"],
            ["Ends-only access", "LinkedListPalindrome",
             "compare getFirst/getLast, then removeFirst/removeLast - shrink from both ends", "O(n)"],
            ["Variable sliding window", "LongestSubstringWithoutRepeatingCharacters",
             "right expands, left shrinks on duplicate via HashSet", "O(n)"],
        ],
    }),
    ("body",
     "`LongestSubstringWithoutRepeatingCharacters` is the corpus's flagship window: `right` scans "
     "forward, and while the new character is already in the set, the left edge removes characters "
     "and advances. The window `[left..right]` is therefore always duplicate-free, and "
     "`maxLen = Math.max(maxLen, right - left + 1)` records the best span. `MaxFavouriteSong` is the "
     "fixed-width sibling: every substring window of width `k` is measured (brute-force O(n·k); a "
     "running count of 'a' characters entering/leaving the window would make it O(n))."),
    ("callout", "Trick - reverse by mapping, not by mutating",
     "`SumatEvenIndicesoftheReversedArray` reverses in place, then sums even indices. The insight "
     "worth keeping: reversing maps index `i` to `n - 1 - i`, so the answer could be computed "
     "directly from the original array - sum every `arr[i]` where `(n - 1 - i) % 2 == 0`. Same "
     "result, no mutation, no second pass."),

    ("h2", "Prefix sums and running aggregates"),
    ("body",
     "`EquilibriumSum` is the corpus's one prefix-sum showcase. Compute the total once; then for each "
     "index, `rightSum = totalSum - leftSum - arr[i]` and compare with `leftSum` - no nested loops, "
     "O(n) time, O(1) space, with `-1` as the not-found sentinel. `NegativeStockPriceDays` uses the "
     "same adjacent-scan discipline for a simpler question (count `arr[i+1] < arr[i]`), and "
     "`StandardDeviation` accumulates mean and mean-squared-deviation in two linear passes - "
     "notably in integer arithmetic, which keeps the printed output exact but truncates decimals."),

    ("h2", "Bit manipulation"),
    ("body",
     "Two files use bits deliberately, and both pay off handsomely:"),
    ("bullets", [
        "**`Integer.bitCount(n)`** (`RearrangementOfBits`) - the population count, straight from the "
        "standard library. The problem 'rearrange all 1-bits to the front' reduces to: count the "
        "ones, then rebuild `2^k - 1` by `result = (result << 1) | 1`, k times.",
        "**XOR as a state flip** (`BulbSwitch`) - the greedy bulb problem in O(n). "
        "`current = arr[i] ^ flipped` applies the accumulated flip state without touching the "
        "prefix; when a bulb is off, increment the switch count and toggle `flipped ^= 1`. The "
        "naive version re-flips every remaining bulb per switch and costs O(n^2).",
    ]),
    ("code",
     '// BulbSwitch: XOR carries the "has this index been flipped an odd number of times" state\n'
     'int current = arr[i] ^ flipped;\n'
     'if (current == 0) { count++; flipped ^= 1; }'),
    ("callout", "Trick - XOR is a toggle",
     "`x ^ 1` flips a bit, `a ^ b` diffs two values, and XOR-ing the same state twice cancels. "
     "Whenever a simulation says 'flip everything after position i', store the *parity* of flips "
     "instead of doing the flips - that is the O(n^2) to O(n) jump."),

    ("h2", "Strings and StringBuilder"),
    ("body",
     "String problems dominate Tier 2, and every one of them assembles its answer with "
     "`StringBuilder` rather than String concatenation (concatenating in a loop copies the string "
     "each time - O(n^2) total). Three building styles appear:"),
    ("bullets", [
        "**Append then reverse** (`DecimalToBinary`, `ReverseWords`) - build in the natural order, "
        "call `reverse()`. Best when later elements belong earlier (remainders, word order).",
        "**Insert at front** (`EncodeCharacter`) - `insert(0, ...)` builds left-to-right for "
        "digit streams. Correct but each insert shifts the buffer; for exam-sized inputs it is "
        "fine, append-plus-reverse is the general habit.",
        "**Rebuild with a filter** (`MoveHyphenstoFront`, `ReplaceMostFrequentCharacters`) - count "
        "what moves or changes, then append characters conditionally. `\"-\".repeat(hCount)` "
        "(Java 11+) seeds the hyphen block in one call.",
    ]),
    ("body",
     "Four string-specific tricks round out the catalogue: `String.split(\" \")` tokenises into a "
     "word array for `FirstKWords`, `LongestWord` and `ReverseWords`; `trim()` normalises edge "
     "spaces before splitting or scanning (`LengthOfLastWord`, `ReverseWords`); `substring(i + 1)` "
     "after finding a delimiter extracts the tail; and `String.matches(regex)` validates a whole "
     "string in one call - `PasswordChecker` packs three requirements into one look-ahead pattern, "
     "with a null check short-circuiting before the regex runs."),
    ("h3", "The adjacent-duplicate stack trick"),
    ("body",
     "`RemoveAdj` removes pairs of adjacent equal characters (`abbaca` becomes `ca`) with a "
     "StringBuilder used like a stack: when `charAt(i) == charAt(i + 1)`, `delete(i, i + 2)` both "
     "characters, then rewind the index with `i = Math.max(0, i - 1)` so the newly-adjacent pair "
     "left behind is re-checked. No explicit stack, one buffer, O(n) amortised."),
    ("code",
     'if (builder.charAt(i) == builder.charAt(i + 1)) {\n'
     '    builder.delete(i, i + 2);\n'
     '    i = Math.max(0, i - 1);   // re-check the seam\n'
     '} else { i++; }'),
    ("h3", "Run-length decoding"),
    ("body",
     "`StringDecoder` splits the binary string on `'0'`; each remaining token is a run of 1s whose "
     "length maps to a letter via `(char) ('A' + length - 1)`. Split-on-delimiter plus a "
     "length-to-value mapping solves in four lines what looks like a parser problem."),

    ("h2", "In-place matrices and marker arrays"),
    ("body",
     "`SetMatrixZeros` is the corpus's 2-D showcase: one pass records which rows and columns contain "
     "a zero into `boolean[] rowZeros` and `boolean[] colZeros`; a second pass rewrites cells whose "
     "row or column is marked. This is the O(m + n) extra-space variant of the classic problem - "
     "clear and safe. The famous O(1)-space version instead uses the matrix's own first row and "
     "column as the markers, at the cost of fiddly bookkeeping; for an exam the marker arrays are "
     "the version you can write without bugs."),
    ("body",
     "`MatrixEvenOddSecondLargest` also traverses a 2-D mindset on 1-D data - partition by index "
     "parity (`i % 2 == 0`), sort each partition, and read answers by subscript."),

    ("h2", "Linked lists via the LinkedList deque API"),
    ("body",
     "`LinkedListPalindrome` never touches nodes or pointers: it uses `java.util.LinkedList`'s "
     "double-ended API - compare `getFirst()` with `getLast()`, then `removeFirst()` and "
     "`removeLast()`, until fewer than two elements remain. It is the two-pointer palindrome "
     "technique expressed through a library type. The trade-off to know: `get(i)` on a "
     "`LinkedList` is O(n) (it walks from the nearest end), which is why this code uses only the "
     "end operations - each is O(1)."),
    ("callout", "Trick - LinkedList ends over indexing",
     "When a `LinkedList` is the given structure, reach for `getFirst`/`getLast`/`removeFirst`/"
     "`removeLast` and never index into it. Every indexed access on a linked list hides a linear "
     "walk; the end operations are genuinely constant time."),

    ("h2", "Recursion and permutations"),
    ("body",
     "Two files recurse. `NthFibonacciTerm` is the textbook doubly-recursive definition with a base "
     "case at `n <= 2` (and it deliberately folds `n = 0` and negatives into that base case) - "
     "correct but O(2^`n`); the iterative two-variable version in `FibonacciSeries` is the same "
     "answer in O(n) time and O(1) space, and is the version to write when `n` can be large. "
     "`VowelPermutation` recurses for factorial: count the consonants, and the number of ways to "
     "arrange them is `consonantCount!` - a counting insight (`n * fact(n - 1)`) rather than an "
     "iteration problem."),
    ("body",
     "The pairing teaches the exam lesson directly: recursion states the recurrence beautifully; "
     "iteration executes it cheaply. Recognise the recurrence (factorial, Fibonacci, digit sums) "
     "from the base case, then choose the loop when size demands it."),
]
