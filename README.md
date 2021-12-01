# Prueba técnica Fintual 

Hola si estás viendo esto es porque te han asignado revisar ésta prueba técnica. 

La realicé con el framework django y la librería restframework ya que llevo un tiempo trabajando con API's simples en distintos lenguajes. 

Espero les sirva de ayuda para concerme y ver si les gusta mi forma de trabajo. 


## Reqerimiento 
Construct a simple Portfolio class that has a collection of Stocks and a "Profit" method that receives 2 dates and returns the profit of the Portfolio between those dates. Assume each Stock has a "Price" method that receives a date and returns its price.
Bonus Track: make the Profit method return the "annualized return" of the portfolio between the given dates.


## Prerequisitos

Python 3.7 o superior
## Instalación

Para probar el proyecto debes seguir los siguientes pasos:

+ clonar el proyecto 
```
    https://github.com/mario-gg/test-fintual.git
```
 +Ingresar al directorio de la apliación 

+ crear un entorno virtual
```
    python3 -m venv <name_of_virtualenv>
```
+ instalar paquetes usando pip 
```
    pip install -r requirements.txt
```
+ ingresar a la carpeta "fintual"

+ ejecutar el comando python manage.py runserver

una vez levantado el proyecto en local puedes probar la función profit en la siguiente url:

```
http://127.0.0.1:<puerto>/portfolio/profit/?start_date={FECHA-INICIO}&end_date={FECHA-FIN}
```



