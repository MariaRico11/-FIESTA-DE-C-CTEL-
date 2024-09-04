### FIESTA DE CÓCTEL
En un evento tipo cóctel, se instalaron varios micrófonos con el fin de capturar las conversaciones de los asistentes. 
Al concluir la fiesta, se solicitó a los ingenieros que extrajeran el audio de la voz de uno de los participantes. 
Sin embargo, al analizar las grabaciones, los ingenieros encontraron que las señales capturadas por los micrófonos eran una mezcla de sonidos provenientes de distintas fuentes (personas), 
lo que presentó el desafío de aislar la voz deseada. Este escenario se conoce como el **"problema de la fiesta de cóctel"**, el cual se refiere a la capacidad de un sistema para enfocarse en 
una única fuente sonora mientras filtra las demás en un entorno con múltiples emisores de sonido. 
Este problema es común tanto en sistemas auditivos humanos como en sistemas artificiales, y su resolución es crucial para aplicaciones como la mejora de la voz, el reconocimiento del 
habla y la cancelación de ruido.

En la segunda practica de laboratorio de procesamiento digital de señales, se busca replicar el problema de la fiesta de cóctel, donde existen 𝑛 fuentes sonoras capturadas por un arreglo 
de 𝑛 micrófonos, siguiendo la siguiente metodología:

**1.	Configuración del sistema:**
- Se conectaron tres micrófonos de celular, ubicados estratégicamente en la sala a una distancia de **0.8 m** entre sí. Estos micrófonos fueron dispuestos para captar diferentes combinaciones de las señales emitidas por las tres fuentes.
  Cada micrófono fue calibrado con una **frecuencia de muestreo de 44 kHz** y un **nivel de cuantificación de 160 kbps**.
  
- En una sala insonorizada, se colocaron tres personas en posiciones fijas, cada una a una distancia de **0.8 m** y orientada frente a uno de los micrófonos, para simular
   un entorno típico de **"fiesta de cóctel"**.
   
   ![image](https://github.com/user-attachments/assets/9f9a00a9-b47e-4edb-85aa-2430913b9b57)
   
**2.	Captura de la señal:**
- La señal se generó utilizando las voces de los tres sujetos de prueba; cada uno de ellos pronunció una frase diferente durante el tiempo de captura de la señal, que fue de **6 segundos**.
  Las señales captadas por los micrófonos fueron registradas por el sistema de adquisición de datos y guardadas para su posterior análisis.

  ###### FRASES PRONUNCIADAS:
  ###### -	DANIELA: "No es tan facil cambiar el corazón, pero podemos persuadir a la mente".
  ###### -	LEONARDO: "Anna ¿Qué sabes de amor de verdad?" Más que tu. Tu solo sabes alejar a la gente".
  ###### -	MARIANA: "La luz esta entrando en el salón, por fin se ilumina cada rincon"
  
![image](https://github.com/user-attachments/assets/3cdd5fde-7e5d-4951-b137-5f627bd0ff43)

> **Ejes de la Gráfica:**

> **-	Eje Vertical (Amplitud):** Representa la amplitud de la señal de audio captada por el micrófono. La amplitud está directamente relacionada con la intensidad del sonido, donde valores más altos indican sonidos más fuertes.

> **-	Eje Horizontal (Tiempo):** Muestra el transcurso del tiempo durante la grabación. Este eje permite observar cómo varía la amplitud de la señal a lo largo del tiempo, proporcionando una visión dinámica de la evolución del sonido.

-	Se realizó la grabación del ruido ambiente en la sala insonorizada utilizando los tres micrófonos. A partir de estas grabaciones, se calculó la Relación Señal-Ruido (SNR),
   un parámetro crucial que mide la diferencia entre la señal de audio deseada y el ruido no deseado capturado por el micrófono.

 	En cuanto a los resultados obtenidos en la relación señal/ruido (SNR) para cada uno de los tres micrófonos:
  ###### *-	Micrófono 1 (18.82 dB):* Presenta la relación señal/ruido más baja, lo que indica que la señal capturada por este micrófono tiene mayor interferencia de ruido en comparación con los otros dos.
  ###### *-	Micrófono 2 (29.99 dB):* Muestra la relación señal/ruido más alta, lo que sugiere que la señal de este micrófono es la más clara y tiene menos interferencia de ruido de fondo.
  ###### *-	Micrófono 3 (20.56 dB):* Tiene una calidad intermedia, con un SNR mejor que el del Micrófono 1, pero inferior al del Micrófono 2.

Es importante considerar que la amplitud de la señal juega un papel crucial en el análisis del SNR. Cuando la señal tiene una alta amplitud y el ruido una amplitud baja, el SNR será elevado, lo que indica una buena calidad de la señal. Por el contrario, si la señal tiene una amplitud baja y el ruido una amplitud comparable, el SNR será bajo, 
indicando una señal más afectada por el ruido.

**3.	Procesamiento de señales:**
- Se realiza un análisis temporal y espectral de las señales capturadas por cada micrófono, con el objetivo de identificar las características principales de cada fuente sonora. Para el análisis espectral, se emplea la Transformada Rápida de Fourier (FFT), una herramienta esencial en el análisis de señales que convierte una señal del dominio
  temporal al dominio de la frecuencia.
  
  ![1](https://github.com/user-attachments/assets/29461f0e-88f4-4191-aa0a-761c451922d6)
  ![2](https://github.com/user-attachments/assets/bdb1c8d9-ecc8-41d9-bf8b-bf9a03c910cf)
  ![3](https://github.com/user-attachments/assets/0c197dab-9902-4f8e-900a-ef298034ac0f)

> **Dominio de la Frecuencia:**

> **- Eje Horizontal (Frecuencia):** Representa las frecuencias en hertzios (Hz) presentes en la señal.

> **- Eje Vertical (Magnitud):** Muestra la magnitud de cada componente de frecuencia en la señal.
  
La FFT descompone la señal en sus frecuencias constituyentes, revelando picos que indican las frecuencias predominantes. Cada pico en la gráfica representa una frecuencia específica en la que la señal tiene una mayor amplitud,
lo que sugiere que en la señal original existen componentes sonoros dominantes en esas frecuencias.

-	la investigar los métodos de separación de fuentes, se optó por utilizar la **técnica de beamforming**. Esta técnica de procesamiento de señales permite dirigir la recepción o transmisión de señales hacia una dirección específica, mejorando la calidad de la señal y reduciendo el ruido de fondo. El beamforming es comúnmente aplicado en sistemas de audio,
  comunicaciones y radar.
 	
  La técnica permite que un sistema, como un arreglo de micrófonos, enfoque su sensibilidad en una dirección particular. Esto es útil para captar señales de interés mientras se minimizan las interferencias provenientes de otras direcciones. Además, el beamforming mejora la Relación Señal-Ruido (SNR) al concentrar la captura del sonido en una dirección específica, 
  lo que puede aumentar significativamente la calidad de la señal. Esta mejora es crucial en aplicaciones como conferencias telefónicas y grabaciones de audio en entornos ruidosos.

  La técnica de beamforming tiene un ancho de banda finito, lo que significa que solo puede enfocar un rango limitado de frecuencias a la vez. Esta limitación puede provocar distorsión fuera del rango de frecuencias para el que el beamformer está optimizado. Además, si los micrófonos no están perfectamente posicionados o calibrados,
  los errores resultantes pueden introducir distorsión en la señal enfocada, afectando la calidad general del audio capturado.

  ![image](https://github.com/user-attachments/assets/d8defaf7-4dd7-41f2-a92e-cee8acfb8f1e)

  Un SNR de 0.10 dB significa que la señal deseada y el ruido están casi al mismo nivel, lo que indica que la señal no se diferencia lo suficiente del ruido. Este resultado puede ser sorprendente, ya que un valor tan bajo, sugiere que la voz que se intentó filtrar se escucha mejor que el ruido producido por las otras voces, 
  a pesar de haber aplicado beamforming para intentar mejorar la calidad de la señal.

### Preguntas para el estudiante:
  
 -**¿Cómo afecta la posición relativa de los micrófonos y las fuentes sonoras en la efectividad de la separación de señales?**
 
La efectividad de la separación de señales en sistemas de beamforming que utilizan tres micrófonos depende en gran medida de la posición relativa de los micrófonos y las fuentes sonoras.

•	**Orientación de los micrófonos:** Para maximizar la efectividad del beamforming, es esencial que los micrófonos estén correctamente orientados hacia las fuentes sonoras. Se recomienda el uso de micrófonos direccionales, que pueden enfocarse en la fuente deseada y minimizar el ruido de fondo. Una orientación incorrecta puede resultar 
en una captura ineficaz de la señal deseada y la inclusión de sonidos no deseados.

•	**Ruido de fondo:**  La efectividad del beamforming puede verse afectada por la presencia de ruido ambiental. Si los micrófonos están demasiado alejados de la fuente deseada, es más probable que capten ruido ambiental, lo que dificulta la separación de la señal deseada. 
Por lo tanto, es crucial considerar la relación señal-ruido en la configuración.

•	**Características de las fuentes sonoras:** La direccionalidad y el volumen de las fuentes sonoras también influyen en la separación de señales. Fuentes que emiten en diferentes direcciones pueden ser más fácilmente separadas si los micrófonos están bien posicionados 
para captar las diferencias en el tiempo de llegada de las ondas sonoras.

-**¿Qué mejoras implementaría en la metodología para obtener mejores resultados?**

Para optimizar la metodología en la técnica de beamforming y obtener mejores resultados, se pueden aplicar varias estrategias que abordan tanto el diseño del sistema como los algoritmos de procesamiento:

•	**Ajuste de la Configuración Geométrica:** Configurar los micrófonos de manera que maximicen la separación espacial, como en arreglos en forma de triángulo o en línea, mejora la capacidad del sistema para detectar diferencias en el tiempo de llegada de las señales de diferentes fuentes sonoras. 
Esta configuración es esencial para la efectividad del beamforming.

•	**Selección de Micrófonos Direccionales:** Utilizar micrófonos con patrones de captación direccional ayuda a enfocar la señal en la fuente deseada, reduciendo al mismo tiempo la captación de ruido ambiental.

•	**Filtrado Avanzado:** Implementar técnicas de filtrado que eliminen el ruido de fondo antes de aplicar el beamforming puede mejorar significativamente la calidad de la señal. Esto incluye el uso de filtros adaptativos que se ajusten dinámicamente a las características del ruido en el entorno.

•	**Uso de Técnicas de Visualización:** Incorporar herramientas de visualización que muestren el rendimiento del beamformer en tiempo real puede facilitar el ajuste de la configuración y optimizar la captación de señales durante su uso.

### INSTRUCCIONES 
Este código está diseñado para ser utilizado en la plataforma Spyder. Para ejecutarlo correctamente, sigue estos pasos:

**1.	Instalación de librerías:** Asegúrate de instalar las librerías necesarias en la consola usando los siguientes comandos:
>	 pip install librosa

>	 pip install matplotlib

>	 pip install numpy

>	 pip install soundfile

**2.	Configuración de los archivos de audio:** Cambia los nombres de los archivos de audio dentro del código por los correspondientes a tu proyecto.
   Todos los archivos de audio deben estar guardados en la misma carpeta.
   
**3.	Duración de los audios:** Es importante que todos los audios tengan la misma duración.

**4.	Grabación de ruido ambiental:** Asegúrate de grabar el ruido del ambiente, ya que será necesario para el procesamiento adecuado del código.







