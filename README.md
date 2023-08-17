# DjangoWorkshop
Workshop de introdução ao django

## ☕ Usando o Django

Tutorial de Iniciação de Django

1. Crie uma pasta na sua área de trabalho

2. Abra essa pasta na sua IDE que possui Python

3. Abra o terminal da IDE

4. Crie um Ambiente Virtual utilizando o comando (o segundo "venv" é o nome do seu ambiente)
<dt>
    
    python -m venv venv
  </dt>

5. Ative o seu ambiente virtual utilizando o comando "venv/scripts/activate". Caso queira desativá-la, o basta utilizar "deactivate"
<dt>
    
    python -m venv venv
  </dt>

6. Instale o Django e suas dependências usando o comando "pip install django"
<dt>
    
    python -m venv venv
  </dt>

7. Crie o seu projeto. Use o comando "django-admin startproject meuprojeto".
<dt>
    
    python -m venv venv
  </dt>

8. Crie o seu app. use o comando "python manage.py startapp meuapp".
<dt>
    
    python -m venv venv
  </dt>

9. Utilize os comandos "python manage.py makemigrations" e "python manage.py migrate" para iniciarmos o banco de dados. (No VS Code, baixe a extensão SQLite Viewer para ter uma boa visualização do db em tempo real)
<dt>
    
    python -m venv venv
  </dt>
<dt>
    
    python -m venv venv
  </dt>

10. Teste se a instalação deu certo. Use o comando "python manage.py runserver" para rodar o server. Se aparecer o foguetinho do Django é porque funcionou
<dt>
    
    python -m venv venv
  </dt>

11. Dentro da primeira pasta do seu projeto (a mais externa), crie uma pasta chamada "templates". Ela receberá os seus arquivos HTML

12. Alterações na settings.py
	12.1: Ir até "INSTALLED_APPS" (linha 33) e adicionar no final dela o nome do seu projeto entre aspas simples. Lembre de colocar a vírgula no final
	12.2: Vá até "TEMPLATES" (linha 55) e adicione dentro da lista 'DIRS' (linha 58) 'templates'. Isso servirá para os arquivos que estarão na nossa pasta criada no passo 11

13. Dentro do app, crie um arquivo chamado urls.py, da mesma forma que tem no projeto. 

14. Conecte e configure as urls.py do APP com a do PROJETO 	
	14.1: Entre na urls.py do projeto e adicione no "from django.urls import path, include"
<dt>
    
    python -m venv venv
  </dt>
	14.2: Depois, dentro da lista urlpatterns, adicione "path('', include(meuapp.urls)),".
<dt>
    
    python -m venv venv
  </dt>
	14.3: Agora, copie o conteúdo do urls.py do PROJETO, vá na urls.py do APP e cole, mantendo o import que colocamos no passo anterior e a lista urlpatterns lá. Deixe-a Vazia.
	14.4: Adicione "from . import views"
<dt>
    
    python -m venv venv
  </dt>
	14.5: Adicione "app_name="meuapp" acima do urlpatterns.
<dt>
    
    python -m venv venv
  </dt>

15. Crie o seu primeiro arquivo HTML (meutemplate.html, por exemplo). Vamos testar se toda a conexão até agora está funcionando. Vamos colocar um header simples: "<h1>teste</h1>".
<dt>
    
    python -m venv venv
  </dt>

16. Crie uma função para visualização da nossa página na views.py. Crie uma função passando como parâmetro o método request, dessa forma:
	def meutemplate(request):
		return render(request, "meutemplate.html")

18. Agora, vá na urls.py (a partir de agora, quando for citado o arquivo urls.py, me refiro ao do APP) e crie um path para aquela função da views. Dentro de urlpatterns, coloque "path("", views.meutemplate, name="meutemplate")". As aspas vazias são a url vazia. Ou seja, quando entrarmos no link principal ("127.0.0.1:8000"), essa será a primeira página que veremos. A views.meutemplate é o "views." seguido do nome da função da views que queremos referenciar a esse caminho, ou seja, a "meutemplate" foi usada neste tutorial. O name [e um nome simbólico dado à URL, permitindo que você utilize esse nome pra se referir a essa url em outras partes do código Django.

19. Rode novamente utilizando o comando "python manage.py runserver" e veja se funcionou. Caso apareça o texto que você definiu no seu arquivo html.
<dt>
    
    python -m venv venv
  </dt>

20. Crie seu superuser para ter acesso a página de admin do django. Utilize o comando "python manage.py createsuperuser" e preencha os dados pedidos.
<dt>
    
    python -m venv venv
  </dt>

21. Entre na página do admin utilizando a a sua url mais /admin.


## 🤝 Colaboradores

Agradecemos às seguintes pessoas que contribuíram para este workshop:

Desenvolvedores:
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Kal-0">
        <img src="https://avatars.githubusercontent.com/u/106926790?s=400&u=d51d91a8d447afbb4a9d0be21d664b82d7091fc5&v=4" width="100px;" alt="Foto Kal"/><br>
        <sub>
          <b>Caio Cesar</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Fiend3333">
        <img src="https://avatars.githubusercontent.com/u/116087739?v=4" width="100px;" alt="Foto Diogo"/><br>
        <sub>
          <b>Diogo Henrique</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/virnaamaral">
        <img src="https://avatars.githubusercontent.com/u/116957619?v=4" width="100px;" alt="Foto Stora"/><br>
        <sub>
          <b>Virna Amaral</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Caiobadv">
        <img src="https://avatars.githubusercontent.com/u/117755420?v=4" width="100px;" alt="Foto Matheus Gomes"/><br>
        <sub>
          <b>Caio Barreto</b>
        </sub>
      </a>
    </td>
  </tr>
</table>
