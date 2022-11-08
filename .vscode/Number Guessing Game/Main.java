import java.util.Random;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        System.out.println("Welcome to the Number Guessing Game!");
        System.out.println("I'm thinking of a number between 1 and 10.");
        double rightNumber = new Random().nextInt(10) + 1;
        try (Scanner scanner = new Scanner(System.in)) {
            int guess = 0;
            int tries = 0;
            while (guess != rightNumber) {
                System.out.print("Enter your guess: ");
                guess = scanner.nextInt();
                tries++;
                if (guess > rightNumber) {
                    System.out.println("Your guess is too high.");
                } 
                else if (guess < rightNumber) {
                     System.out.println("Your guess is too low.");
                }
                else {
                    System.out.println("You got it! The number was " + rightNumber + ".");
                    System.out.println("It took you " + tries + " tries.");
                }
                
                
            }
        }
    }
}
