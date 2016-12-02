
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class AngryProfessor {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bufferedReader.readLine());
		String[] s;
		for (int i = 0; i < n; i++) {
			s = bufferedReader.readLine().split(" ");
			int numberOfStudents = Integer.parseInt(s[0]);
			int threshold = Integer.parseInt(s[1]);
			s = bufferedReader.readLine().split(" ");
			int[] timings = new int[numberOfStudents];
			for (int j = 0; j < numberOfStudents; j++) {
				timings[j] = Integer.parseInt(s[j]);
			}
			System.out.println(isClassCancelled(timings, threshold));
		}
	}

	private static String isClassCancelled(int[] timings, int threshold) {
		int countOfStudentsInTime = 0;
		for (int i = 0; i < timings.length; i++) {
			if (timings[i] <= 0) {
				countOfStudentsInTime++;
			}
		}
		return countOfStudentsInTime >= threshold ? "NO" : "YES";
	}

}
