const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const path = require('path');

// Configuración del middleware para analizar JSON en las solicitudes
app.use(bodyParser.json());

// Configuración del motor de plantillas EJS
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

let resultadoGlobal; // Variable global para almacenar el resultado

app.post('/resultado', (req, res) => {
  const resultado = req.body.resultado;
  console.log('Resultado recibido:', resultado);

  resultadoGlobal = resultado; // Almacena el resultado en la variable global

  res.send('OK');
});

app.get('/result', (req, res) => {
  const resultado = req.query.resultado;
  res.render('result', { resultado: resultado });
});

// Ruta para servir archivos estáticos
app.use(express.static(path.join(__dirname, 'public')));

// Inicia el servidor
app.listen(3000, () => {
  console.log('Servidor escuchando en el puerto 3000');
});
