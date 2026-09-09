function createHelloWorld() {
  return function (...args): string {
    return "Hello World";
  };
}

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 * f(1, 2, 3); // "Hello World"
 */
