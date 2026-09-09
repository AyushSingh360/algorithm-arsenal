/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function (fn) {
  const grouped = {}; // result object [web:55][web:56]

  for (const item of this) {
    // `this` is the array instance [web:56][web:63]
    const key = fn(item); // key is always a string per problem [web:57]
    if (!grouped[key]) {
      // create bucket if missing [web:55][web:60]
      grouped[key] = [];
    }
    grouped[key].push(item); // append in original order [web:55][web:60]
  }

  return grouped;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */
