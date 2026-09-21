package Tier_2;

public class AbsoluteDifference {
    static int absDiff(int[] arr, int num, int diff) {
        int count = 0;
        for (int i = 0; i < arr.length; i++) {
            if (Math.abs(arr[i] - num) <= diff) {
                count++;
            }
        }

        return count > 0 ? count: -1;
    }

    public static void main(String[] args) {
        test(new int[]{1, 2, 3, 4, 5}, 3, 1, 3);
        test(new int[]{10, 20, 30}, 20, 0, 1);
        test(new int[]{-5, -2, 0, 3}, -2, 3, 3);
        test(new int[]{}, 10, 5, -1);
        test(new int[]{1, 2, 3}, 10, 0, -1);
        test(new int[]{12, 3, 14, 56, 77, 13}, 13, 2, 3);
    }

    private static void test(int[] arr, int num, int diff, int expected) {
        int actual = absDiff(arr, num, diff);
        if (actual != expected) {
            throw new AssertionError("Expected " + expected + ", but got " + actual);
        }
    }
}
