# -*- coding: utf-8 -*-
BLOCKS = [
    ("part", "Section 1 - The Corpus at a Glance",
     "This report analyses all 52 Java source files in the CodingQuestions repository - 19 Tier 1 "
     "solutions, 21 Tier 2 solutions and 12 Tier 3 solutions (about 1,700 lines of code). It records "
     "every library and API the code relies on, the algorithmic concepts and patterns it uses, the "
     "reusable tips and tricks worth carrying into the exam, and an honest code-review pass over the "
     "spots where the current versions have bugs or sharp edges."),

    ("h2", "How the corpus is organised"),
    ("body",
     "Each file solves one assessment-style coding problem. Every solution follows the same shape: a "
     "static helper method that does the work, and a `main` that exercises it - either by printing "
     "results or by running small self-written tests. The tiers mark increasing difficulty: Tier 1 "
     "is arithmetic, loops and strings; Tier 2 introduces hashing, sorting and two-pointer work; "
     "Tier 3 adds sliding windows, greedy simulation and matrix problems."),
    ("table", {
        "caption": "Corpus composition",
        "headers": ["Tier", "Files", "Dominant themes", "Typical complexity"],
        "widths": [0.10, 0.10, 0.55, 0.25],
        "rows": [
            ["Tier 1", "19", "Number bases, digit manipulation, primes and divisors, recursion, string basics",
             "O(n) or O(sqrt(n))"],
            ["Tier 2", "21", "HashMap/HashSet counting, sorting, anagrams, regex, StringBuilder building, greedy picks",
             "O(n log n)"],
            ["Tier 3", "12", "Two pointers, sliding windows, in-place matrix marking, XOR simulation, linked lists",
             "O(n) to O(n log n)"],
        ],
    }),

    ("h2", "The one-paragraph summary"),
    ("body",
     "If the whole corpus had to be compressed into one sentence: **almost every problem here is "
     "solved by counting something in a HashMap, sorting the data and then scanning it once, walking "
     "two pointers toward each other, or extracting digits with `%` and `/`** - and the answers are "
     "assembled with `StringBuilder` and guarded with small edge-case checks at the top of each "
     "method. The libraries are confined to `java.util` collections and `java.lang` workhorses "
     "(`Math`, `StringBuilder`, `Integer`, `String`); there is no external dependency anywhere."),
    ("callout", "The meta-pattern of this codebase",
     "Count it, sort it, walk it, build it. A frequency map for counting, `Arrays.sort` for "
     "order-based insight, a single scan for the answer, and `StringBuilder` for output. Nine out of "
     "ten problems in this repository fall to one of those four moves."),

    ("part", "Section 2 - Libraries and APIs Used",
     "The corpus deliberately sticks to the standard library. This section inventories every import "
     "and every heavily-used `java.lang` API, where it appears, and the specific idiom each file "
     "uses - the exact vocabulary an examiner ( or a reviewer ) sees when reading this code."),

    ("h2", "The java.util collections"),
    ("table", {
        "caption": "Collection types used across the 52 files",
        "headers": ["Type", "Used in", "What it does there", "Idiom to remember"],
        "widths": [0.16, 0.22, 0.32, 0.30],
        "rows": [
            ["HashMap", "CountOccurences, MostFrequentVowel, ReplaceMostFrequentCharacters, RhymeWords",
             "Frequency counting; grouping words by suffix",
             "`mp.put(k, mp.getOrDefault(k, 0) + 1)`"],
            ["HashSet", "RemoveDuplicates, IntersectionOfLists, LongestSubstring..., ReplaceMostFrequentCharacters",
             "Deduplication; O(1) membership tests",
             "`set.contains(x)` then `set.remove(x)` for one-time matching"],
            ["Map.Entry", "CountOccurences, MostFrequentVowel, RhymeWords",
             "Iterating key-value pairs",
             "`for (Map.Entry<K,V> e : mp.entrySet())`"],
            ["ArrayList / List", "PalindromeInRange, IntersectionOfLists, MergeTwoSortedArrays, MatrixEvenOddSecondLargest, RhymeWords, PairSumwithMaximumProduct",
             "Building result lists of dynamic length",
             "`list.add(...)`; print via `toString()`"],
            ["LinkedList", "LinkedLists, LinkedListPalindrome",
             "Deque-style end operations",
             "`getFirst() / getLast() / removeFirst() / removeLast()`"],
        ],
    }),
    ("body",
     "Two grouping idioms stand out. The first is the frequency counter, which appears in four "
     "different files and is the single most repeated pattern in the corpus:"),
    ("code",
     'HashMap<Character, Integer> mp = new HashMap<>();\n'
     'for (char ch : str.toCharArray()) {\n'
     '    mp.put(ch, mp.getOrDefault(ch, 0) + 1);\n'
     '}'),
    ("body",
     "The second is the group-by-suffix pattern in `RhymeWords`, which uses `computeIfAbsent` with a "
     "lambda - the only lambda in the corpus, and the cleanest way to build a `Map<String, "
     "List<String>>` without a null check:"),
    ("code",
     'map.computeIfAbsent(suffix, key -> new ArrayList<>()).add(word);'),
    ("callout", "Trick - the counting idiom",
     "`getOrDefault(key, 0) + 1` replaces the three-line if-present-else dance. In an exam it saves "
     "time and removes the most common null-pointer mistake. Its sibling, `computeIfAbsent`, does "
     "the same favour for map-of-list grouping."),

    ("h2", "Sorting utilities: Arrays and Collections"),
    ("body",
     "Sorting appears in six files and comes in exactly two flavours: `Arrays.sort` for primitive "
     "arrays and char arrays (`IsAnagram`, `MaximumDifferenceBetweenSuccessiveElement`, "
     "`ChocolateDistribution`, `PairSumwithMaximumProduct`), and `Collections.sort` for `ArrayList`s "
     "(`MergeTwoSortedArrays`, `MatrixEvenOddSecondLargest`). None of the uses need a custom "
     "`Comparator` - every sort is natural ascending order, and the problems exploit the resulting "
     "order rather than the sorting itself. the sorting deep dive in Section 3 dissects each sort-dependent pattern."),
    ("body",
     "One subtle API appears in the test code of `PalindromeInRange`: `Arrays.asList(1, 2, 3)` wraps "
     "literal values into a `List` in one call, which makes expected-value comparisons readable."),

    ("h2", "The java.lang workhorses"),
    ("table", {
        "caption": "java.lang APIs the corpus depends on (no import needed)",
        "headers": ["API", "Where", "Notes and tricks"],
        "widths": [0.24, 0.30, 0.46],
        "rows": [
            ["StringBuilder", "11 files - all string building",
             "`append`, `insert(0, ...)`, `reverse()`, `delete(i, i+2)`, `charAt`, `length`. Never use "
             "`+=` on Strings in a loop."],
            ["String", "everywhere",
             "`split(\" \")`, `trim()`, `substring`, `toCharArray()`, `charAt`, `matches` (regex), "
             "`format`, `repeat` (Java 11+), `indexOf` as membership test."],
            ["Math", "8 files",
             "`abs`, `max`, `min`, `sqrt`, `pow`. `Math.abs(arr[i]-num)` for distance checks; "
             "`Math.max` inside scans."],
            ["Integer", "RearrangementOfBits, ChocolateDistribution",
             "`Integer.bitCount(n)` counts set bits; `Integer.MAX_VALUE` as a safe 'infinity' for "
             "min-tracking."],
            ["long arithmetic", "FibonacciSeries",
             "Fibonacci terms overflow `int` past term 46 - the code uses `long` for the running "
             "terms."],
        ],
    }),

    ("h2", "I/O and testing utilities"),
    ("body",
     "The only `java.io` usage in the corpus is a testing trick, not real I/O. `FibonacciSeries` and "
     "`StandardDeviation` capture their own stdout so the exact printed output can be compared "
     "against an expected string:"),
    ("code",
     'PrintStream originalOut = System.out;\n'
     'ByteArrayOutputStream output = new ByteArrayOutputStream();\n'
     'try {\n'
     '    System.setOut(new PrintStream(output));\n'
     '    printFib(n);              // method under test\n'
     '} finally {\n'
     '    System.setOut(originalOut);   // always restore\n'
     '}'),
    ("body",
     "This matters for the assessment directly: coding rounds diff the **exact** stdout, so being "
     "able to assert on captured output locally - including newlines, via the "
     "`replace(System.lineSeparator(), \"\\n\")` normalisation in `StandardDeviation` - is the "
     "cheapest way to catch formatting bugs before submitting."),
    ("callout", "Exam trap this trick defuses",
     "Wrong output format is the silent killer: a trailing space, a missing newline or a prompt line "
     "like `Enter a number:` fails otherwise-correct solutions. Capturing stdout and diffing it "
     "against the expected block catches all three before submission."),

    ("h2", "APIs conspicuously absent"),
    ("body",
     "It is just as informative to note what the corpus never uses: no `Scanner` or `BufferedReader` "
     "(inputs are hardcoded test arrays, since the round grades exact output), no Java Streams, no "
     "third-party libraries, no custom `Comparator` or lambda-based sorting, and no "
     "`Arrays.asList`-backed algorithms beyond test data. Everything is deliberately hand-rolled so "
     "the algorithm itself is visible - which is exactly the skill the coding round grades."),
]
