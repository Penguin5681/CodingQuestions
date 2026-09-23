package Tier_3;

public class VowelPermutation {
    static int recursionHelper(int n) {
        if (n == 0 || n == 1) {
            return 1;
        }

        return n * recursionHelper(n - 1);
    }

    static int findArrangements(String string) {
        int consonantCount = 0;

        for (char ch : string.toCharArray()) {
            if ("AEIOUaeiou".indexOf(ch) != -1) {
                continue;
            } else consonantCount++;
        }
        
        return recursionHelper(consonantCount);
    }
    public static void main(String[] args) {
        System.out.println(findArrangements("ABC"));
    }
}
