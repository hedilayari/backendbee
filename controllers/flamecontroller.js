const iotmodel=require('../models/iotmodel');
const { all } = require('../routers/iotrouter');



const getallvalueflame = async (req, res) => {
    try {
      const result = await iotmodel
        .find({}, { flame:1, timestamp: 1 })
        .sort({timestamp:-1})
        .limit(10)
        .exec();
  
      res.send(result);
    } catch (err) {
      console.log(err);
    }
  };
  
exports.getallvalueflame=getallvalueflame;