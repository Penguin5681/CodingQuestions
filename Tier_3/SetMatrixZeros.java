package Tier_3;

public class SetMatrixZeros {
    static void printMatrix(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }

    static void setMatrixZeros(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        
        boolean[] rowZeros = new boolean[rows];
        boolean[] colZeros = new boolean[cols];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (matrix[i][j] == 0) {
                    rowZeros[i] = true;
                    colZeros[j] = true;
                }
            }
        }

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (rowZeros[i] == true || colZeros[j] == true) {
                    matrix[i][j] = 0;
                }
            }
        }

        printMatrix(matrix);
        
    }

    public static void main(String[] args) {
        System.out.println("Test Case 1:");
        setMatrixZeros(new int[][] {{1, 1, 1}, {1, 0, 1}, {1, 1, 1}});
        
        System.out.println("\nTest Case 2:");
        setMatrixZeros(new int[][] {{0, 1, 2, 0}, {3, 4, 5, 2}, {1, 3, 1, 5}});
        
        System.out.println("\nTest Case 3:");
        setMatrixZeros(new int[][] {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}});
        
        System.out.println("\nTest Case 4:");
        setMatrixZeros(new int[][] {{0}});
        
        System.out.println("\nTest Case 5:");
        setMatrixZeros(new int[][] {{1, 2}, {3, 4}});
    }
}
