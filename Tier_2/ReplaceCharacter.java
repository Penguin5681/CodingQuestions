package Tier_2;

/**
 * ReplaceCharacter
 */
public class ReplaceCharacter {
    static String replaceCharacters(String string, char replace, char replaceWith) {
        char[] arr = string.toCharArray();

        for (int i = 0; i < string.length(); i++) {
            if (arr[i] == replace) {
                arr[i] = replaceWith;
            }
            else if (arr[i] == replaceWith) {
                arr[i] = replace;
            }
        }

        return new String(arr);
    }
    public static void main(String[] args) {
        System.out.println(replaceCharacters("apples", 'a', 'p'));       // ppales
        System.out.println(replaceCharacters("banana", 'a', 'o'));       // bonono
        System.out.println(replaceCharacters("hello", 'l', 'x'));        // hexxo
        System.out.println(replaceCharacters("mississippi", 's', 'p'));  // mi pp i pp i? 
        System.out.println(replaceCharacters("same", 'a', 'a'));         // same
        System.out.println(replaceCharacters("nothing", 'x', 'y'));      // nothing
        System.out.println(replaceCharacters("", 'a', 'b'));             // empty string
    }
}