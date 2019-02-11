import java.io.IOException;
import java.util.Date;

public class Coursera {

	public static void main(String[] args) throws IOException {
		long launch_date1 = Long.parseLong("1469923200000");
		long launch_date2 = Long.parseLong("1469923200000");
		long enrollment_date = Long.parseLong("1470268800000");
		long[][] specialization_courses = new long[2][3];
		specialization_courses[0][0] = launch_date1;
		specialization_courses[0][1] = 2;
		specialization_courses[0][2] = 4;
		specialization_courses[1][0] = launch_date2;
		specialization_courses[1][1] = 2;
		specialization_courses[1][2] = 4;

		long[][] ans = getSpecializationSessionSchedule(specialization_courses, enrollment_date);
		for (int i = 0; i < ans.length; i++) {
			System.out.println(ans[i][0] + ", " + ans[i][1]);
		}
	}

	static long[][] getSpecializationSessionSchedule(long[][] specialization_courses, long enrollment_date) {
		long[][] specializationSessionSchedule = new long[specialization_courses.length][2];
		Date enrollmentDate = new Date(enrollment_date);
		Date launchDate;
		Date endDate;
		Date session = null;
		for (int i = 0; i < specialization_courses.length; i++) {
			launchDate = new Date(specialization_courses[i][0]);
			if (session == null || launchDate.after(session)) {
				session = getStartSession(launchDate);
			}
			int repeat_frequency = (int) specialization_courses[i][1];
			if (enrollmentDate.after(session)) {
				session = getNextSession(session, repeat_frequency);
			}
			specializationSessionSchedule[i][0] = session.getTime();
			long duration = specialization_courses[i][2];
			endDate = getEndDate(session, duration);
			specializationSessionSchedule[i][1] = endDate.getTime();
			session = endDate;
		}
		return specializationSessionSchedule;
	}

	private static Date getNextSession(Date date, int repeat_frequency) {
		int daysToIncrement = repeat_frequency * 7;
		return addDays(date, daysToIncrement);
	}

	private static Date getStartSession(Date date) {
		int daysToIncrement = (8 - date.getDay()) % 7;
		return addDays(date, daysToIncrement);
	}

	private static Date getEndDate(Date date, long duration) {
		long daysToIncrement = duration * 7;
		return addDays(date, daysToIncrement);
	}

	private static Date addDays(Date date, long daysToIncrement) {
		return new Date(date.getTime() + (daysToIncrement * 24 * 60 * 60 * 1000));
	}

}
