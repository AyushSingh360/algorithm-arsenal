/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function (fn) {
  // flag to remember if we've called fn before
  let called = false; // [web:34][web:38]

  return function (...args) {
    if (!called) {
      // first call
      called = true; // mark as called
      return fn(...args); // execute and return result [web:34][web:38]
    }
    // subsequent calls
    return undefined; // fn is not called again [web:34][web:38]
  };
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */
