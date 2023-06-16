const iotcontroller=require("../controllers/iotcontrol")
const flamecontroller=require("../controllers/flamecontroller")

const router=require("express").Router()

router.get("/",iotcontroller.getallvalue)
router.get("/moy",iotcontroller.getMonthlyAverage)
router.get("/feu",flamecontroller.getallvalueflame)
module.exports=router