const { json } = require('express');
var express = require('express')
var router = express.Router()

var data = require('./data')

router.get('/', (req, res) => {
  res.json('Hello World!')
});

router.get('/collection_overview', (req, res) => {
  res_data = (
    ({ tweets, named_entities }) => ({ tweets, named_entities })
  )(data);

  res.json(res_data)
});


router.get('/quick_stats', (req, res) => {
  res_data = (
    ({quick_stats}) => ({quick_stats})
  )(data);

  res.json(res_data)
});

module.exports = router