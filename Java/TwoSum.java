/*
Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
*/

class Solution_two_sum {
    public int[] twoSum(int[] nums, int target) {
        int[] found = new int[2];

        for (int i = 0; i < nums.length; i++){
            for (int j = i + 1; j < nums.length; j++){
                if ((nums[i] + nums[j]) == target){
                    found[0] = i;
                    found[1] = j;
                }
            }
        }
        return found;
    }
}
