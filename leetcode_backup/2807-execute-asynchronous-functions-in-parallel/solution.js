/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function (functions) {
  return new Promise((resolve, reject) => {
    const n = functions.length;
    const results = new Array(n); // preserve order [web:17]
    let resolvedCount = 0;
    let finished = false; // avoid multiple settle calls [web:17]

    for (let i = 0; i < n; i++) {
      // Each item is a function returning a promise; call it immediately in parallel [web:19][web:20]
      Promise.resolve()
        .then(() => functions[i]()) // this also catches sync throw inside functions[i] [web:17]
        .then((value) => {
          if (finished) return;
          results[i] = value;
          resolvedCount++;
          if (resolvedCount === n) {
            finished = true;
            resolve(results); // resolve when all are done [web:17]
          }
        })
        .catch((err) => {
          if (finished) return;
          finished = true;
          reject(err); // reject on first error [web:17][web:21]
        });
    }
  });
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */
