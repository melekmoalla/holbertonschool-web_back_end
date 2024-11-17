const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', () => {
  let consoleSpy;

  beforeEach(() => {
    // Spy on console.log
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    // Restore the original console.log after each test
    consoleSpy.restore();
  });

  it('should log "The total is: 120" when called with 100 and 20', () => {
    sendPaymentRequestToApi(100, 20);

    // Verify the log message
    expect(consoleSpy.calledOnceWithExactly('The total is: 120')).to.be.true;

    // Verify console.log is only called once
    expect(consoleSpy.callCount).to.equal(1);
  });

  it('should log "The total is: 20" when called with 10 and 10', () => {
    sendPaymentRequestToApi(10, 10);

    // Verify the log message
    expect(consoleSpy.calledOnceWithExactly('The total is: 20')).to.be.true;

    // Verify console.log is only called once
    expect(consoleSpy.callCount).to.equal(1);
  });
});
