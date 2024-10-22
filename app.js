const express = require('express');
const app = express();

app.use(express.static('public')); // 정적 파일 제공

const hostname = 'localhost';
const port = 3000;

// 서버 실행
app.listen(port, hostname, () => {
  console.log(`서버가 실행됩니다. 주소: http://${hostname}:${port}/`);
});