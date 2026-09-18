package Tier_1;

public class NthFibonacciTerm {
    static int nthFib(int n) {
        if (n <= 2) {
            return 1;
        }

        return nthFib(n - 1) + nthFib(n - 2);
    }

    public static void main(String[] args) {
        testNthFib();
    }

    private static void testNthFib() {
        assertEquals(1, nthFib(1));
        assertEquals(1, nthFib(2));
        assertEquals(2, nthFib(3));
        assertEquals(5, nthFib(5));
        assertEquals(55, nthFib(10));
        assertEquals(1, nthFib(0));
        assertEquals(1, nthFib(-1));
    }

    private static void assertEquals(int expected, int actual) {
        if (expected != actual) {
            throw new AssertionError("Expected " + expected + ", but got " + actual);
        }
    }
}
