const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', () => {
  describe('SUM', () => {
    it('should return 6 for SUM(1.4, 4.5)', () => {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });
    it('should return 0 for SUM(-1.4, 1.4)', () => {
      assert.strictEqual(calculateNumber('SUM', -1.4, 1.4), 0);
    });
  });

  describe('SUBTRACT', () => {
    it('should return -4 for SUBTRACT(1.4, 4.5)', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });
    it('should return 3 for SUBTRACT(3.5, 1.2)', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', 3.5, 1.2), 3);
    });
  });

  describe('DIVIDE', () => {
    it('should return 0.2 for DIVIDE(1.4, 4.5)', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });
    it('should return "Error" for DIVIDE(1.4, 0)', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });
    it('should return 2.5 for DIVIDE(4.5, 2)', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 4.5, 2), 2.5);
    });
  });

  describe('Invalid operation type', () => {
    it('should throw an error for an invalid type', () => {
      assert.throws(() => calculateNumber('MULTIPLY', 1, 2), {
        name: 'Error',
        message: 'Invalid operation type',
      });
    });
  });
});
