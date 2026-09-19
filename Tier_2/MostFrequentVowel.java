package Tier_2;

import java.util.HashMap;
import java.util.Map;

public class MostFrequentVowel {
    static char mostFrequentVowel(String str) {
        HashMap<Character, Integer> mp = new HashMap<>();

        for (char ch : str.toCharArray()) {
            mp.put(ch, mp.getOrDefault(ch, 0) + 1);
        }

        int max = -1;
        char mostFreq = '\0';

        for (Map.Entry<Character, Integer> entry : mp.entrySet()) {
            char ch = entry.getKey();
            int curr = entry.getValue();
            if (curr > max && "aeiouAEIOU".indexOf(ch) != -1) {
                max = curr;
                mostFreq = ch;
            }
        }

        return mostFreq;
    }
    public static void main(String[] args) {
        System.out.println(mostFrequentVowel("hello world"));
        System.out.println(mostFrequentVowel("xyuaab"));
        System.out.println(mostFrequentVowel("beautiful"));
        System.out.println(mostFrequentVowel("xyz"));
    }
}
