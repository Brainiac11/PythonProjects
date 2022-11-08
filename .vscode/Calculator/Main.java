import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        System.out.println("Calculator");
        System.out.println("1. Add");
        System.out.println("2. Subtract");
        System.out.println("3. Multiply");
        System.out.println("4. Divide");
        System.out.println("5. Exit");
        System.out.println("Enter your choice: ");
        try (Scanner choice = new Scanner(System.in)) {
            double ch = choice.nextInt();
            if(ch == 1){
                System.out.println("Enter two numbers: ");
                Scanner num = new Scanner(System.in);
                double a = num.nextDouble();
                double b = num.nextDouble();
                double sum = a + b;
                System.out.println("Sum = " + sum);
            }
            else if(ch == 2){
                System.out.println("Enter two numbers: ");
                Scanner num = new Scanner(System.in);
                double a = num.nextDouble();
                double b = num.nextDouble();
                double diff = a - b;
                System.out.println("Difference = " + diff);
            }
            else if(ch == 3){
                System.out.println("Enter two numbers: ");
                Scanner num = new Scanner(System.in);
                double a = num.nextDouble();
                double b = num.nextDouble();
                double prod = a * b;
                System.out.println("Product = " + prod);
            }
            else if(ch == 4){
                System.out.println("Enter two numbers: ");
                Scanner num = new Scanner(System.in);
                double a = num.nextDouble();
                double b = num.nextDouble();
                double div = a / b;
                System.out.println("Quotient = " + div);
            }
            else if(ch == 5){
                System.out.println("Exiting...");
            }
            else{
                System.out.println("Invalid choice");
            }
            
        }
    }
}
