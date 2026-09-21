package Tier_3;

import java.util.Arrays;

/**
 * ChocolateDistribution
 */
public class ChocolateDistribution {
    static int findMinDiff(int[] arr, int m) {
        if (arr.length == m) {
            return Math.abs(arr[0] - arr[m - 1]);
        }

        Arrays.sort(arr);

        int minDiff = Integer.MAX_VALUE;
        for (int i = 0; i <= arr.length - m; i++) {
            int currentDiff = Math.abs(arr[i] - arr[i + m - 1]);
            minDiff = Math.min(currentDiff, minDiff);
        }

        return minDiff;
    }

    public static void main(String[] args) {
        System.out.println(findMinDiff(new int[] { 12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43,
                50 }, 7));
    }
}