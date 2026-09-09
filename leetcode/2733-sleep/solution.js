/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
  return new Promise((resolve) => setTimeout(resolve, millis)); // [web:66][web:67]
}

/**
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // ~100
 */
