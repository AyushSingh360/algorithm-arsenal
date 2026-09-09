/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function (fn, args, t) {
  // call immediately
  fn(...args);

  // schedule repeated calls
  const intervalId = setInterval(() => {
    fn(...args);
  }, t);

  // return cancel function
  return function cancelFn() {
    clearInterval(intervalId);
  };
};
