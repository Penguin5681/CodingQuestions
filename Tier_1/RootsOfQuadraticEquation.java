package Tier_1;

public class RootsOfQuadraticEquation {

    static void getRoots(double a, double b, double c) {
        String equation = String.format("%.2fx^2 %s %.2fx %s %.2f = 0",
            a, b >= 0 ? "+" : "-", Math.abs(b),
            c >= 0 ? "+" : "-", Math.abs(c));
        System.out.println("Given Equation: " + equation);

        if (a == 0) {
            if (b == 0) {
                System.out.println(c == 0 ? "Infinitely many solutions" : "No solution");
            } else {
                System.out.println("Root: " + (-c / b));
            }
            return;
        }

        double discriminant = b * b - 4 * a * c;

        if (discriminant < 0) {
            double real = -b / (2 * a);
            double imag = Math.sqrt(-discriminant) / (2 * a);
            System.out.println("Root 1: " + formatComplex(real, imag));
            System.out.println("Root 2: " + formatComplex(real, -imag));
            return;
        }

        double squareRoot = Math.sqrt(discriminant);

        if (discriminant == 0) {
            double root = -b / (2 * a);
            System.out.println("Root (repeated): " + root);
            return;
        }

        // Numerically stable form: avoid cancellation when b and sqrt(disc)
        // are close in magnitude.
        double q = (b >= 0) ? -0.5 * (b + squareRoot) : -0.5 * (b - squareRoot);
        double root1 = q / a;
        double root2 = c / q;

        System.out.println("Root 1: " + root1);
        System.out.println("Root 2: " + root2);
    }

    private static String formatComplex(double real, double imag) {
        String sign = imag >= 0 ? "+" : "-";
        return String.format("%.4f %s %.4fi", real, sign, Math.abs(imag));
    }

    public static void main(String[] args) {
        getRoots(4, -5, 12);   // complex roots: 0.6250 ± 1.6960i
        getRoots(1, -3, 2);    // real roots 1, 2
        getRoots(1, 2, 1);     // repeated root -1
        getRoots(0, 2, -4);    // linear
        getRoots(0, 0, 0);     // infinite
        getRoots(0, 0, 5);     // no solution
    }
}
