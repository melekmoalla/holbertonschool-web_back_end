const request = require('request');
const { expect } = require('chai');

describe('Index page', () => {
  const baseUrl = 'http://localhost:7865';

  it('should return the correct status code for GET /', (done) => {
    request.get(`${baseUrl}/`, (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it('should return the correct result for GET /', (done) => {
    request.get(`${baseUrl}/`, (err, res, body) => {
    expect(res.statusCode).to.equal(200);
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('should return the correct result for GET /', (done) => {
    request.get(`${baseUrl}/available_payments`, {json: {userName: 'Betty'}}, (err, res, body) => {
    expect(res.statusCode).to.equal(200);
      expect(body).to.equal({payment_methods: {
        credit_cards: true,
        paypal: false,
      }});
      done();
    });
  });

  it('should return the correct result for GET /', (done) => {
    request.get(`${baseUrl}/login`, {json: {userName: 'Betty'}}, (err, res, body) => {
    expect(res.statusCode).to.equal(200);
      expect(body).to.equal('Welcome Betty');
      done();
    });
  });


});
