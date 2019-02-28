# desafio-back-end

O desafio foi concluído utilizando Python 3.  
Foi feito cobertura de teste, criado um webservice que requer autenticação. A autenticação está mockada, mas foi feito de uma forma que poderia facilmente apontar para um banco, api, ad, etc...

Ao executar, utilizar a URL abaixo para ver o resultado do crawler:  
http://127.0.0.1:5000/api/v1/crawler/autoesporte  
Usuário: teste  
Senha: teste

O Dockerfile já faz um clone do projeto no github. Para rodar basta dar um build no Dockerfile e em seguida o run.
Comandos abaixo:

`sudo docker build -t  crawler/dbe:flask-alpine .`  
`sudo docker run -p 5000:5000 -t -d crawler/dbe:flask-alpine`


Também é possível executar o webservice sem utilização de docker, para isso instalar o requirements do projeto com o comando abaixo:

`pip install -r requirements`

Em seguida, executar via Python o módulo app.py:

`python app.py`

Também é possível executar apenas o módulo crawler.py para recuperar os dados do crawler.
Arquivo tests possui a cobertura de testes do scrap do xml e da quebra do html da descrição da página.
