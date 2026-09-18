package Tier_1;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

public class RemoveDuplicates {
    static void removeDuplicates(int[] arr) {
        HashSet<Integer> set = new HashSet<>();
        for (int num : arr) {
            set.add(num);
        }

        for (int num : set) {
            System.out.print(num + " ");
        }
    }
    public static void main(String[] args) {
        removeDuplicates(new int[] {1, 1, 2, 3, 3, 4, 5, 6});
    }
}
