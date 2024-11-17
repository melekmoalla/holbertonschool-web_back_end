const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', () => {
  let spy;

  beforeEach(() => {
    // Set up the spy before each test
    spy = sinon.spy(Utils, 'calculateNumber');
  });

  afterEach(() => {
    // Restore the original method after each test
    spy.restore();
  });

  it('should call Utils.calculateNumber with SUM, 100, 20', () => {
    sendPaymentRequestToApi(100, 20);

    expect(spy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
  });

  it('should call Utils.calculateNumber with SUM, 10.5, 9.4', () => {
    sendPaymentRequestToApi(10.5, 9.4);

    expect(spy.calledOnceWithExactly('SUM', 10.5, 9.4)).to.be.true;
  });

  it('should log the correct total when called', () => {
    const consoleSpy = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    expect(consoleSpy.calledOnceWithExactly('The total is: 120')).to.be.true;

    consoleSpy.restore();
  });

  it('should call calculateNumber only once', () => {
    sendPaymentRequestToApi(30, 40);

    expect(spy.calledOnce).to.be.true;
  });

  it('should work with negative numbers', () => {
    sendPaymentRequestToApi(-10, -20);

    expect(spy.calledOnceWithExactly('SUM', -10, -20)).to.be.true;
  });
});
