🧮 Calculadora Avançada — Django
Este é um projeto de uma Calculadora Avançada com Login, desenvolvida como parte de um desafio técnico. O sistema permite que usuários autenticados realizem operações matemáticas e acompanhem um histórico completo de suas atividades.

🔗 Repositório: github.com/ReservadoRamon/calculadora-django

🚀 Funcionalidades
✅ Login e autenticação de usuários
✅ Tela de login estilizada com UI moderna
✅ Calculadora funcional com suporte a:
Adição, subtração, multiplicação, divisão
Cálculo com porcentagem (%)
Inversão de sinal (±)
✅ Histórico de operações individual por usuário
Inclui horário da operação
Histórico exibido em ordem decrescente
Histórico
Botão para limpar todo o histórico
✅ Modo claro/escuro com alternância manual (🌙 / ☀️)
✅ Interface visual refinada com responsividade
🖥️ Tecnologias Utilizadas
Python 3.11
Django 5.2.4
SQLite3 (banco de dados)
HTML5 + CSS3 (Poppins & Segoe UI)
SessionStorage para controle de estado
📂 Estrutura de Pastas
calculadora_project/ ├── core/ │ ├── templates/ │ │ └── core/ │ │ └── calculadora.html │ ├── static/ │ │ └── css/ │ │ ├── style.css │ │ └── login.css │ ├── models.py │ ├── views.py │ └── urls.py ├── templates/ │ └── registration/ │ └── login.html ├── manage.py └── README.md

🛠️ Como rodar o projeto localmente
1.Clone o repositório

git clone https://github.com/ReservadoRamon/calculadora-django.git

2. Crie e ative um ambiente virtual (recomendado)

python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux/Mac

3. Instale as dependências

pip install django

4. Execute as migrações

python manage.py migrate

5. Crie um superusuário

python manage.py createsuperuser

6. Inicie o servidor

python manage.py runserver

7. Acesse no navegador:
👉 http://127.0.0.1:8000


