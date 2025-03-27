import java.util.Scanner;
public class exercisio03 {
    public static void main(String[] args) throws Exception {
        int n1;
        int n2;
        int n3;
        Scanner n1Scanner = new Scanner(System.in);
        System.out.println("primero numero:");
        n1 = n1Scanner.nextInt();
        System.out.println("egundo numero:");
        n2 = n1Scanner.nextInt();
        n3 = n1 + n2;
        System.out.println(n3);
        n1Scanner.close();
    }
}