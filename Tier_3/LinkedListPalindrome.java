package Tier_3;

import java.util.Arrays;
import java.util.LinkedList;

public class LinkedListPalindrome {
    static boolean isPalindrome(LinkedList<Integer> list) {
        if (list.size() < 2) {
            return false;
        }

        for (int i = 0; i < list.size(); i++) {
            if (list.getFirst() != list.getLast()) {
                return false;
            }
            list.removeFirst();
            list.removeLast();
        }
        return true;
    }
    public static void main(String[] args) {
        // Test case 1: Palindrome list [1, 2, 2, 1]
        LinkedList<Integer> list1 = new LinkedList<>();
        list1.add(1);
        list1.add(2);
        list1.add(2);
        list1.add(1);
        System.out.println("Test 1 - [1, 2, 2, 1]: " + isPalindrome(list1));
            // Test case 2: Non-palindrome list [1, 2, 3, 4]
        LinkedList<Integer> list2 = new LinkedList<>();
        list2.add(1);
        list2.add(2);
        list2.add(3);
        list2.add(4);
        System.out.println("Test 2 - [1, 2, 3, 4]: " + isPalindrome(list2));
        
        // Test case 3: Single element [5]
        LinkedList<Integer> list3 = new LinkedList<>();
        list3.add(5);
        System.out.println("Test 3 - [5]: " + isPalindrome(list3));
        
        // Test case 4: Odd-length palindrome [1, 2, 3, 2, 1]
        LinkedList<Integer> list4 = new LinkedList<>();
        list4.add(1);
        list4.add(2);
        list4.add(3);
        list4.add(2);
        list4.add(1);
        System.out.println("Test 4 - [1, 2, 3, 2, 1]: " + isPalindrome(list4));
    }
}
