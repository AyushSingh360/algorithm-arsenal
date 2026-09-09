/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function (functions) {
  return function (x) {
    // start with the input value
    let result = x; // [web:13]

    // apply functions from right to left
    for (let i = functions.length - 1; i >= 0; i--) {
      result = functions[i](result); // [web:13][web:15]
    }

    // for empty array, this just returns x (identity)
    return result; // [web:13][web:16]
  };
};

/**
 * const fn = compose([x => x + 1, x => 2 * x]);
 * fn(4); // 9
 */
