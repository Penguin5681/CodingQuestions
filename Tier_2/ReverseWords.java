package Tier_2;

public class ReverseWords {
    static void reverseWords(String sentence) {
        String[] words = sentence.trim().split(" ");
        StringBuilder stringBuilder = new StringBuilder("");

        for (int i = words.length - 1; i >= 0; i--) {
            stringBuilder.append(words[i] + " ");
        }

        System.out.println(stringBuilder.toString().trim());
    }

    static void main(String[] args) {
        reverseWords("Hello World!");
    }
}
