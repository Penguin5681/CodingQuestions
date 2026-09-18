package Tier_1;

import java.util.HashMap;
import java.util.Map;

public class CountOccurences {
    static void countOccurences(int[] arr) {
        HashMap<Integer, Integer> mp = new HashMap<>();
        for (int num : arr) {
            mp.put(num, mp.getOrDefault(num, 0) + 1);
        }

        for (Map.Entry<Integer, Integer> entry : mp.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }

    public static void main(String[] args) {
        countOccurences(new int[] { 1, 2, 2, 2, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1 });
    }
}
