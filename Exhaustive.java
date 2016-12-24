import java.util.Arrays;
import java.util.Stack;
import java.util.Random;

// DESCRIPTION: Brute force approach to the subset sum problem.
// There could be an exponential number of subsets, and this method attempts to search
// for all of them. Meaning this algorithm is inefficient and exponential time is likely.

public class Exhaustive {

	public static void main(String[] args) {
                
                //length of test; run the test ___ times
                int lenTest = 5;
                //array containing test execution time results
                long[] arrTest = new long[lenTest];
                //average variable
                long avgTest = 0;
                //sum of array
                long sumTest = 0;
                
                //test loop
                for (int i = 0; i < lenTest; i++)
                {
                    Random r = new Random();
                    //change length here ↓
                    int[] set = new int[5];
                    int length = set.length;

                    //smallest element in the array
                    int min = 0;
                    //largest element in the array
                    int max = 10;
                    //populating the set array
                    for (int j=0; j < length; j++)
                    {
                        set[j] = (int) (r.nextInt(max - min + 1) + min);
                    }
                    System.out.println("Array: " + Arrays.toString(set));
                    //randomly generate target in range of min to max
                    int sum = r.nextInt(max - min + 1) + min;
                    System.out.println("Target: " + sum);

                    long startT = System.nanoTime();
                    findSubsets(set, 0, sum, new Stack<Integer>());
                    long endT = System.nanoTime();
                    long duration = (endT - startT);
                    //System.out.println(duration + " nanoseconds");
                    arrTest[i] = duration;
                }
                
                //sum loop
                for (long num : arrTest)
                {
                    sumTest = sumTest + num;
                }

                //averaging the results
                avgTest = sumTest / lenTest;
                System.out.println("Average time to complete " + lenTest + " algorithm runs: " + avgTest + " nanoseconds");
                //System.out.println(Arrays.toString(arrTest));
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
