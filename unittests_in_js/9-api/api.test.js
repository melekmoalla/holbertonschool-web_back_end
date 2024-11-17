const request = require('supertest');
const app = require('./api');
const { expect } = require('chai');

describe('GET /cart/:id', () => {
  it('should return 200 and the correct response for a numeric id', async () => {
    const res = await request(app).get('/cart/12');
    expect(res.status).to.equal(200);
    expect(res.text).to.equal('Payment methods for cart 12');
  });

  it('should return 404 for a non-numeric id', async () => {
    const res = await request(app).get('/cart/hello');
    expect(res.status).to.equal(404);
    expect(res.text).to.include('Cannot GET /cart/hello');
  });

  it('should return 404 for missing id', async () => {
    const res = await request(app).get('/cart/');
    expect(res.status).to.equal(404);
  });
});
