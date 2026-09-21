package Tier_3;

import java.util.HashSet;

public class LongestSubstringWithoutRepeatingCharacters {
    static String longestSubStr(String str) {
        int left = 0;
        int maxLen = 0;

        HashSet<Character> set = new HashSet<>();

        for (int right = 0; right < str.length(); right++) {
            while (set.contains(str.charAt(right))) {
                set.remove(str.charAt(right));
                left++;
            }

            set.add(str.charAt(right));

            maxLen = Math.max(maxLen, right - left + 1);
        }

        return set.toString();
    }
    public static void main(String[] args) {
        System.out.println(longestSubStr("abcabcbb"));
    }
}
