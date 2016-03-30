# modulo-odoo
nuevo modulo para odoo
1.- Abrimos Netbeans, creo un proyecto php con servidor remoto. Configuramos con nuestra ip y usuario root para que tenga permisos de acceso a la carpeta addons de Odoo.

2.-Cargamos la carpeta en blanco donde irá nuestro modulo y creamos los archivos necesarios (openerp, init, modules, la carpeta view y por supuesto el xml de openacademy), a través del comando indicado scaffold

3.- Creamos una clase Course con el campo name en el archivo models. Luego las creamos un Curso predefinido en el xml de demo, podemos crear varios "Courses" por defecto.

4.- En el openacademy.xml creamos un menú de Courses, con el cual un usuario podrá modificar o crear sus propios Cursos. No hay que olvidarse de declarar el openacademy.xml en la "data" del openerp.py

5.- Configuramos nuestro openacademy.xml para que salga nuestro menú de Course a nuestro gusto, esta vez tendrá una "Form view".

6.- Añadimos un search_view en el openacademy.xml que nos servirá para buscar entre todos los titulos de cursos o por su descripción.

7.- Creamos un nuevo modelo llamado Session en models.py y creamos tambien su form view en el xml.

8.- Usamos los llamados one2many y many2one para crear "campos relacionales" entre los dos modelos, añadiendo en models.py las lineas necesarias y en openacademy.xml adaptamos las vistas.

9.- Creamos el fichero partner.xml en la carpeta views, partner.py en la carpeta raiz, añadimos en los datos del openerp el partnet.xml y importamos en parnet en el init. Con esto ya podremos crear herencias, las cuales un objeto nuevo puede "heredar" partes de un modelo ya existente.

10.- Añadimos campos calculados, el cual calculamos el valor de un cálculo. Le añadimos una progress bar. Añadimos tambien valores por defecto.

11.- Añadimos advertencias llamadas onChange en el models.py, las cuales nos dirán cuando un valor es inválido

