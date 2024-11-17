const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', () => {
  describe('SUM', () => {
    it('should return 6 for SUM(1.4, 4.5)', () => {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });
    it('should return 0 for SUM(-1.4, 1.4)', () => {
      expect(calculateNumber('SUM', -1.4, 1.4)).to.equal(0);
    });
  });

  describe('SUBTRACT', () => {
    it('should return -4 for SUBTRACT(1.4, 4.5)', () => {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });
    it('should return 3 for SUBTRACT(3.5, 1.2)', () => {
      expect(calculateNumber('SUBTRACT', 3.5, 1.2)).to.equal(3);
    });
  });

  describe('DIVIDE', () => {
    it('should return 0.2 for DIVIDE(1.4, 4.5)', () => {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });
    it('should return "Error" for DIVIDE(1.4, 0)', () => {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });
    it('should return 2.5 for DIVIDE(4.5, 2)', () => {
      expect(calculateNumber('DIVIDE', 4.5, 2)).to.equal(2.5);
    });
  });

  describe('Invalid operation type', () => {
    it('should throw an error for an invalid type', () => {
      expect(() => calculateNumber('MULTIPLY', 1, 2)).to.throw(Error, 'Invalid operation type');
    });
  });
});
