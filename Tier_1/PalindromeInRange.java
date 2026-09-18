package Tier_1;

import java.util.ArrayList;
import java.util.Arrays;

public class PalindromeInRange {
    static int reverseNumberHelper(int n) {
        int reverse = 0;
        while (n > 0) {
            int currentDigit = n % 10;
            reverse = (reverse * 10) + currentDigit;
            n /= 10;
        }
        return reverse;
    }

    static ArrayList<Integer> getRangePalindrome(int start, int end) {
        ArrayList<Integer> rsl = new ArrayList<>();
        for (int i = start; i <= end; i++) {
            if (i == reverseNumberHelper(i)) {
                rsl.add(i);
            }
        }
        return rsl;
    }

    public static void main(String[] args) {
        testRange(1, 10, new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9)));
        testRange(10, 30, new ArrayList<>(Arrays.asList(11, 22)));
        testRange(100, 150, new ArrayList<>(Arrays.asList(101, 111, 121, 131, 141)));
        testRange(5, 5, new ArrayList<>(Arrays.asList(5)));
        testRange(20, 21, new ArrayList<>());
    }

    private static void testRange(int start, int end, ArrayList<Integer> expected) {
        ArrayList<Integer> actual = getRangePalindrome(start, end);
        boolean passed = actual.equals(expected);
        System.out.printf("Range [%d, %d]: %s - %s%n", start, end,
                passed ? "PASS" : "FAIL", actual);
    }
}
