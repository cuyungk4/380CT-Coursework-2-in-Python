
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author user
 */
import java.util.Arrays;
import java.util.Random;
import java.lang.*;

class DynamicSubsetSum
{
	static boolean subsetTest(int set[], int length, int sum)
	{
		boolean subset[][] = new boolean[sum+1][length+1];
		
		//if sum is 0 (in column 1), set to true (remember table in video)
		for(int i = 0; i <= length; i++)
			subset[0][i] = true;
		
		//if set length is 0, set false on that row
		for(int i = 1; i <= sum; i++)
			subset[i][0] = false;
		
		//fill up the table
		for(int i = 1; i <= sum; i++)
		{
			for(int j = 1; j <= length; j++)
			{
				//going through the [row][column] of table
				subset[i][j] = subset[i][j-1];
				
				//if i is larger or equal to last element in set
				if(i >= set[j-1])
				{
					//either include or exclude from subset
					subset[i][j] = subset[i][j] || subset[i - set[j-1]][j-1];
				}
			}
		}
		
		//print the table
		/*for(int i = 0; i <= sum; i++)
		{
			for(int j = 0; j <= length; j++)
				System.out.println(subset[i][j]);
			System.out.println("\n");
		}*/
		
		return subset[sum][length];
	}

	public static void main(String args[])
	{
            // add code from Friday to fix dynamic by applying bitlength 
                Random r = new Random();
                int[] set = new int[10];
                int length = set.length;
                 
                double min = 0;
                double max = 5;
                //maxbitlength, 2^max - 1
                //the larger the numbers the array stores, the more memory they take
                double maxBitLength = Math.pow(2.0,max) - 1;
                for (int i=0; i < length; i++)
                {
                    set[i] = (int) (r.nextInt((int) (maxBitLength - min + 1)) + min);
                }
                System.out.println("Array: " + Arrays.toString(set));
		//int set[] = {3, 34, 4, 12, 5, 2};
                //pick a random target from 0 to length x maxBitLength
		double sum = r.nextInt((int) (((length * maxBitLength) - min + 1) + min));
		
                long startT = System.nanoTime();
		if (subsetTest(set, length, (int) sum) == true)
			System.out.println("Found a subset with given sum: " + sum);
		else
			System.out.println("No subset with given sum: " + sum);
                long endT = System.nanoTime();
                long duration = (endT - startT);
                System.out.println(duration + " nanoseconds");
	}
}
