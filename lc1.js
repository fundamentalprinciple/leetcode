/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // good algorithm -> check if difference of target and element exists in hashmap of elements,indices

    hashmap = new Map();
    index=-1
    for (element of nums) {
        index++;
        if (hashmap.has(target-element)) {
            return [hashmap.get(target-element),index];
        }
        hashmap.set(element,index);
    };



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
