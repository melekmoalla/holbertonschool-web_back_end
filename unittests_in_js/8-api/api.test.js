const request = require('request');
const { expect } = require('chai');

describe('Index page', () => {
  const baseUrl = 'http://localhost:7865';

  before((done) => {
    require('./api');
    done();
  });

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
});
