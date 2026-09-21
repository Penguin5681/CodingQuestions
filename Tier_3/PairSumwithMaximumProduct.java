package Tier_3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class PairSumwithMaximumProduct {
    static String findPair(int[] arr, int target) {
        List<Integer> ans = new ArrayList<>();
        Arrays.sort(arr);

        int start = 0;
        int end = arr.length - 1;
        int maxProd = 0;
        while (start < end) {
            int currentSum = arr[start] + arr[end];

            if (currentSum == target) {
                int currentProduct = arr[start] * arr[end];
                if (currentProduct > maxProd) {
                    maxProd = currentProduct;
                    ans.add(arr[start]);
                    ans.add(arr[end]);
                }
                start++; end--;
            }

            else if (currentSum < target) {
                end--;
            } else {
                start++;
            }
        }

        return ans.toString();
    }
    public static void main(String[] args) {
        System.out.println(findPair(new int[] {11, 1, 2, 8, 10, 11, 15, 7}, 18));
    }
}
