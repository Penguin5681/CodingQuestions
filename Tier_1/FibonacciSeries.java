package Tier_1;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

public class FibonacciSeries {
    static void printFib(int n) {
        long firstTerm = 0;
        long secondTerm = 1;

        for (int i = 1; i <= n; i++) {
            System.out.println(firstTerm);
            long next = firstTerm + secondTerm;
            firstTerm = secondTerm;
            secondTerm = next;
        }
    }
    public static void main(String[] args) {
        testPrintFibZeroTerms();
        testPrintFibOneTerm();
        testPrintFibFiveTerms();
        testPrintFibNegativeTerms();
        System.out.println("All tests passed");
    }

    private static void testPrintFibZeroTerms() {
        checkOutput(0, "", "zero terms");
    }

    private static void testPrintFibOneTerm() {
        checkOutput(1, "0\n", "one term");
    }

    private static void testPrintFibFiveTerms() {
        checkOutput(5, "0\n1\n1\n2\n3\n", "five terms");
    }

    private static void testPrintFibNegativeTerms() {
        checkOutput(-1, "", "negative terms");
    }

    private static void checkOutput(int n, String expected, String testName) {
        PrintStream originalOut = System.out;
        ByteArrayOutputStream output = new ByteArrayOutputStream();

        try {
            System.setOut(new PrintStream(output));
            printFib(n);
        } finally {
            System.setOut(originalOut);
        }

        if (!expected.equals(output.toString())) {
            throw new AssertionError("Failed " + testName + " test: expected "
                    + expected + " but got " + output);
        }
    }
}
