# corsairBacklitPipe

Toma el color que está debajo del mouse y hace el cambio de color en el retroiluminado del teclado. 

Test: Corsair K55

Librería para teclado en Linux: [CKB-Next](https://github.com/ckb-next/ckb-next)

Seleccionar animación Pipe y configurar el nombre a /tmp/ckbpipe012 (u otro nombre y modificarlo en el script)

## Daemonize Python
Ejecute el script de python, es suficiente para iniciar en modo background. Para detenerlo, utilice el comando kill.

## Bash script GIT
### Al actualizar el prompt:
En .zshrc o .bashrc insertar
```
if [ -p '/tmp/ckbpipe012' ]; then
        PS1+='$(ckbgit)'
fi
```
### Cargar script
Es necesario copiar el script *ckbgit* a un directorio que esté en PATH. Por ejemplo /home/miusuario/.local/bin o /usr/bin y darle permisos de ejecución para todos.

Si quiere, puede agregar un nuevo PATH en .zshrc o .bashrc
```
PATH+=":/home/miusuario/bin/"
```

