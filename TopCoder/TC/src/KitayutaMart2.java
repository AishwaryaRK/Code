
public class KitayutaMart2 {

	public static void main(String[] args) {
		System.out.println(numBought(100, 100));
	}

	public static int numBought(int K, int T) {
		return (int)(Math.log(T / K + 1) / Math.log(2));
	}

}
