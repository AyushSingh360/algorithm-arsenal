var TimeLimitedCache = function () {
  this.cache = new Map(); // key -> { value, timerId }
};

/**
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function (key, value, duration) {
  const exists = this.cache.has(key);

  // If key exists, clear its previous expiration timer
  if (exists) {
    clearTimeout(this.cache.get(key).timerId);
  }

  const timerId = setTimeout(() => {
    this.cache.delete(key);
  }, duration);

  this.cache.set(key, { value, timerId });

  // Problem wants true if there was an un-expired key already
  return exists;
};

/**
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function (key) {
  if (!this.cache.has(key)) {
    return -1;
  }
  return this.cache.get(key).value;
};

/**
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function () {
  return this.cache.size;
};
