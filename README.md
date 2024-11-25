# Enumeración de boletos con python

![](/python.png)


### Descripción

Este script automatiza la numeración de boletos en un archivo PDF. A partir de un archivo PDF de plantilla, genera un nuevo documento donde cada boleto es numerado en un formato específico. Los boletos se distribuyen en páginas tamaño oficio (legal) y se numeran secuencialmente.

----

**Explicación**

A partir de una imagen(boleto inicial), crear una repetición en un documento pdf según los boletos que se desear tener en una hoja.
![Imagen del boleto inicial](/boleto.png "width: 20%; height: 200px")
La repetición se puede hacer directamente con algun editor como *word*, *publisher*, *canva* entre otros, eso no quiere decir con **python** no se pueda hacer, sin embargo la finalidad de esto, unicamente es la  **enumeración de cada boleto**.

[Plantilla inicial]([/bol_oficio.pdf)

Primeramente necesitamos tener instalado la biblioteca  `<PyPDF2>` en caso de no tenerla, instalarla con el siguiente comando:

`pip install PyPDF2`

Si se esta trabajando en *google colab* esto no es necesario.
___
**Coordenadas de enumeración**
Ademas segun el acomodo de los boletos en el documento pdf, debemos de saber las coordenas, considerando que en un pdf las coordenas `(0,0)` inician en el la esquina inferior izquierda, hacia la derecha aumenta en `x` y hace arriba aumenta en `y`.
Lo mas conveniente en este caso es establecer una matriz para las coordenas, *en mi caso cada boleto debe de llevar dos veces el mismo numero, como encabezado y pie de página* por lo tanto la matriz resultante fue:

```python
positions = [
        # Boleto 1: inicio y final
        (52, 902), (570, 902),
        
        # Boleto 2: inicio y final
        (52, 727), (570, 727),
        
        # Boleto 3: inicio y final
        (52, 545), (570, 545), 
        
        # Boleto 4: inicio y final
        (52, 352), (570, 352),
        
        # Boleto 5: inicio y final
        (52, 167), (570, 167),  # Aumentado el Y
    ]
```

En caso de no saber las coordenas, se puede emplear algun software para indentificarlas o bien mediante **prueba y error**.
___
**Tipo de hoja**
> letter
> legal

Hojas mas comunes *aunque puede ser cualquier tipo de tamaño* estas se definen en la importación de nuestro código de la siguiente manera:
`from reportlab.lib.pagesizes import legal`
Tambien sera necesario asiganarle este tamaño al objeto canvas *(apartado de personalización)*.
___
**Enumeración**
Podemos elegir entre una gran variación de opciones, segun nuetro criterio:

* Con algun prefiejo (111... , AA...)
* Con algún sufijo (...00, ...ABC)
* Con letras ramdon
* Con numeros ramdon(entre ciertos números)

Y asi tenemos muchimas más opciones.

## Personalización
`c = canvas.Canvas(packet, pagesize=legal)`
Mediante el objeto canvas, es posible personalizar el color, la orientacion, tamaño, estilo, entre otras muchas cosas.

```python
 c.setFont("Helvetica-Bold", 14)
    c.setFillColorRGB(1, 1, 1)  # Color blanco
```

## Ejecución
Se ejecuta desde el método main: `if __name__ == "__main__"` aqui se estableces los valos como la cantidad de boletos, nombre de la *plantilla inicial*, nombre del archivo de salida, enumeracion inicial.

```python
if __name__ == "__main__":
    number_tickets(
        input_pdf_path="bol_oficio.pdf",
        output_pdf_path="boletos_finales.pdf",
        start_number=11001,
        total_tickets=250
    )

```

___

 ### Dependencias

* `PyPDF2`: Para manipulación de archivos PDF (lectura, escritura y edición).
* `ReportLab`: Para generar contenido dinámico, como la capa con números sobre los boletos.
* `math`: Para cálculos matemáticos, como redondeo.
* `io.BytesIO`: Para manejar datos binarios en memoria.

#### Importaciones:

* `PdfReader`, `PdfWriter`, y `PageObject` de **PyPDF2**: Permiten leer, escribir y crear páginas PDF.
* `canvas` y `legal` de **ReportLab**: Utilizados para dibujar texto y definir el tamaño de página.
* `BytesIO`: Almacena datos de manera temporal en memoria.

### End
[![My Skills](https://skillicons.dev/icons?i=python)](https://skillicons.dev)

#### 🌐 Redes:
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=Instagram&logoColor=white)](https://instagram.com/stbn27) 
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/estebanjose27) 
[![Github](https://img.shields.io/badge/github-%23171515.svg?logo=GitHub&logoColor=white)](https://github.com/stbn27) 
