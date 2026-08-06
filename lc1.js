/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    i=0
    j=1
    while (j!=nums.length+1) {
        if (target-nums[i]-nums[j]==0) {
                return [i,j];
        } else {
            i++;
            j++;
        };
    };
};
