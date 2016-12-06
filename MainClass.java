import java.util.Stack;

// DESCRIPTION: Brute force approach to the subset sum problem.
// There could be an exponential number of subsets, and this method attempts to search
// for all of them. Meaning this algorithm is inefficient and exponential time is likely.

public class MainClass {

	public static void main(String[] args) {

		int[] arr = { 10, 34, 19, 27 };
		int sum = 56;
		findSubsets(arr, 0, sum, new Stack<Integer>());

	}

	private static void findSubsets(int[] arr, int start, int target, Stack<Integer> s) {

		// Base cases
		if (start == arr.length && target == 0) {
			System.out.printf("\nSUB SET FOUND: %s\n\n", s);
		}
		if (start == arr.length) {
			return;
		}
		System.out.println("checking value: " + arr[start] + " iteration: " + start);
		// check if the current element in the array is in the set
		// recurse twice to check if the element is in the set, or if it is not

		// check if the element is in the lit
		s.add(arr[start]);
		System.out.println(s);
		findSubsets(arr, start + 1, target - arr[start], s);

		// check if the element is not in the list
		s.pop();
		findSubsets(arr, start + 1, target, s);
	}
}