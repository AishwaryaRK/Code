
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ServiceLane {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
		String[] s = bufferedReader.readLine().split(" ");
		int n = Integer.parseInt(s[0]);
		int t = Integer.parseInt(s[1]);
		s = bufferedReader.readLine().split(" ");
		int[] serviceLane = new int[n];
		for (int i = 0; i < n; i++) {
			serviceLane[i] = Integer.parseInt(s[i]);
		}
		for (int i = 0; i < t; i++) {
			s = bufferedReader.readLine().split(" ");
			int entry = Integer.parseInt(s[0]);
			int exit = Integer.parseInt(s[1]);
			System.out.println(getPassableVehicle(entry, exit, serviceLane));
		}
	}

	private static int getPassableVehicle(int entry, int exit, int[] serviceLane) {
		int passableVehicle = serviceLane[entry];
		for (int i = entry + 1; i <= exit; i++) {
			if (serviceLane[i] < passableVehicle) {
				passableVehicle = serviceLane[i];
			}
		}
		return passableVehicle;
	}

}
