package Tier_3;

public class RemoveAdj {
    static void removeAdjacentEqualChars(String string) {
        StringBuilder builder = new StringBuilder(string);

        for (int i = 0; i < builder.length() - 1;) {
            if (builder.charAt(i) == builder.charAt(i + 1)) {
                builder.delete(i, i + 2);
                i = Math.max(0, i - 1);
            } else {
                i++;
            }
        }

        System.out.println(builder.toString());
    }

    public static void main(String[] args) {
        System.out.println("Test 1: abbaca");
        removeAdjacentEqualChars("abbaca");
        
        System.out.println("\nTest 2: aa");
        removeAdjacentEqualChars("aa");
        
        System.out.println("\nTest 3: a");
        removeAdjacentEqualChars("a");
        
        System.out.println("\nTest 4: abcd");
        removeAdjacentEqualChars("abcd");
        
        System.out.println("\nTest 5: aabbcc");
        removeAdjacentEqualChars("aabbcc");
    }
    // abbaca => ca
    // aaca
    // ca
}
