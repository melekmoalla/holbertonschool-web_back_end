const express = require('express');
const app = express();

// Route for GET /
app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

app.get('/cart/:id(\\d+)', (req, res) => {
    const cartId = req.params.id;
    res.send(`Payment methods for cart ${cartId}`);
  });

  app.use(express.json());

  app.get('/available_payments', (req, res) => {
    res.json({
      payment_methods: {
        credit_cards: true,
        paypal: false,
      },
    });
  });
  
  app.post('/login', (req, res) => {
    const { userName } = req.body;
  
    if (!userName) {
      return res.status(400).send('Missing userName');
    }
  
    res.send(`Welcome ${userName}`);
  });
// Start the server
const PORT = 7865;
app.listen(PORT, () => {
  console.log(`API available on localhost port ${PORT}`);
});

module.exports = app;
