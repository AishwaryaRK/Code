import java.io.*;

public class CandidateCode {

	public static void main(String[] args) {
		System.out.println(passCount(5, 3, 2));
	}

	public static int passCount(int N, int M, int L) {
		int count = 0;
		int[] passReceivedCountOfPlayers = new int[N + 1];
		passReceivedCountOfPlayers[1] = 1;
		for (int i = 2; i <= N; i++) {
			passReceivedCountOfPlayers[i] = 0;
		}
		int currentPlayer = 1;
		int maxPassesReceived = 1;
		while (maxPassesReceived < M) {
			int p = passReceivedCountOfPlayers[currentPlayer];
			System.out.println("current player = " + currentPlayer);
			System.out.println("p = " + p);
			if (p >= M) {
				return count;
			}
			if (p % 2 == 0) {
				currentPlayer = (currentPlayer + L) % N == 0 ? N : (currentPlayer + L) % N;

				System.out.println("even currentPLayer=" + currentPlayer);
				passReceivedCountOfPlayers[currentPlayer]++;
				count++;
			} else {
				currentPlayer = (currentPlayer - L) % N <= 0 ? N + (currentPlayer - L) % N : (currentPlayer - L) % N;
				System.out.println("odd currentPLayer=" + currentPlayer);

				passReceivedCountOfPlayers[currentPlayer]++;
				count++;
			}
		}
		return -1;
	}
}