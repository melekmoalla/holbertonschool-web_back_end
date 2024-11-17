const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', () => {
  it('should return a successful response when success is true', (done) => {
    getPaymentTokenFromAPI(true)
      .then((response) => {
        expect(response).to.have.property('data').that.equals('Successful response from the API');
        done();
      })
      .catch(done);
  });

  it('should not return a response when success is false', (done) => {
    getPaymentTokenFromAPI(false)
      .then(() => {
        done(new Error('Expected to fail, but it did not'));
      })
      .catch(() => {
        done();
      });
  });
});
