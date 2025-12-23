var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');

// var indexRouter = require('./routes/index');
// var usersRouter = require('./routes/users');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(logger('dev'));  //GET /html.test 200 5.364 ms - 227 이런식으로 로그에 찍어주는 미들웨어
app.use(express.json());
app.use(express.urlencoded({ extended: false }));  //queryString으로 파싱해주는 미들웨어
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));


app.listen(9999)//Node.js express WAS 포트번호

app.get('/te.st',function(req,res,next){
  res.send('abcd')
})

app.get('/html.test',function(req,res,next){
    html = ""
    html += "<!DOCTYPE html>"
    html += "<html lang='en'>"
    html += "<head>"
    html += "    <meta charset='UTF-8'>"
    html += "    <meta name='viewport' content='width=device-width, initial-scale=1.0'>"
    html += "    <title>Document</title>"
    html += "</head>"
    html += "<body>"
    html += "<h1>대제목</h1>" 
    html += "<h2>소제목</h2>"
    html += "</body>"
    html += "</html>"
  res.send(html)
})

// http://195.168.9.246:9999/param.test?a=10&b=20
app.get('/param.test',function(req,res,next){
  console.log(req.query.a);
  console.log(req.query.b);
  console.log(req.query.a*1+req.query.b*1);
  html = ""
    html += "<!DOCTYPE html>"
    html += "<html lang='en'>"
    html += "<head>"
    html += "    <meta charset='UTF-8'>"
    html += "    <meta name='viewport' content='width=device-width, initial-scale=1.0'>"
    html += "    <title>Document</title>"
    html += "</head>"
    html += "<body>"
    html += "<h1>"+req.query.a+"</h1>" 
    html += "<h2>"+req.query.b+"</h2>"
    html += "<h2>"+req.query.a+req.query.b+"</h2>"
    html += "</body>"
    html += "</html>"
  res.send(html)
})


// xml/json을 만들어서 응답 + front end에서
//http://195.168.9.246:9999/json.test?a=10&b=20
app.get('/json.test',function(req,res,next){
  console.log(req.query.a);
  console.log(req.query.b);
  var cc = req.query.a*1+req.query.b*1
  var dd = {'result': cc}
  res.setHeader("Access-Control-Allow-Origin","*");
  res.send(dd)
})




// app.use('/', indexRouter);
// app.use('/users', usersRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
