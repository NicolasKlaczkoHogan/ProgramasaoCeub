import java.util.Scanner;
public class exercisio02 {
    public static void main(String[] args) throws Exception {
        String altura;
        String idade;
        String peso;
        String nome;
        Scanner alturaScanner = new Scanner(System.in);
        System.out.println("qual sua altura:");
        altura = alturaScanner.nextLine();
        Scanner idadeScanner = new Scanner(System.in);
        System.out.println("qual sua idae:");
        idade = idadeScanner.nextLine();
        Scanner pesoScanner = new Scanner(System.in);
        System.out.println("qual seu peso:");
        peso = pesoScanner.nextLine();
        Scanner nomeScanner = new Scanner(System.in);
        System.out.println("qual seu nome:");
        nome = nomeScanner.nextLine();
        

        System.out.println("sou " + nome + " tenho " + idade + " anos tenho " + altura + " de altura e peso " + peso);
        alturaScanner.close();
        pesoScanner.close();
        idadeScanner.close();
        nomeScanner.close();
    

    }
}
