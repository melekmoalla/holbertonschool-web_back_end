const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi with stub', () => {
  let stub;
  let consoleSpy;

  beforeEach(() => {
    stub = sinon.stub(Utils, 'calculateNumber').returns(10);

    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    stub.restore();
    consoleSpy.restore();
  });

  it('should call Utils.calculateNumber with SUM, 100, and 20', () => {
    sendPaymentRequestToApi(100, 20);

    expect(stub.calledOnceWithExactly('SUM', 100, 20)).to.be.true;

    expect(consoleSpy.calledOnceWithExactly('The total is: 10')).to.be.true;
  });

  it('should not call the original Utils.calculateNumber implementation', () => {
    sendPaymentRequestToApi(50, 30);

    expect(stub.callCount).to.equal(1);
    expect(stub.returned(10)).to.be.true;

    expect(consoleSpy.calledOnceWithExactly('The total is: 10')).to.be.true;
  });
});
