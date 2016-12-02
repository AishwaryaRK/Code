
public class PeacefulLine {

	public static void main(String[] args) {
		int[] x = { 1, 1, 1, 2 };
		System.out.println(makeLine(x));
	}

	public static String makeLine(int[] x) {
		int threshold = x.length % 2 == 0 ? x.length / 2 : x.length / 2 + 1;
		System.out.println(threshold);
		int[] count = new int[26];
		for (int i = 1; i <= 25; i++) {
			count[i] = 0;
		}
		for (int i = 0; i < x.length; i++) {
			count[x[i]]++;
			if (count[x[i]] > threshold) {
				return "impossible";
			}
		}
		return "possible";
	}
}
