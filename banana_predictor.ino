char estadoPlatano;

const int ledVerde = 2;    // Unripe
const int ledAmarillo = 3; // Ripe
const int ledNaranja = 4;   // Overripe

void setup() {
  Serial.begin(9600); // Comunicación con COM4
  pinMode(ledVerde, OUTPUT);
  pinMode(ledAmarillo, OUTPUT);
  pinMode(ledNaranja, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    estadoPlatano = Serial.read();

    // Apagar todos
    digitalWrite(ledVerde, LOW);
    digitalWrite(ledAmarillo, LOW);
    digitalWrite(ledNaranja, LOW);

    // Encender solo uno
    if (estadoPlatano == 'U') {
      digitalWrite(ledVerde, HIGH);
    } else if (estadoPlatano == 'R') {
      digitalWrite(ledAmarillo, HIGH);
    } else if (estadoPlatano == 'O') {
      digitalWrite(ledNaranja, HIGH);
    }
  }
}
