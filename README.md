# obligatorio_p1_2025
Trabajo obligatorio_Programación1_Universidad_De_Montevideo

Descripción del sistema

Una fábrica de máquinas agrícolas desea informatizar la gestión de su producción,
inventario y ventas para poder brindar un mejor servicio a sus clientes. Para ello se deberá
implementar un programa en Python en modo consola, seleccionando opciones de un menú
en la terminal de comandos.

El objetivo es gestionar el stock de piezas (materiales necesarios para construir las
máquinas) disponibles y faltantes, el conjunto de máquinas a producir, indicando los
requerimientos de piezas que necesita cada una para ser fabricada, y el conjunto de
clientes con los pedidos que estos realizan.

Al momento de registrar los pedidos de clientes, se debe comprobar la disponibilidad actual para poder cumplir con el pedido, por lo que existirán pedidos entregados y otros pendientes por falta de stock. Deberán realizarse
reposiciones de stock para completar los pedidos pendientes dadas las piezas faltantes.

Además, se requiere llevar un registro contable de las compras de piezas para reponer el
stock, las ventas de máquinas a los clientes y la ganancia total resultante. Se pedirán
listados variados, a los efectos de controlar el stock, pedidos, clientes, etc.


Funcionalidades a aplicar

1. Registrar una nueva pieza, ingresando su descripción, costo y cantidad disponible.
2. Registrar una nueva máquina, indicando una descripción y los requerimientos de piezas necesarias.
3. Registrar clientes con datos de identificación y contacto, los cuales pueden ser de tipo cliente particular o empresa.
4. Registrar el pedido de un cliente para comprar una máquina.
5. Marcar como entregado o pendiente un pedido, según la disponibilidad actual de piezas.
6. Registrar reposiciones de piezas del stock, según la cantidad de lotes comprados.
7. Actualizar automáticamente el stock cuando se entrega un pedido, se ingresa una nueva pieza o se registra una reposición.
8. Gestionar automáticamente los pedidos pendientes, pasándose a estado “entregado” cuando puedan ser cubiertos luego de reponer el stock.
9. Listar datos de clientes.
10. Mostrar listado de pedidos, pudiendo filtrar por estado entregado o pendiente.
11. Mostrar listado de piezas, indicando disponibilidad y cantidad faltante para completar pedidos pendientes si corresponde.
12. Listar las máquinas, detallando costo, precio y disponibilidad.
13. Mostrar el desglose de ventas y costos asociados, junto a la ganancia total resultante.

Clases

1. Sistema: clase general que contiene los conjuntos de cada tipo de objeto (clientes, piezas, máquinas, etc.).
2. Pieza: representa los elementos que están en el stock.
3. Maquina: define qué piezas necesita para fabricar un producto.
4. Requerimiento: cantidad necesaria de una pieza para una máquina particular.
5. Cliente: representa a los clientes que hacen pedidos. Es una clase abstracta a partir de la cual se definen las siguientes clases heredadas:
    a. ClienteParticular
    b. Empresa
6. Pedido: representa un pedido recibido de un cliente para comprar una máquina. El estado del pedido puede ser “entregado” o “pendiente”.
7. Reposición: se utiliza para registrar las compras de piezas para reponer el stock.
8. Excepciones: una clase por cada tipo de error en tiempo de ejecución que los
programadores quieran controlar


<img width="288" alt="image" src="https://github.com/user-attachments/assets/1bbdf67a-cbb1-449a-bb0e-98c8321e4a05" />
