/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function (fn, t) {
  return async function (...args) {
    const timeoutPromise = new Promise((_, reject) => {
      setTimeout(() => reject("Time Limit Exceeded"), t);
    });

    // fn(...args) already returns a promise per constraints
    const fnPromise = fn(...args);

    // Whichever finishes first wins
    return Promise.race([fnPromise, timeoutPromise]);
  };
};
