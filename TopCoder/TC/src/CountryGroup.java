
public class CountryGroup {

	public static void main(String[] args) {
		int[] a = { 2, 2, 3, 3, 3 };
		System.out.println(solve(a));
	}

	public static int solve(int[] a) {
		int numberOfCountries = 0;
		for (int i = 0; i < a.length; i++) {
			int pivotValue = a[i];
			int j = i + 1;
			for (; j < a.length && j <= i + pivotValue - 1; j++) {
				if (a[i] != pivotValue) {
					return -1;
				}
			}
			if (j <= i + pivotValue - 1 && i >= a.length) {
				return -1;
			}
			numberOfCountries++;
			i = j - 1;
		}
		return numberOfCountries;
	}

}
