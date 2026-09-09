/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function (fn, args, t) {
  // schedule fn to run after t ms
  const timeoutId = setTimeout(() => {
    fn(...args); // execute with provided args after delay [web:79][web:81]
  }, t);

  // return a cancel function
  return function cancelFn() {
    clearTimeout(timeoutId); // cancel the scheduled execution if still pending [web:77][web:81]
  };
};

/**
 *  const result = [];
 *
 *  const fn = (x) => x * 5;
 *  const args = [2], t = 20, cancelTimeMs = 50;
 *
 *  const start = performance.now();
 *
 *  const log = (...argsArr) => {
 *      const diff = Math.floor(performance.now() - start);
 *      result.push({"time": diff, "returned": fn(...argsArr)});
 *  }
 *
 *  const cancel = cancellable(log, args, t);
 *
 *  const maxT = Math.max(t, cancelTimeMs);
 *
 *  setTimeout(cancel, cancelTimeMs);
 *
 *  setTimeout(() => {
 *      console.log(result); // [{"time":20,"returned":10}]
 *  }, maxT + 15)
 */
