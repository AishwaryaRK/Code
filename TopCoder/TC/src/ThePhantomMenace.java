import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class ThePhantomMenace {

	public static void main(String[] args) {
		int[] doors = {1,2,3,4};
		int[] droids = {5,6,7,8};
		System.out.println(find(doors, droids));
	}

	public static int find(int[] doors, int[] droids) {
		List<Integer> safestDistances = new ArrayList<Integer>();
		for (int i = 0; i < doors.length; i++) {
			int safestDistance = Math.abs(doors[i] - droids[0]);
			for (int j = 1; j < droids.length; j++) {
				if (Math.abs(doors[i] - droids[j]) < safestDistance) {
					safestDistance = Math.abs(doors[i] - droids[j]);
				}
			}
			safestDistances.add(safestDistance);
		}
		return Collections.max(safestDistances);
	}

}
