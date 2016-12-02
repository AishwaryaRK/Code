
public class MultiplicationTable2Easy {

	public static void main(String[] args) {
		int[] table = { 1, 1, 2, 3, 1, 0, 2, 3, 3, 3, 0, 3, 2, 2, 2, 0 };
		int[] t = { 2, 3 };
		System.out.println(isGoodSet(table, t));
	}

	public static String isGoodSet(int[] table, int[] t) {
		int n = getN(table) + 1;
		for (int i = 0; i < t.length; i++) {
			for (int j = 0; j < t.length; j++) {
				int a = t[i];
				int b = t[j];
				int ans = table[a * n + b];
				if (!contains(t, ans)) {
					return "Not Good";
				}
			}
		}
		return "Good";
	}

	public static int getN(int[] table) {
		int n = 0;
		for (int i = 0; i < table.length; i++) {
			if (table[i] > n) {
				n = table[i];
			}
		}
		return n;
	}

	public static boolean contains(int[] t, int ans) {
		for (int i = 0; i < t.length; i++) {
			if (t[i] == ans) {
				return true;
			}
		}
		return false;
	}
}
