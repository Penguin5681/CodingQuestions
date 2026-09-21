package Tier_2;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class MergeTwoSortedArrays {
    static void merge(int[] arr1, int[] arr2) {
        int[] newArr = new int[arr1.length + arr2.length];

        List<Integer> list = new ArrayList<>();

        for (int i = 0; i < arr1.length; i++) {
            list.add(arr1[i]);
        }

        for (int i = 0  ; i < arr1.length; i++) {
            list.add(arr2[i]);
        }

        Collections.sort(list);

        System.out.println(list.toString());
    }   
    public static void main(String[] args) {
        merge(new int[] {1, 2, 3, 4, 5}, new int[] {2, 4, 6, 8, 10});
    }
}
