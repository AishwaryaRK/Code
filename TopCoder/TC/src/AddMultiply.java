
public class AddMultiply {

	public static void main(String[] args) {
		int[] x = makeExpression(6);
		for (int i = 0; i < x.length; i++) {
			System.out.print(x[i] + ",");
		}
	}

	public static int[] makeExpression(int y) {
		int[] x = { 2, -2, y + 4 };
		return x;
	}
}
