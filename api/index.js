const express = require('express')
const app = express()
const port = process.env.port || 5000 // 5000 for testing
const routes = require('./routes')


app.use(routes)

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})
