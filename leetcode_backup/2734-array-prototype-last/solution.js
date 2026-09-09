/**
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function () {
  // `this` is the array instance on which .last() is called. [web:47][web:50]
  if (this.length === 0) {
    return -1; // empty array case [web:45][web:52]
  }
  return this[this.length - 1]; // last element [web:47][web:52]
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */
