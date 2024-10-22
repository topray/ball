const https = require('https');
const fs = require('fs');
const express = require('express');
const app = express();

app.use(express.static('public')); // 정적 파일 제공

const options = {
  key: fs.readFileSync('server.key'),
  cert: fs.readFileSync('server.crt')
};

https.createServer(options, app).listen(443, () => {
  console.log('HTTPS 서버가 실행 중입니다.');
});
