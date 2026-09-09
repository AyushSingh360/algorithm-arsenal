/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function (promise1, promise2) {
  const [v1, v2] = await Promise.all([promise1, promise2]); // wait for both [web:55][web:62]
  return v1 + v2; // sum and return [web:55][web:60]
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */
