/**
 * @param {Array} arr
 * @param {number} n
 * @return {Array}
 */
var flat = function (arr, n) {
  if (n === 0) return arr;

  const result = [];

  for (const el of arr) {
    if (Array.isArray(el) && n > 0) {
      result.push(...flat(el, n - 1));
    } else {
      result.push(el);
    }
  }

  return result;
};
