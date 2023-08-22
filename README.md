# Workshop de Introdução ao Django

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
    
    venv/scripts/activate
  </dt>

6. Instale o Django e suas dependências usando o comando "pip install django"
<dt>
    
    pip install django
  </dt>

7. Crie o seu projeto. Use o comando "django-admin startproject meuprojeto".
<dt>
    
    django-admin startproject meuprojeto
  </dt>

8. Crie o seu app. use o comando "python manage.py startapp meuapp".
<dt>
    
    python manage.py startapp meuapp
  </dt>

9. Utilize os comandos "python manage.py makemigrations" e "python manage.py migrate" para iniciarmos o banco de dados. (No VS Code, baixe a extensão SQLite Viewer para ter uma boa visualização do db em tempo real)
<dt>
    
    python manage.py makemigrations
  </dt>
<dt>
    
    python manage.py migrate
  </dt>

10. Teste se a instalação deu certo. Use o comando "python manage.py runserver" para rodar o server. Se aparecer o foguetinho do Django é porque funcionou
<dt>
    
    python manage.py runserver
  </dt>

11. Dentro da primeira pasta do seu projeto (a mais externa), crie uma pasta chamada "templates". Ela receberá os seus arquivos HTML

12. Alterações na settings.py
	12.1: Ir até "INSTALLED_APPS" (linha 33) e adicionar no final dela o nome do seu projeto entre aspas simples. Lembre de colocar a vírgula no final
	12.2: Vá até "TEMPLATES" (linha 55) e adicione dentro da lista 'DIRS' (linha 58) 'templates'. Isso servirá para os arquivos que estarão na nossa pasta criada no passo 11

13. Dentro do app, crie um arquivo chamado urls.py, da mesma forma que tem no projeto. 

14. Conecte e configure as urls.py do APP com a do PROJETO 	
	14.1: Entre na urls.py do projeto e adicione no "from django.urls import path, include"
<dt>
    
    from django.urls import path, include
  </dt>
	14.2: Depois, dentro da lista urlpatterns, adicione "path('', include('meuapp.urls')),".
<dt>
    
    path('', include('meuapp.urls')),
  </dt>
	14.3: Agora, copie o conteúdo do urls.py do PROJETO, vá na urls.py do APP e cole, mantendo o import que colocamos no passo anterior e a lista urlpatterns lá. Deixe-a Vazia.
	14.4: Adicione "from . import views"
<dt>
    
    from . import views
  </dt>
	14.5: Adicione "app_name="meuapp"" acima do urlpatterns.
<dt>
    
    app_name="meuapp"
  </dt>

15. Crie o seu primeiro arquivo HTML (meutemplate.html, por exemplo). Vamos testar se toda a conexão até agora está funcionando. Vamos colocar um header simples:
<dt>
    
    <h1>teste</h1>
  </dt>

16. Crie uma função para visualização da nossa página na views.py. Crie uma função passando como parâmetro o método request, dessa forma:
	def meutemplate(request):
		return render(request, "meutemplate.html")
<dt>
    
    def meutemplate(request):
		return render(request, "meutemplate.html")
  </dt>

18. Agora, vá na urls.py (a partir de agora, quando for citado o arquivo urls.py, me refiro ao do APP) e crie um path para aquela função da views. Dentro de urlpatterns, coloque "path("", views.meutemplate, name="meutemplate")". As aspas vazias são a url vazia. Ou seja, quando entrarmos no link principal ("127.0.0.1:8000"), essa será a primeira página que veremos. A views.meutemplate é o "views." seguido do nome da função da views que queremos referenciar a esse caminho, ou seja, a "meutemplate" foi usada neste tutorial. O name [e um nome simbólico dado à URL, permitindo que você utilize esse nome pra se referir a essa url em outras partes do código Django.
<dt>
    
    path("", views.meutemplate, name="meutemplate")
  </dt>

19. Rode novamente utilizando o comando "python manage.py runserver" e veja se funcionou. Caso apareça o texto que você definiu no seu arquivo html.
<dt>
    
    python manage.py runserver
  </dt>

20. Crie seu superuser para ter acesso a página de admin do django. Utilize o comando "python manage.py createsuperuser" e preencha os dados pedidos.
<dt>
    
    python manage.py createsuperuser
  </dt>

21. Entre na página do admin utilizando a a sua url mais /admin ( "127.0.0.1:8000/admin" ).

## 🤖 Descrições

Views:

Propósito: Em desenvolvimento web, as views lidam com a lógica por trás do tratamento de requisições HTTP, processamento de dados e geração de respostas apropriadas. Elas encapsulam a lógica de negócios da aplicação, a manipulação de dados e a interação com os models.
Função: Quando um usuário faz uma requisição a uma URL específica, a função de visualização correspondente é responsável por processar essa requisição, buscar dados do banco de dados, se necessário, realizar cálculos ou transformações e decidir qual resposta enviar de volta. As views atuam essencialmente como intermediárias entre as requisições recebidas e os dados a serem apresentados ou manipulados.
Linguagem: As views são tipicamente implementadas como funções ou classes em Python em frameworks como o Django. Elas podem retornar vários tipos de respostas, como conteúdo HTML, dados JSON, redirecionamentos ou até mensagens de erro.

Templates:

Propósito: Os templates são usados para definir a estrutura e aparência da interface do usuário. Eles separam a camada de apresentação da lógica de negócios e manipulação de dados, permitindo que os desenvolvedores criem páginas da web dinâmicas e visualmente atrativas.
Função: Os templates contêm espaços reservados e tags de template que são substituídos por dados reais quando o template é renderizado. Eles definem a estrutura da página HTML, onde o conteúdo dinâmico é inserido, e frequentemente incluem loops, condições e outras lógicas para controlar como o conteúdo é exibido. Os templates focam em como a informação é apresentada ao usuário.
Linguagem: Os templates geralmente são escritos em HTML, mas podem incluir tags de template e filtros específicos do framework sendo usado. No Django, por exemplo, os templates utilizam sua linguagem de template para incorporar dados dinâmicos e lógica.
models:

Propósito: Os models definem a estrutura e o comportamento dos dados na aplicação. Eles representam a maneira como os dados são armazenados, recuperados e manipulados no banco de dados. Os models ajudam a garantir consistência e integridade na forma como os dados são gerenciados.
Função: Em frameworks como o Django, os models são implementados como classes em Python que herdam de uma classe de models base. Cada atributo da classe do models corresponde a um campo na tabela do banco de dados. Os models definem relacionamentos entre diferentes tipos de dados e podem incluir métodos para realizar várias operações nesses dados, como criação, atualização, exclusão e consulta.
Linguagem: Os models são implementados usando classes Python e fazem parte da lógica do backend. Eles abstraem a estrutura e as interações do banco de dados, permitindo que os desenvolvedores trabalhem com dados de maneira orientada a objetos sem lidar diretamente com SQL.
Em resumo, as distinções entre views, templates e models são:

Views: Lidam com o processamento de requisições, manipulação de dados e geração de respostas. Elas preenchem a lacuna entre as requisições dos usuários e a lógica do backend da aplicação.

Templates: Definem como os dados são apresentados aos usuários na parte frontal (frontend). Eles estruturam o layout HTML e incorporam conteúdo dinâmico usando tags e lógica de template.

Models: Definem a estrutura de dados, relacionamentos e comportamento. Eles abstraem as operações de banco de dados e fornecem uma interface orientada a objetos de alto nível para trabalhar com dados.

## 🤓☝️ Recomendações didaticas

<table>
  <tr>
    <td align="center">
      <a href="https://www.youtube.com/@djangolessons4614">
        <img src="https://yt3.googleusercontent.com/ytc/AOPolaRasVoZafNkRP0cd-lsDZAy9izjsW_fhsr9e9i_=s176-c-k-c0x00ffffff-no-rj" width="100px;" alt="Django Lessons"/><br>
        <sub>
          <b>Django Lessons</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://www.youtube.com/@freecodecamp">
        <img src="https://yt3.googleusercontent.com/ytc/AOPolaTs1IEit9EUooQAJkWS4SkpUE7oMDXYrjIgnOk1Kw=s176-c-k-c0x00ffffff-no-rj" width="100px;" alt="freeCodeCamp.org"/><br>
        <sub>
          <b>freeCodeCamp.org</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://www.youtube.com/@DennisIvy">
        <img src="https://yt3.googleusercontent.com/ytc/AOPolaRYDmFeW15xdieLdvxXXspEidhG6zvZ_k3iUiOoRg=s176-c-k-c0x00ffffff-no-rj" width="100px;" alt="Dennis Ivy"/><br>
        <sub>
          <b>Dennis Ivy</b>
        </sub>
      </a>
    </td>
<td align="center">
      <a href="https://www.youtube.com/@Codemycom">
        <img src="https://yt3.googleusercontent.com/ytc/AOPolaTLKrm1mKm_4KBznZxMmeMfh7HPhLkzMel9Ydil=s176-c-k-c0x00ffffff-no-rj" width="100px;" alt="Codemy.com"/><br>
        <sub>
          <b>Codemy.com</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://www.youtube.com/@DevOpsJourney">
        <img src="https://yt3.googleusercontent.com/dQk85R0vZ_EKoE7BgbwMFIcmovijvOsbMD3DQJ26_j1hr5CYMeSSmHez9urr7A1zRcrpcVvoGeI=s176-c-k-c0x00ffffff-no-rj" width="100px;" alt="DevOps Journey"/><br>
        <sub>
          <b>DevOps Journey</b>
        </sub>
      </a>
    </td>
   <td align="center">
      <a href="https://docs.djangoproject.com/en/4.2/">
        <img src="https://img.stackshare.io/service/994/4aGjtNQv.png" width="100px;" alt="Django documentation"/><br>
        <sub>
          <b>Django documentation</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

## 🤝 Colaboradores

Agradecemos às seguintes pessoas que contribuíram para este workshop:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Kal-0">
        <img src="https://avatars.githubusercontent.com/u/106926790?s=400&u=d51d91a8d447afbb4a9d0be21d664b82d7091fc5&v=4" width="100px;" alt="Foto Kal"/><br>
        <sub>
		<b>Caio Cesar</b>
		<br>
		<b>Slack: ccbh@cesar.school</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Fiend3333">
        <img src="https://avatars.githubusercontent.com/u/116087739?v=4" width="100px;" alt="Foto Diogo"/><br>
        <sub>
		<b>Diogo Henrique</b>
		<br>
		<b>Slack: dhmc@cesar.school</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/virnaamaral">
        <img src="https://avatars.githubusercontent.com/u/116957619?v=4" width="100px;" alt="Foto Stora"/><br>
        <sub>
	        <b>Virna Amaral</b>
		<br>
		<b>Slack: vfpa@cesar.school</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Caiobadv">
        <img src="https://avatars.githubusercontent.com/u/117755420?v=4" width="100px;" alt="Foto Matheus Gomes"/><br>
        <sub>
		<b>Caio Barreto</b>
		<br>
		<b>Slack: cba2@cesar.school</b>
        </sub>
      </a>
    </td>
  </tr>
</table>
