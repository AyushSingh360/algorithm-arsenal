/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function (obj) {
  // For arrays: keys are indices "0","1",..., so empty array => 0 keys. [web:24][web:28]
  // For plain objects: keys are its own properties, so empty object => 0 keys. [web:24][web:28]
  return Object.keys(obj).length === 0;
};
