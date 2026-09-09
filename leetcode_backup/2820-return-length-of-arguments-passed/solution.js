/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function (...args) {
  return args.length; // number of arguments passed [web:22][web:23]
};

/**
 * argumentsLength(1, 2, 3); // 3
 */
