const express = require('express');
const app = express();



app.get('/cart/:id(\\d+)', (req, res) => {
    const cartId = req.params.id;
    res.send(`Payment methods for cart ${cartId}`);
  });

// Start the server
const PORT = 7865;
app.listen(PORT, () => {
  console.log(`API available on localhost port ${PORT}`);
});

module.exports = app;
