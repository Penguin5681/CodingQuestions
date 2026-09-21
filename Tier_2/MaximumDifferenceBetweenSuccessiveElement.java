package Tier_2;

import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;

public class MaximumDifferenceBetweenSuccessiveElement {
    static int findMaxDiff(int[] arr) {
        Arrays.sort(arr);
        int maxDiff = 0;

        for (int i = 0; i < arr.length - 1; i++) {
            maxDiff = Math.max(maxDiff, Math.abs(arr[i+1] - arr[i]));
        }

        return maxDiff;
    }
    public static void main(String[] args) {
        System.out.println(findMaxDiff(new int[] {3,6,9,1}));
    }
}
