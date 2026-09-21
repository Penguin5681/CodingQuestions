package Tier_2;

public class PasswordChecker {
    static boolean isValidPassword(String passwordString) {
        return passwordString != null
                && passwordString.matches("(?=[^0-9])(?=.*[0-9])(?=.*[A-Z])[^\\s/]{4,}");
    }

    public static void main(String[] args) {
        test("Abcd1", true);
        test("abcde1", false);
        test("Abcde", false);
        test("A1b", false);
        test("1Abcd", false);
        test("Ab cd1", false);
        test("Ab/cd1", false);
        test(null, false);
        test("Z9xy", true);
        test("Password123", true);
        test("A1!x", true);
        test("abcd1E", true);
        test("Abc1", true);
        test("Ab1", false);
        test("Abcdef", false);
        test("abcdef1", false);
        test("1234Ab", false);
        test("Ab\tcd1", false);
        test("Ab\ncd1", false);
        test("Ab-cd1", true);
        test("Ab_cd1", true);
        test("ABCD1234", true);
        test("Abcd!", false);
    }

    private static void test(String password, boolean expected) {
        boolean actual = isValidPassword(password);
        if (actual != expected) {
            throw new AssertionError("Unexpected result for password: " + password);
        }
    }
}
