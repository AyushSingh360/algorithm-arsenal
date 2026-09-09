/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function (fn, t) {
  let timer = null; // persists across calls [web:4]

  return function (...args) {
    if (timer !== null) {
      // cancel previous scheduled call [web:4]
      clearTimeout(timer);
    }

    timer = setTimeout(() => {
      // schedule new call after t ms [web:4]
      fn(...args); // call with latest arguments [web:4]
    }, t);
  };
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */
