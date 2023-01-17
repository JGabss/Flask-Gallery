# Sobre o trabalho
 Salve, salve, esse trabalho foi desenvolido para a disciplina de Desenvolvimento de Aplicações Web do IFPB - Campus Cazeiras, por:
 * Cauã Roberto Vieira de Sousa
 * Gustavo Lopes Lemos 
 * José Gabriel Abreu Moreira
 * Raynara Lima de Sousa
 
 A aplicação consiste em um sistema para geração e armazenamento de imagens, uma galeria (utilizando como base a API e IA da DALL-E 2), sendo possível realizar o CRUD por completo dessas informações,  
 
# Como usar:
 Acredito que se estás aqui, queira utilizar e vizualizar o projeto.
 
 Para isso, primeiramente clone o repositório para sua máquina, através do comando: <code>git clone https://github.com/JGabss/Flask-Gallery.git</code>
 Feito isso, belezura, agora é necessário instalar as bibliotecas usadas, seja localmente seja em um ambiente virutal (recomendo essa segunda), para isso use o comando; <code> pip install -r requirements.txt</code>
 <br>
 <br>
 Se deu tudo certo até aqui, comemoremos, mas agora é preciso configurar os settings da aplicacação, assim como seu banco de dados. Para isso, por uma questão de seguranças não foram disponibilizados algumas variáveis, mas foi disponibilizado um arquivo env-sample, basta criar um arquivo .env copiar o que estava escrito no arquivo env-sample e preencher com os dados necessários.
 No campo API_KEY, se tiver como falar comigo eu lhe disponibilizo uma, senão terá que gerar uma no site da openai
 <br>
 <br>
 Tenho fé, que preenchera tudo corretamente, com os dados do seu computador e afins, configurando  nosso banco, digite os seguintes comandos:
 <br>
 <code> flask -A app db init </code>
 <br>
 <code> flask -A app db migrate </code>
 <br>
 <code> flask -A app db upgrade </code>
 <br>
 
 se deu tudo certo, tá pronto, então basta rodar com um <code>flask -A app run</code> e, teoricamente ksksksk, é para funcionar.
 
