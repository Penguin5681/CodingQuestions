package Tier_2;

import java.util.Arrays;

public class IsAnagram {
    static boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        char[] char_s = s.toCharArray();
        char[] char_t = t.toCharArray();

        Arrays.sort(char_s);
        Arrays.sort(char_t);

        return new String(char_s).equals(new String(char_t));
    }
    public static void main(String[] args) {
        System.out.println(isAnagram("listen", "silent")); // true
        System.out.println(isAnagram("anagram", "nagaram")); // true
        System.out.println(isAnagram("rat", "car")); // false
        System.out.println(isAnagram("a", "ab")); // false
        System.out.println(isAnagram("", "")); // true
    }
}
