package Tier_2;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

public class IntersectionOfLists {
    static void intersect(int[] arr1, int[] arr2) {
        HashSet<Integer> set1 = new HashSet<>();
        for (int x : arr1) {
            set1.add(x);
        }

        List<Integer> ls = new ArrayList<>();

        for (int x : arr2) {
            if (set1.contains(x)) {
                ls.add(x);
                set1.remove(x);
            }
        }

        System.out.println(ls.toString());
    }
    public static void main(String[] args) {
        intersect(new int[] {1, 2, 3, 4, 5}, new int[] {2, 4, 6});
    }
}
