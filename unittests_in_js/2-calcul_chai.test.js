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

});
