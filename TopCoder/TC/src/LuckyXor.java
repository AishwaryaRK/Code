
public class LuckyXor {

	public static void main(String[] args) {
		System.out.println(construct(4));
	}

	public static int construct(int a) {
		for (int i = a + 1; i <= 100; i++) {
			int result = a ^ i;
			if (isLucky(result)) {
				return i;
			}
		}
		return -1;
	}

	private static boolean isLucky(int result) {
		for (char digit : (result + "").toCharArray()) {
			if (digit != '4' && digit != '7') {
				return false;
			}
		}
		return true;
	}

}
