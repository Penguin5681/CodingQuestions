package Tier_1;

import java.util.Arrays;

public class MaxInArray {
    static void maxInArray(int[] arr) {
        int currentMax = arr[0];
        int indexMax = 0;
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > currentMax) {
                currentMax = arr[i];
                indexMax = i;
            }
        }

        System.out.println(currentMax);
        System.out.println(indexMax);
    }
    public static void main(String[] args) {
        int[] arr1 = {23, 45, 82, 27, 66, 12, 78, 13, 71, 86};
        System.out.println("Test case 1:");
        maxInArray(arr1);
        
        int[] arr2 = {-5, -1, -10};
        System.out.println("Test case 2:");
        maxInArray(arr2);
        
        int[] arr3 = {4, 4, 2};
        System.out.println("Test case 3:");
        maxInArray(arr3);
    }
}
