import java.util.Scanner;

public class Hiss {

	public static void main(String[] args) {
		Scanner console = new Scanner(System.in);

		if (console.nextLine().contains("ss")) {
			System.out.println("hiss");
		} else {
			System.out.println("no hiss");
		}
	}
}