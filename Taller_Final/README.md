# Ciberseguridad en el Internet de las Cosas (IoT)

El Internet de las Cosas (IoT) ha transformado la forma en que interactuamos con el mundo, conectando miles de millones de dispositivos que van desde electrodomésticos inteligentes hasta maquinaria industrial. Sin embargo, esta vasta interconexión también ha abierto una nueva y compleja frontera para la ciberseguridad. Este README explora los desafíos actuales, los protocolos, el cifrado y los ataques más comunes en el entorno IoT.

---

## Desafíos Actuales de la Ciberseguridad en IoT

La naturaleza intrínseca de los dispositivos IoT presenta desafíos únicos en seguridad:

- **Heterogeneidad y diversidad**: Una amplia gama de dispositivos con distintas arquitecturas de hardware, sistemas operativos y capacidades.
- **Limitaciones de recursos**: Muchos dispositivos son de bajo costo y tienen restricciones de procesamiento, memoria y energía, lo que limita la implementación de soluciones de seguridad robustas.
- **Falta de seguridad desde el diseño**: Históricamente, la funcionalidad y el costo han predominado sobre la seguridad en el desarrollo de dispositivos IoT.
- **Ciclos de vida prolongados**: Algunos dispositivos IoT operan durante años sin actualizaciones de seguridad, dejando vulnerabilidades expuestas.
- **Gestión y monitoreo a escala**: Dificultad para supervisar y gestionar la seguridad de millones de dispositivos conectados.
- **Privacidad de los datos**: Gran volumen de datos personales y sensibles recopilados, lo que genera preocupaciones sobre su uso y protección.

---

## Protocolos de Seguridad Utilizados en IoT

Los protocolos de comunicación en IoT buscan un equilibrio entre eficiencia y seguridad. A menudo, se combinan con otros protocolos para mejorar la protección:

- **MQTT**: Protocolo de mensajería ligero. Se complementa con TLS/SSL y autenticación de usuario/contraseña.
- **CoAP**: Diseñado para dispositivos restringidos. Utiliza DTLS para cifrado y autenticación.
- **HTTP/HTTPS**: HTTPS incorpora TLS/SSL para proteger la comunicación entre dispositivos y la nube.
- **DDS**: Utilizado en entornos industriales. Ofrece control de acceso, autenticación y cifrado.
- **Zigbee y Z-Wave**: Protocolos inalámbricos de bajo consumo para domótica. Incorporan cifrado AES y autenticación.
- **LoRaWAN**: Protocolo para redes de área amplia de baja potencia. Utiliza cifrado AES a nivel de red y aplicación.
- **Bluetooth Low Energy (BLE)**: Ofrece emparejamiento seguro y cifrado AES.

> Adicionalmente, la **Infraestructura de Clave Pública (PKI)** es fundamental para la gestión de certificados digitales y autenticación de dispositivos.

---

## Tipos de Cifrado en Dispositivos IoT

La elección del cifrado es crucial debido a las limitaciones de recursos de muchos dispositivos IoT:

### Cifrado Simétrico

- **AES (Advanced Encryption Standard)**: Eficiente y seguro (AES-128, AES-192, AES-256). AES-128 es el más común en IoT.
- **DES / 3DES**: Obsoletos y menos seguros. Poco usados en nuevas implementaciones.

### Cifrado Asimétrico (Criptografía de Clave Pública)

- **RSA**: Usa claves pública/privada. Se emplea en intercambio de claves y firmas digitales.
- **ECC (Elliptic Curve Cryptography)**: Igual de seguro que RSA pero con claves más pequeñas, ideal para IoT.

### Hashing

- **SHA-256, SHA-3**: Usados para verificar integridad de datos y almacenar contraseñas de forma segura.

> 📌 **Práctica común**: Usar **AES** para el cifrado de datos y **ECC** para autenticación e intercambio de claves.

---

## Ataques Más Frecuentes en el Entorno IoT

El amplio ecosistema IoT es un blanco atractivo para ciberataques:

- **DDoS y Botnets**: Dispositivos comprometidos usados en ataques masivos (ej. botnet Mirai).
- **Robo de Datos**: Acceso a información personal (ubicación, salud, hábitos).
- **Acceso No Autorizado**:
  - Contraseñas débiles o predeterminadas.
  - Explotación de vulnerabilidades de software/firmware.
  - Inyección de nodo malicioso.
- **Secuestro de Firmware (Firmware Hijacking)**: Instalación de firmware malicioso.
- **Ataques a la Cadena de Suministro**: Introducción de vulnerabilidades en diseño, fabricación o distribución.
- **Ataques Físicos / Manipulación de Sensores**: Acceso físico para alterar dispositivos.
- **Intercepción (Man-in-the-Middle)**: Intercepción y modificación de datos no cifrados.
- **Ataques de Downgrade**: Forzar uso de versiones inseguras de firmware o protocolos.

---
