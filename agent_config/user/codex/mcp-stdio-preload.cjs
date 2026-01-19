// Force console logs to stderr so MCP stdio channel stays clean.
const toErr = (...args) => console.error(...args);
console.log = toErr;
console.info = toErr;
console.warn = toErr;
