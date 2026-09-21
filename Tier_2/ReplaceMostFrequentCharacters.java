package Tier_2;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

public class ReplaceMostFrequentCharacters {
    static String replaceChars(String string, char replacement, int k) {
        HashMap<Character, Integer> frequencies = new HashMap<>();

        for (char ch : string.toCharArray()) {
            frequencies.put(ch, frequencies.getOrDefault(ch, 0) + 1);
        }

        Set<Character> charactersToReplace = new HashSet<>();

        for (int i = 0; i < k && charactersToReplace.size() < frequencies.size(); i++) {
            char mostFrequent = '\0';
            int highestFrequency = 0;

            for (char ch : frequencies.keySet()) {
                if (!charactersToReplace.contains(ch)
                        && frequencies.get(ch) > highestFrequency) {
                    mostFrequent = ch;
                    highestFrequency = frequencies.get(ch);
                }
            }

            charactersToReplace.add(mostFrequent);
        }

        StringBuilder result = new StringBuilder();

        for (char ch : string.toCharArray()) {
            if (charactersToReplace.contains(ch)) {
                result.append(replacement);
            } else {
                result.append(ch);
            }
        }

        return result.toString();
    }

    public static void main(String[] args) {

    }
}
