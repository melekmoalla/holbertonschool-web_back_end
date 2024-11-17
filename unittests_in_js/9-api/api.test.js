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
    request.get(`${baseUrl}/cart/20`, (err, res, body) => {
    expect(res.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 20');
      done();
    });
  });

  it('should return 404 for missing id',  (done) => {
    request.get('/cart/', (err, res, body) => {
    expect(res.status).to.equal(404);
      done();
    });
  });
});