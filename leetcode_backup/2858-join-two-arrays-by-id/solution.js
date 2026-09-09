/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function (arr1, arr2) {
  const map = {};

  // Put all objects from arr1 into the map
  for (const obj of arr1) {
    map[obj.id] = { ...obj };
  }

  // Merge / add objects from arr2
  for (const obj of arr2) {
    if (map[obj.id]) {
      // arr2 overrides arr1 on key conflicts
      map[obj.id] = { ...map[obj.id], ...obj };
    } else {
      map[obj.id] = { ...obj };
    }
  }

  // Convert map to array and sort by id
  return Object.values(map).sort((a, b) => a.id - b.id);
};
