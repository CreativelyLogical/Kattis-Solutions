import java.util.Scanner;

public class TakeTwoStones {

	public static void main(String[] args) {
		Scanner console = new Scanner(System.in);

		if (console.nextInt() % 2 == 0) {
			System.out.println("Bob");
		} else {
			System.out.println("Alice");
		}
	}
}