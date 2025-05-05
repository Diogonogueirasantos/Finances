# Sobre o projeto
Bom a ideia por trás desse projeto surgiu pelo simples desejo de aplicar todo conhecimento que venho adquirindo sobre python e criações de interfaces gráficas, em um projeto real, apesar de ter a análise de dados como foco principal, não acho que seja de todo mal aprender sobre engenharia de software. Certo este projeto nada mais é que um programa de auxilio financeiro, sim, muito semelhante com as planilhas que costumamos usar para controlar nossas finanças, porém mais interativa (pelo menos é o que acredito ser). 

Gostaria de fazer uma breve observação sobre como a interface está sendo criada, apesar de conhecer o Qt_tools e todo o seu poder para a criação de uma interface, optei por escrever todo o código usando o módulo PyQt6, sim, escolhi o caminho mais "Díficil", como está é minha primeira vez tendo contato com este tipo de conceito acredito que usar o Qt_tools não me permitiria aprender o conceito por trás do desenvolvimento de interfaces.

***
## Dependências

A seguir você poderá ver sobre os pacotes necessários para o funcionamento do programa:

* PyQt6
* Sqlite3
* Mariadb (Futura implementação)

### IDE utilizada
* Pycharm Community

 ***

# Instalação dos módulos 
**I**. Lembre-se de criar um ambiente virtual para evitar a ocorrência de conflitos de pacotes com o ambiente raiz do seu sistema:

**Linux**


 		python3 -m venv <nome_ambiente>

**Windows**
		
		python -m venv <nome_ambiente>


**II**. Ative o seu ambiente virtual e instale os pacotes necessários:

**Linux**

		source <caminho_ambiente_virtual/bin/activate>	
		pip3 install PyQt6

**Windows**

		<caminho_ambiente_virtual\Scripts\activate.bat>
		pip install PyQt6

**III**. Agora basta entrar no diretório **Sql_version** e rodar o seguinte comando:

**Linux**

		python3 interface.py


**Windows**

		python -m interface.py


***

#### Contato
Bom, caso tenha algum problema ou sugestão para o projeto, basta entrar em contato com **Email** ou **Linkedin**. Até uma próxima.