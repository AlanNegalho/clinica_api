# Desafio clinica_api


## Descrição do projeto
  Você deverá implementar uma API (Interface de Programação de Aplicação) na qual gestor da clínica (superusuário) poderá cadastrar especialidades, médicos e disponibilizar horários nos quais os clientes poderão marcar as consultas. 

## :hammer: Funcionalidades do projeto
##### Crie uma API com os seguintes endpoints contendo as funcionalidades a seguir: 
#### Cadastrar especialidades 
Deve ser possível cadastrar as especialidades médicas (ex: CARDIOLOGIA, PEDIATRIA) que a clínica atende fornecendo as seguintes informações: 
* Nome: nome da especialidade médica (obrigatório) 
#### Cadastrar médicos 
Deve ser possível cadastrar os médicos que podem atender na clínica fornecendo as seguintes informações: 
* Nome: Nome do médico (obrigatório) 
* CRM: Número do médico no conselho regional de medicina (obrigatório) ● E-mail: Endereço de e-mail do médico
* Telefone: Telefone do médico 
* Especialidade: Especialidade na qual o médico atende 
#### Criar agenda para médico 
Deve ser possível criar uma agenda para um médico em um dia específico fornecendo as seguintes informações: 
* Médico: Médico que será alocado (obrigatório) 
* Dia: Data de alocação do médico (obrigatório) 
* Horários: Lista de horários na qual o médico deverá ser alocado para o dia especificado (obrigatório) 
#### Crie uma página para os clientes realizarem um cadastro 
Deve ser possível o cliente realizar o seu cadastro no sistema fornecendo as seguintes informações: 
* Nome: Nome do médico (obrigatório) 
* CPF: Número do médico no conselho regional de medicina (obrigatório) ● E-mail: Endereço de e-mail do médico 
* Sexo: Sexo do cliente (masculino ou feminino) 
* Telefone: Telefone do médico 
#### Crie uma página para o cliente marque as consultas 
Dado que o cliente já esteja logado no sistema ele poderá marcar uma consulta com um determinado médico para uma determinada data. O cliente pode realizar o login e logout do sistema. 
#### Restrições: 
* Não deve ser possível criar mais de uma agenda para um médico em um mesmo dia 
* Não deve ser possível criar uma agenda para um médico em um dia passado
## 📁 Acesso ao projeto

**É possível baixar ou acessar o código fonte do projeto no [Link](https://github.com/AlanNegalho/clinica_api.git) ou clone o repositório**
```python
git clone https://github.com/AlanNegalho/clinica_api.git
```

## 🛠️ Abrir e rodar o projeto

Após acessar o código fonte do projeto faça o download através do git clone ou no formato zip. Podemos agora iniciamos a instalação da aplicação em nossa máquina. Lembrando que utilizaremos o ambiente virtual para criação do projeto.

## Upgrade necessários

Acesse a pasta diretoria da aplicação
```python
cd clinica_api
```
Atualizar o sistema caso esteja no Linux

```python
sudo apt update 
```


```python
sudo apt -y upgrade
```

Instalar o pip3


```python
sudo apt install python3-pip
```

Instalar ferramentas adicionais


```python
sudo apt install build-essential libssl-dev libffi-dev python3-dev
```

Instalando o env e virtualenv


```python
sudo apt install -y python3-venv
```


```python
sudo apt install python3-virtualenv
```
Instalando no Windows

```python
pip install virtualenv
```
Instalando no MacOS

```python
sudo pip uninstall virtualenv

sudo -H pip install virtualenv
```

## Criando o ambiente virtual
Criando seu ambiente virtual. Vamos chamá-lo venv

No Linux
```python
python3 -m venv venv
```

Criando o seu ambiente virtual no Windows 

```python
python -m venv venv
```

Criando seu ambiente virtual no MacOS

```python
virtualenv -p python3 <desired-path>


virtualenv -p python3 env

```

Ative o ambiente virtual 

No Windows
```python
venv\Scripts\activate.bat
```
No linux
```python
. venv/bin/activate
```
Para desativar o ambiente virtual, na pasta


```python
deactivate 
```

```python
quit()
```
## Bibliotecas utilizadas no desenvolvimento da aplicação
- Django==4.1.4
- djangorestframework==3.14.0
- django-jazzmin 2.6.0(Utilizada para estilizar o admin)

1.   https://pypi.org/project/Django/
2.   https://pypi.org/project/djangorestframework/
3.   https://pypi.org/project/django-jazzmin/

Instale todas as bibliotecas acima através do requirements.txt arquivo localizado na pasta da aplicação.

```python
pip install -r requirements.txt
```
Realize  as migrations e o migrate:
```python
python manage.py makemigrations
```
```python
python manage.py migrate
```
Após realizar as migrações, crie um super usuário pra realizar acesso ao admin do Django. Adicione o nome do usuário logo após o comando.
```python
python manage.py createsuperuser
```
Inicie o servidor:
```python
python manage.py runserver
```
Acesse o link da aplicação:
```python
http://127.0.0.1:8000/
```

Pode-se observar que ao acessarmos a página pela primeira vez nota-se que não estamos logados. Para resolvermos isso no link da aplicação http://127.0.0.1:8000/ adiciaonaremos um novo endedreços de pagina chamado admin então o novo link fica http://127.0.0.1:8000/admin  faça o ligin com os dados superuser criados anteriormente, retorne a página principal de aplicação http://127.0.0.1:8000/
![Captura de tela de 2023-01-19 19-26-14](https://user-images.githubusercontent.com/107214420/213577501-fd721244-7ab9-4571-ad60-4569634fff9e.png)

Podemos observa no canto superior direito que estamos logados no sistema, podendo assim ser feito a ultilização da api. 
#### Só e possessível acessar o endpoints Agenda com os seguintes dados usuário: Cliente  senha: 1234
![Captura de tela de 2023-01-19 19-47-56](https://user-images.githubusercontent.com/107214420/213579462-d94f6623-d358-4f32-8c31-f4f9ca8a254f.png)

## Deploy da aplicação
A api esta disponível na web, acesse através do [Link](http://alanoliveira.pythonanywhere.com/)

⌨️ com ❤️ por [Alan Negalho](https://github.com/AlanNegalho) 😊
