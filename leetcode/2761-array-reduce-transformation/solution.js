/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function (nums, fn, init) {
  let val = init; // start from init [web:4]
  for (let i = 0; i < nums.length; i++) {
    val = fn(val, nums[i]); // accumulate using reducer fn [web:4]
  }
  return val; // if nums is empty, this just returns init [web:4]
};
