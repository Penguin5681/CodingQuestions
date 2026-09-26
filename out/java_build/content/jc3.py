# -*- coding: utf-8 -*-
BLOCKS = [
    ("part", "Section 4 - Testing Patterns in the Corpus",
     "Roughly half the files test themselves inside `main` with hand-rolled assertion helpers. This "
     "section records the four testing patterns the corpus uses, because they are directly reusable "
     "in an exam environment where no JUnit is available and output must be exact."),

    ("h2", "Pattern 1: the assert-helper family"),
    ("body",
     "`GooglyPrimeNumbers`, `SumOfPrimesLessThanN`, `SumOfDivisors`, `DecimalToBinary`, "
     "`NthFibonacciTerm`, `CountCarry`, `AbsoluteDifference` and `StringDecoder` all define tiny "
     "private helpers - `assertEquals`, `assertTrue`, `assertFalse` - that throw "
     "`AssertionError` with a message naming the case. The pattern is three lines per helper and "
     "turns `main` into a readable test suite:"),
    ("code",
     'private static void assertEquals(int expected, int actual) {\n'
     '    if (expected != actual) {\n'
     '        throw new AssertionError("Expected " + expected + ", but got " + actual);\n'
     '    }\n'
     '}'),
    ("body",
     "The same files show the discipline that makes the helpers valuable: tests cover **zero** "
     "(`digitSum(0)`, `findPrimeSum(0)`), **one** (`isPrime(1)` is false), **negatives** "
     "(`nthFib(-1)`), **empty input** (`absDiff` on `{}` returns -1), and **boundaries** "
     "(`n == 1` in `SumOfDivisors` returns 0, since 1 is not a proper divisor of itself)."),

    ("h2", "Pattern 2: expected-output tables"),
    ("body",
     "`StringDecoder` and `PalindromeInRange` store test cases as data - a `String[][]` of "
     "{input, expected} pairs, or `Arrays.asList(...)` expectations - and loop over them. Adding a "
     "case is one array row, not a new block of code. This is the lightest-weight table-driven test "
     "possible in plain Java."),
    ("code",
     'String[][] testCases = { { "10110111", "ABC" }, { "1", "A" }, { "11110111", "DC" } };\n'
     'for (String[] testCase : testCases) {\n'
     '    if (!decodeString(testCase[0]).equals(testCase[1]))\n'
     '        throw new AssertionError(...);\n'
     '}'),

    ("h2", "Pattern 3: stdout capture for exact-output methods"),
    ("body",
     "Methods that print instead of returning (`FibonacciSeries.printFib`, "
     "`StandardDeviation.deviation`) are tested by swapping `System.out` for a "
     "`ByteArrayOutputStream`-backed `PrintStream`, restoring it in a `finally`, and comparing the "
     "captured string against the exact expected block. `StandardDeviation` adds the newline "
     "normalisation (`replace(System.lineSeparator(), \"\\n\")`) so the test is OS-independent. This "
     "is the pattern that guards the one thing an online judge actually grades."),

    ("h2", "Pattern 4: demonstration mains"),
    ("body",
     "The remaining files (`Table`, `LinkedLists`, `MaxInArray`, `ReplaceCharacter`, "
     "`MoveHyphenstoFront`) print worked examples across several inputs. Useful while developing, "
     "but weaker than the assert patterns - nothing fails if an output changes. The corpus trend is "
     "clear though: earlier files demonstrate, later files assert."),

    ("part", "Section 5 - Tips and Tricks: The Master List",
     "Every reusable technique observed in the 52 files, condensed into one checklist. The arrow "
     "points at the concrete trick; the text says when to reach for it. If you revise only one "
     "section of this report before the coding round, make it this one."),

    ("h2", "Characters, digits and small maths"),
    ("numbers", [
        "`charAt(i) - '0'` converts a digit character to its integer value; `(char) ('A' + k - 1)` "
        "maps 1..26 to letters. No parsing libraries needed.",
        "`n % 10` peels the last digit, `n /= 10` drops it; loop `while (n > 0)` for digits, but "
        "guard the `n == 0` case separately (DecimalToBinary does).",
        "Loop `while (num1 != 0 || num2 != 0)` - *or*, not *and* - when two numbers' digits are "
        "consumed in lockstep (CountCarry).",
        "`i * i <= n` is the overflow-safe, allocation-free way to loop to sqrt(n) for primes and "
        "divisors; add the `i != n / i` guard when collecting divisor pairs.",
        "Divisible by A and B? Check `x % LCM(A,B) == 0` - one modulo (the % 15 trick).",
        "Missing number in 1..n? Gauss: `n * (n + 1) / 2 - actualSum` - no array scan for the gap.",
        "floor(log2 n) without logs: count how many times `n /= 2` until zero (MaxExponentOf2).",
        "`Math.abs`, `Math.max`, `Math.min` replace four-line if-blocks; `Integer.MAX_VALUE` is the "
        "safe starting point for min-tracking.",
        "Watch overflow: Fibonacci passed term 46 overflows `int` - FibonacciSeries uses `long`.",
        "Numerically fragile formula? Rearrange it. RootsOfQuadraticEquation computes roots via "
        "`q = -0.5 * (b + sign(b) * sqrt(disc))`, `root1 = q / a`, `root2 = c / q` to avoid "
        "catastrophic cancellation - and handles `a == 0` (linear) and `b == 0 && c == 0` "
        "(infinite solutions) before touching the discriminant.",
    ]),

    ("h2", "Collections idioms"),
    ("numbers", [
        "Frequency counting in one line: `mp.put(k, mp.getOrDefault(k, 0) + 1)`.",
        "Grouping into a map of lists in one line: `map.computeIfAbsent(key, x -> new ArrayList<>())"
        ".add(item)`.",
        "HashSet for 'have I seen it?', plus `set.remove(x)` when an element may match only once "
        "(IntersectionOfLists).",
        "Iterate with `for (Map.Entry<K, V> e : map.entrySet())` when you need key *and* value.",
        "HashMap iteration order is unspecified - if a tie-break matters, use TreeMap/LinkedHashMap "
        "or compare explicitly (MostFrequentVowel returns hash-order-dependent answers on ties).",
        "LinkedList: only `getFirst/getLast/removeFirst/removeLast` - never index into it; `get(i)` "
        "is O(n).",
        "`Arrays.sort` for arrays and char arrays, `Collections.sort` for Lists; expected values as "
        "`Arrays.asList(...)` make test data one-liners.",
        "`\"-\".repeat(count)` (Java 11+) seeds a repeated block without a loop (MoveHyphenstoFront).",
    ]),

    ("h2", "Sorting moves"),
    ("numbers", [
        "Anagram check: length guard, then sort both char arrays and compare (IsAnagram).",
        "'Max/min difference between successive elements' means *sorted-order neighbours* - sort, "
        "then scan `arr[i+1] - arr[i]` (MaximumDifferenceBetweenSuccessiveElement).",
        "Smallest range covering m items: sort, then slide a window of width m and minimise "
        "`arr[i + m - 1] - arr[i]` (ChocolateDistribution).",
        "Pair with a target sum: sort, converge two pointers; move `start` up when the sum is "
        "small, `end` down when it is large (PairSumwithMaximumProduct).",
        "Second largest: sort and read index `size() - 2` - or track `max` and `secondMax` in one "
        "scan if sorting is too expensive (MatrixEvenOddSecondLargest).",
        "Sorting is O(n log n) - if the problem only needs counts or extrema, a single scan or a "
        "counting array is cheaper. Sort when *order* answers the question.",
    ]),

    ("h2", "Pointers, windows and prefixes"),
    ("numbers", [
        "In-place reversal: swap `arr[left]` and `arr[right]`, step both inward, stop at "
        "`left >= right` (SumatEvenIndicesoftheReversedArray).",
        "Prefix sums kill nested loops: `rightSum = total - leftSum - arr[i]` in one pass "
        "(EquilibriumSum); return -1 as the sentinel.",
        "Variable sliding window: expand `right`, shrink `left` while a HashSet still contains the "
        "incoming character; track `right - left + 1` (LongestSubstringWithoutRepeatingCharacters).",
        "Fixed window: instead of recounting each window, keep a running count - add the entering "
        "character, drop the leaving one (MaxFavouriteSong is the brute-force version; O(n·k) "
        "becomes O(n)).",
        "Adjacent-pair scans use `arr.length - 1` as the bound - off-by-one lives exactly there "
        "(NegativeStockPriceDays).",
    ]),

    ("h2", "Bits and simulation"),
    ("numbers", [
        "`Integer.bitCount(n)` counts set bits; rebuild all-ones from them with `result = (result "
        "<< 1) | 1` (RearrangementOfBits).",
        "XOR is a toggle: `x ^ 1` flips, applying twice cancels. Carry flip *state* in one int "
        "instead of re-flipping a whole prefix (BulbSwitch: O(n^2) becomes O(n)).",
        "Greedy simulations usually need only local state - the current element plus one carried "
        "flag. Find that flag before writing loops.",
    ]),

    ("h2", "Strings and output"),
    ("numbers", [
        "Never `+=` Strings in a loop; use `StringBuilder.append` (eleven files follow this; "
        "`FirstKWords` shows the concat habit to avoid).",
        "Build-then-reverse beats insert-at-front for anything built right-to-left (remainders, "
        "reverse word order).",
        "Mutually swapping two characters? Use `if / else if` in the same pass, or the second "
        "replacement overwrites the first (ReplaceCharacter).",
        "Adjacent-pair removal: `StringBuilder.delete(i, i + 2)` then rewind `i = Math.max(0, i - "
        "1)` to re-check the seam (RemoveAdj - a stack without a stack).",
        "Run-length decode via `split` on the delimiter, then map run length to value "
        "(StringDecoder).",
        "One regex with look-aheads validates multi-rule strings: `(?=.*[0-9])(?=.*[A-Z])...` - and "
        "null-check before calling `matches` (PasswordChecker).",
        "Membership in a tiny alphabet: `\"aeiouAEIOU\".indexOf(ch) != -1` - one line, no Set.",
        "`split(\" \")` + `trim()` handles stray spaces; but note `split` drops trailing empty "
        "tokens - trim first.",
    ]),

    ("h2", "Structure, guards and exam discipline"),
    ("numbers", [
        "Guard the edges before the loop: zero, one element, empty input, null, negatives. The "
        "corpus's correct answers almost always start with a two-line early return.",
        "Sentinel returns are part of the spec: `count > 0 ? count : -1` (AbsoluteDifference), "
        "`return -1` for not-found (EquilibriumSum). Read the Notes block for the exact sentinel "
        "the judge expects.",
        "Seed extrema from `arr[0]`, not `Integer.MIN_VALUE`, when the array can be all-negative "
        "and non-empty (MaxInArray).",
        "Print exactly what the problem states: no prompts, no trailing whitespace. The stdout-"
        "capture test pattern (Section 4) verifies this mechanically.",
        "Write the tiny assert helpers first, then the solution - the tests document the intended "
        "edge cases while the algorithm is fresh.",
        "Keep helpers static and stateless; pass everything in as parameters - every file here "
        "follows that shape, which makes methods trivially testable.",
    ]),
]
