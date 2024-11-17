
const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');


describe('sendPaymentRequestToApi', () => {
    it('should use Utils.calculateNumber with the correct arguments', () => {
      const spy = sinon.spy(Utils, 'calculateNumber');
  
      sendPaymentRequestToApi(100, 20);
        expect(spy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
  
      spy.restore();
    });
  });