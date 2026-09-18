package Tier_1;

public class SumOfNumbersDivisibleByBoth3And5 {
    static int getSumOfNumbersDivisibleByBoth3And5(int n) {
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            if (i % 15 == 0) {
                sum += i;
            }
        } 
        return sum;
    }
    public static void main(String[] args) {
        test(0, 0);
        test(14, 0);
        test(15, 15);
        test(30, 45);
        test(100, 315);
    }

    private static void test(int n, int expected) {
        int actual = getSumOfNumbersDivisibleByBoth3And5(n);
        if (actual != expected) {
            throw new AssertionError("n=" + n + ": expected " + expected + ", but got " + actual);
        }
    }
}
