void setup() {
  Serial.begin(9600);
}

void loop() {
  float latitud = random(-9000.000, 90.000);
  float longitud = random(-18000.000, 180.000);
  String datos = "$GNGGA,125335.123," + String(latitud) + ",N," + String(longitud) + ",W,12345.67890";
  Serial.println(datos);
  delay(1000);
}
