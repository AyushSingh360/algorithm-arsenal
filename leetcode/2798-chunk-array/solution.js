/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function (arr, size) {
  const res = [];

  // Move the index by `size` each time, slicing subarrays. [web:37][web:41]
  for (let i = 0; i < arr.length; i += size) {
    res.push(arr.slice(i, i + size)); // last slice may be shorter [web:37]
  }

  return res;
};
