
public class TheArithmeticProgression {

	public static void main(String[] args) {
		System.out.println(minimumChange(0, 2, 1));
	}

	public static double minimumChange(int a, int b, int c) {
		double mid = (a + c) / 2.0;
		return Math.abs(b - mid);
	}
}
