const express = require('express')
const app = express()
const port = 80 //8080 for testing, 80 for deployment
const routes = require('./routes')


app.use(routes)

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})
