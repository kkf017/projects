const global = require("./global");


(global.app).get('/', (req, res) => {
    res.render("../templates/home.hbs");  
});


(global.app).get('/home/', (req, res) => {
    res.render("../templates/home.hbs");  
});

(global.app).get('/about/', (req, res) => {
    res.render("../templates/about.hbs");  
});
