import java.util.Scanner;
import java.util.Random;

public class MagicSquareGame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter Odd Number For Magic Square: ");
        int inputNumber = scanner.nextInt();

        if (inputNumber % 2 == 0) {
            System.out.println("Please enter a valid Odd Number");
            System.exit(0);
        }

        int[][] magicSquare = createSquare(inputNumber);

        int shuffleCount = 2;
        for (int i = 0; i < shuffleCount; i++) {
            magicSquare = shuffleSquare(magicSquare);
        }

        playGame(magicSquare);
    }

    // Method for creating square
    public static int[][] createSquare(int inputNumber) {
        int[][] square = new int[inputNumber][inputNumber];
        int x = 0, y = inputNumber / 2;
        square[x][y] = 1;

        for (int i = 2; i <= inputNumber * inputNumber; i++) { // Loop fills square with remaining numbers
            // Staying in valid range of array
            int newX = (x - 1 + inputNumber) % inputNumber;
            int newY = (y - 1 + inputNumber) % inputNumber;

            if (square[newX][newY] != 0) {
                x = (x + 1) % inputNumber;
            } else {
                x = newX;
                y = newY;
            }

            square[x][y] = i;
        }

        return square; // Return completed square
    }

    public static void displaySquare(int[][] square) { // Method for Displaying numbers array in a square format
        int inputNumber = square.length;
        for (int i = 0; i < inputNumber; i++) {
            for (int k = 0; k < inputNumber; k++) {
                System.out.print(square[i][k] + " "); // Prints out 2d array of numbers one line at a time
            }
            System.out.println(); // Makes it print out numbers on new line to make it look like a square
        }
    }

    public static int[][] shuffleSquare(int[][] square) {
        int size = square.length;
        Random random = new Random();

        // Randomly select two elements and swap them
        int row1 = random.nextInt(size);
        int col1 = random.nextInt(size);
        int row2 = random.nextInt(size);
        int col2 = random.nextInt(size);

        int temp = square[row1][col1];
        square[row1][col1] = square[row2][col2];
        square[row2][col2] = temp;

        return square;
    }

    public static void playGame(int[][] magicSquare) {
        Scanner scanner = new Scanner(System.in);
        int size = magicSquare.length;
        int moves = 0; // Counts how many moves the player makes

        while (true) {
            displaySquare(magicSquare);
            System.out.print("Enter the move (e.g., '2 1 D'): ");
            String input = scanner.nextLine().toUpperCase();
            String[] parts = input.split(" "); // Seperates the input by spaces and creates an array of the input

            if (parts.length != 3) {
                System.out.println("Invalid input format. Please try again.");
                continue;
            } // checks to see if the input is valid e.g. follows the format 3 1 u

            int row = Integer.parseInt(parts[0]) - 1;
            int col = Integer.parseInt(parts[1]) - 1; // subtracting 1 to use it for indexs
            String direction = parts[2]; // extracting direction of move

            if (row < 0 || row >= size || col < 0 || col >= size) { // error catch if player puts in too big/little
                                                                    // input
                System.out.println("Invalid row or column. Please try again.");
                continue;
            }

            if (direction.equals("U")) { // if statement to figure out which method to use for direction
                magicSquare = swapUp(magicSquare, row, col);
            } else if (direction.equals("D")) {
                magicSquare = swapDown(magicSquare, row, col);
            } else if (direction.equals("L")) {
                magicSquare = swapLeft(magicSquare, row, col);
            } else if (direction.equals("R")) {
                magicSquare = swapRight(magicSquare, row, col);
            } else {
                System.out.println("Invalid direction. Please try again."); // error catch if direction is not valid
                                                                            // choice
                continue;
            }

            moves++; // increments how many moves the player has done

            if (isMagicSquare(magicSquare)) { // method call for win condition
                System.out.println("Congratulations! You solved the magic square in " + moves + " moves.");
                break;
            }
        }
    }

    // The following methods are for directions and changes the square depending on
    // the direction

    public static int[][] swapUp(int[][] square, int row, int col) {
        int size = square.length;
        int[][] newSquare = new int[size][size];

        for (int i = 0; i < size; i++) {
            for (int k = 0; k < size; k++) {
                newSquare[i][k] = square[i][k];
            }
        }

        if (row > 0) { // Avoids going out of bounds
            int temp = newSquare[row][col];
            newSquare[row][col] = newSquare[row - 1][col];
            newSquare[row - 1][col] = temp;
        }

        return newSquare;
    }

    public static int[][] swapDown(int[][] square, int row, int col) {
        int size = square.length;
        int[][] newSquare = new int[size][size];

        for (int i = 0; i < size; i++) {
            for (int k = 0; k < size; k++) {
                newSquare[i][k] = square[i][k];
            }
        }

        if (row < size - 1) { // Avoid going out of bounds
            int temp = newSquare[row][col];
            newSquare[row][col] = newSquare[row + 1][col];
            newSquare[row + 1][col] = temp;
        }

        return newSquare;
    }

    public static int[][] swapLeft(int[][] square, int row, int col) {
        int size = square.length;
        int[][] newSquare = new int[size][size];

        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                newSquare[i][j] = square[i][j];
            }
        }

        if (col > 0) { // Avoids going out of bounds
            int temp = newSquare[row][col];
            newSquare[row][col] = newSquare[row][col - 1];
            newSquare[row][col - 1] = temp;
        }

        return newSquare;
    }

    public static int[][] swapRight(int[][] square, int row, int col) {
        int size = square.length;
        int[][] newSquare = new int[size][size];

        for (int i = 0; i < size; i++) {
            for (int k = 0; k < size; k++) {
                newSquare[i][k] = square[i][k];
            }
        }

        if (col < size - 1) { // Avoids going out of bound
            int temp = newSquare[row][col];
            newSquare[row][col] = newSquare[row][col + 1];
            newSquare[row][col + 1] = temp;
        }

        return newSquare;
    }

    // Method to check if the player has won the game e.g. the current magic square
    // matches the actual magic square

    public static boolean isMagicSquare(int[][] square) {
        int size = square.length;
        int magicSum = size * (size * size + 1) / 2;

        // Check rows
        for (int i = 0; i < size; i++) {
            int rowSum = 0;
            for (int j = 0; j < size; j++) {
                rowSum += square[i][j];
            }
            if (rowSum != magicSum) {
                return false;
            }
        }

        // Check the columns
        for (int j = 0; j < size; j++) {
            int colSum = 0;
            for (int i = 0; i < size; i++) {
                colSum += square[i][j];
            }
            if (colSum != magicSum) {
                return false;
            }
        }

        // Check the diagonals
        int diagonalSum1 = 0;
        int diagonalSum2 = 0;
        for (int i = 0; i < size; i++) {
            diagonalSum1 += square[i][i];
            diagonalSum2 += square[i][size - 1 - i];
        }
        if (diagonalSum1 != magicSum || diagonalSum2 != magicSum) {
            return false;
        }

        return true;
    }
}