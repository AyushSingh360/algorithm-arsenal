/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
  const cache = {}; // cache: key -> result [web:46][web:48]

  return function (...args) {
    const key = JSON.stringify(args); // unique key for this argument list [web:47][web:48]

    if (key in cache) {
      // seen before?
      return cache[key]; // return cached result [web:46][web:48]
    }

    const result = fn(...args); // compute and store [web:46][web:48]
    cache[key] = result;
    return result;
  };
}

/**
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *   callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5, from cache; callCount is 1
 * console.log(callCount) // 1
 */
