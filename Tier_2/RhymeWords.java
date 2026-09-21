package Tier_2;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class RhymeWords {
    static void findRhymingWords(String[] words, int rhymeLength) {
        Map<String, List<String>> map = new HashMap<>();

        for (String word : words) {
            word = word.toLowerCase();
            if (word.length() < rhymeLength) {
                continue;
            }

            String suffix = word.substring(word.length() - rhymeLength);
            map.computeIfAbsent(suffix, key -> new ArrayList<>()).add(word);
        }

        for (Map.Entry<String, List<String>> entry : map.entrySet()) {
            List<String> rhymStrings = entry.getValue();

            if (rhymStrings.size() >= 2) {
                System.out.println(rhymStrings);
            }
        }
    }
    public static void main(String[] args) {
        // Matching three-letter suffixes.
        findRhymingWords(new String[]{"cat", "bat", "hat", "dog", "fog"}, 3);

        // Case-insensitive matching.
        findRhymingWords(new String[]{"Light", "night", "MIGHT", "day"}, 3);

        // Words shorter than rhymeLength are ignored.
        findRhymingWords(new String[]{"a", "an", "ant", "plant", "slant"}, 3);

        // No repeated suffixes.
        findRhymingWords(new String[]{"apple", "orange", "banana"}, 2);
    }
}
