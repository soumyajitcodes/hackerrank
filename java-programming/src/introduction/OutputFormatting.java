package introduction;

import java.util.Scanner;

public class OutputFormatting {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("================================");
        for (int i = 0; i < 3; i++) {
            String s1 = sc.next();
            int x = sc.nextInt();
            //Complete this line
            String number = String.format("%03d", x);

            String spaces = "";
            for (int j = 1; j <= (15 - s1.length()); j++)
                spaces = spaces + " ";

            System.out.println(s1 + spaces + number);
        }
        System.out.println("================================");

    }
}
