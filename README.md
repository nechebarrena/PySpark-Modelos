# PySpark
## Modelos

La idea de este repo es probar distintos modelos basicos de DS utilizando PySpark. El modelo clasificador lo heredo de otro repo anterior. A este voy a sumar en primera instancia un modelo regresor.

Primeras pruebas de un clasificador utilizando Pyspark.

Uso un docker con una instalacion ya hecha de Pyspark. Para bajarlo hay que tener instalado Docker y ejecutar:
```bash
sudo docker run -v $PWD:/home/jovyan/work/ -p 8888:8888 jupyter/pyspark-notebook
```
El docker viene con un arbol de directorios `/home/jovyan/work/`. Por simplicidad voy a poner el codigo y cualquier archivo que necesite ahi mismo. Para poder modificar el archivo localmente y que este repercuta en el docker uso `-v`. 

La primera vez que corra este comando va a decirme que no encuentra localmente esta imagen y la va a bajar de dockerhub. Luego, cada vez que lo ejecute, va a buscar la imagen local. Una vez que tengo la imagen corriendo puedo ejecutar:

 ```bash
docker container ls
```

 para ver la lista de imagenes corriendo. Si ejecuto 
```bash
docker exec -it ID bash
```
"Entro" al bash de la imagen. Una vez "dentro" puedo ir al directorio donde tengo el programa y ejecutarlo con:
```bash
spark-submit clasificador.py 
```


