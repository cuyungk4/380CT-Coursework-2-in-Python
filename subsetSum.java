/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author user
 */
class subsetSum
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

		return subset[sum][length];
	}

	public static void main(String args[])
	{
		int set[] = {3, 34, 4, 12, 5, 2};
		int sum = 9;
		int length = set.length;
		if (subsetTest(set, length, sum) == true)
			System.out.println("Found a subset with given sum");
		else
			System.out.println("No subset with given sum");
	}
}
