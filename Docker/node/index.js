let express = require('express');

const app = express();

app.get("/hello",(req,res)=>{
    res.send("<h1>HELLO AND THANKS FOR VISITING</h1>")
})

app.listen(8000, ()=>{
    console.log("APP IS RUNNING AT 8000")
});