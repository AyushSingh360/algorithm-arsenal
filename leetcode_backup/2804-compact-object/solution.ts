type JSONValue =
  null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function compactObject(obj: Obj): Obj {
  // If it's not an object (i.e., primitive or null), just return it
  if (obj === null || typeof obj !== "object") {
    return obj;
  }

  // Handle arrays
  if (Array.isArray(obj)) {
    // Filter out falsy values, then recursively compact each remaining element
    return obj.filter(Boolean).map((item) => compactObject(item as Obj)) as Obj;
  }

  // Handle plain objects
  const result: Record<string, JSONValue> = {};
  for (const [key, value] of Object.entries(obj)) {
    if (!value) continue; // skip falsy values at this level

    const compacted = compactObject(value as Obj);
    // After recursion, compacted is guaranteed truthy because value was truthy
    result[key] = compacted as JSONValue;
  }
  return result;
}
