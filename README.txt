Instalar Requerimientos
pip install -r requirements.txt


Iniciar proyecto
python main.py


* Se recomienda tener un "enviroment" con python versión > 3.0 (versión usada Python 3.7.3)
Para más información consultar :  https://docs.python.org/3/library/venv.html

*Si llega a obtener un error al generar el grafo es por algunas dependencias. Para corregir, es necesario instalar el paquete de graphviz

Para windows(tested) : 
	Instalar paquete https://graphviz.gitlab.io/_pages/Download/Download_windows.html
	Añadir variable de entorno "User PATH y System PATH" C:\Program Files (x86)\Graphviz2.38\bin
 
Para MAC OS:
	brew install graphviz

Para Linux (tested):
	sudo apt-get install graphviz
 
