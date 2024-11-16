// 0-calcul.test.js
const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', function() {
  it('should return 4 for (1, 3)', function() {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('should return 5 for (1, 3.7)', function() {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('should return 5 for (1.2, 3.7)', function() {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('should return 6 for (1.5, 3.7)', function() {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  it('should return 0 for (0, 0)', function() {
    assert.strictEqual(calculateNumber(0, 0), 0);
  });

  it('should return 2 for (-1, 3)', function() {
    assert.strictEqual(calculateNumber(-1, 3), 2);
  });
});
