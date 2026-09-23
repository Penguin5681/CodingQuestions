package Tier_3;

/**
 * StringDecoder
 */
public class StringDecoder {
    static String decodeString(String string) {
        // 10110111
        // 1 | 11 | 111
        // A | B | C

        StringBuilder result = new StringBuilder("");

        String[] charSequence = string.split("0");

        for (String oneLen : charSequence) {
            result.append((char) ('A' + oneLen.length() - 1));
        }

        return result.toString();
    }

    public static void main(String[] args) {
        String[][] testCases = {
                { "10110111", "ABC" },
                { "1", "A" },
                { "11", "B" },
                { "111", "C" },
                { "10101", "AAA" },
                { "11110111", "DC" }
        };

        for (String[] testCase : testCases) {
            String actual = decodeString(testCase[0]);
            if (!actual.equals(testCase[1])) {
                throw new AssertionError(
                        "Expected " + testCase[1] + " but got " + actual);
            }
            System.out.println(testCase[0] + " -> " + actual);
        }
    }
}