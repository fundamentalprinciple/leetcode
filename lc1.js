/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // faulty algorithm, can't be improved further
    /*
    Checks for adjacent elements
    i=0
    j=1
    //nums.sort((a,b)=>{return a-b}) // array.sort() method works strings
    while (j!=nums.length+1) {
        if (target-nums[i]-nums[j]==0) {
                return [i,j];
        } else {
            i++;
            j++;
        };
    };

    Checks for same element apperaing twice
    i=0
    j=1
    nums.sort((a,b)=>{return a-b})
    while (j!=nums.length+1) {
        if (target-nums[i]-nums[j]==0) {
                return [i,j];
        } else {
            i++;
            j++;
        };
    };

    Misses non-adjacent element solutions
    */
};
