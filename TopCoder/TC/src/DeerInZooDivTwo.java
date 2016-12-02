
public class DeerInZooDivTwo {

	public static void main(String[] args) {
		int[] ans = getminmax(3, 2);
		System.out.println(ans[0]+", "+ans[1]);
	}

	public static int[] getminmax(int N, int K) {
		int minDeers =  N > K ? N - K : 0;
		int maxDeers = N - (K / 2 + K % 2);
		int[] ans = { minDeers, maxDeers };
		return ans;
	}
}
