const Utils = {
    calculateNumber: function (type, a, b) {
      if (type === 'SUM') {
        return Math.round(a) + Math.round(b);
      } else if (type === 'SUBTRACT') {
        return Math.round(a) - Math.round(b);
      } else if (type === 'DIVIDE') {
        const roundedB = Math.round(b);
        if (roundedB === 0) {
          throw new Error('Cannot divide by zero');
        }
        return Math.round(a) / roundedB;
      } else {
        throw new Error('Invalid type');
      }
    },
  };
  
  module.exports = Utils;
  