import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Coursera {

	public static void main(String[] args) throws IOException {
		BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
		long launch_date = Long.parseLong(bufferedReader.readLine());
		long enrollment_date = Long.parseLong(bufferedReader.readLine());
		long[] ans = getUpcomingSessions(launch_date, 2, enrollment_date);
		for (int i = 0; i < ans.length; i++) {
			System.out.println(ans[i]);
		}
	}

	private static long[] getUpcomingSessions(long launch_date, int repeat_frequency, long enrollment_date) {
		int numberOfSessions = 3;
		int minRepeatFrequency = 1;
		long[] upcomingSessions = new long[numberOfSessions];
		Date launchDate = new Date(launch_date);
		Date session = getStartSession(launchDate);
		Date enrollmentDate = new Date(enrollment_date);
		if (repeat_frequency == 0) {
			repeat_frequency = minRepeatFrequency;
		}
		if (enrollmentDate.after(session)) {
			session = getNextSession(session, repeat_frequency);
		}
		for (int i = 0; i < numberOfSessions; i++) {
			upcomingSessions[i] = session.getTime();
			session = getNextSession(session, repeat_frequency);
		}
		return upcomingSessions;
	}

	private static Date getNextSession(Date date, int repeat_frequency) {
		int daysToIncrement = repeat_frequency * 7;
		return addDays(date, daysToIncrement);
	}

	private static Date getStartSession(Date date) {
		int daysToIncrement = (8 - date.getDay()) % 7;
		return addDays(date, daysToIncrement);
	}

	private static Date addDays(Date date, long daysToIncrementForNextSession) {
		return new Date(date.getTime() + (daysToIncrementForNextSession * 24 * 60 * 60 * 1000));
	}

}
