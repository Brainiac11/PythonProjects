import java.util.Scanner;
public class Main {
    String name;
    int age;
    double height;
    boolean isAlive;
    char averageGrade;
    public Main(String nameOfPerson, int ageOfPerson, double heightOfPerson, boolean isAliveOfPerson, char averageGradeOfPerson) {
        name = nameOfPerson;
        age = ageOfPerson;
        height = heightOfPerson;
        isAlive = isAliveOfPerson;
        averageGrade = averageGradeOfPerson;
    }
    public String keyOfPerson() {
        String key = "";
        String strAge = Integer.toString(age);
        String strHeight = Double.toString(height);
        String strAverageGrade = Character.toString(averageGrade);
        key = key.concat(name);
        key = key.concat(strAge + strAverageGrade);
        key = key.concat(strHeight);
        if (isAlive) {
            key = key.concat("Alive");
        } else {
            key = key.concat("Dead");
        }
        return key;
    }
    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in);
        System.out.println("Enter the name of the person: ");
        String nameOfPerson = myObj.nextLine();
        System.out.println("Enter the age of the person: ");
        int ageOfPerson = myObj.nextInt();
        System.out.println("Enter the height of the person: ");
        double heightOfPerson = myObj.nextDouble();
        System.out.println("Is the person alive? (true/false): ");
        boolean isAliveOfPerson = myObj.nextBoolean();
        System.out.println("Enter the average grade of the person: ");
        char averageGradeOfPerson = myObj.next().charAt(0);
        Main name = new Main(nameOfPerson, ageOfPerson, heightOfPerson, isAliveOfPerson, averageGradeOfPerson);
        System.out.println("The person's unique key is: " + name.keyOfPerson());
    }
    
}
