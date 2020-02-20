// Initial version: taken from https://github.com/miguelbalboa/rfid/blob/268682dc0b1aabc2d285c31f296659981540967f/examples/Ntag216_AUTH/Ntag216_AUTH.ino
// Thanks to GARGANTUA from RoboCreators.com & paradoxalabs.com for initial version

// This version has been written by Luca Ferroni IIS Merloni Miliani
// for the NAOCHALLENGE 2020

#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN    9   // 
#define SS_PIN    10    //

MFRC522 mfrc522(SS_PIN, RST_PIN); // Create MFRC522 instance

void setup() {
  Serial.begin(9600);   // Initialize serial communications with the PC
  while (!Serial);    // Do nothing if no serial port is opened (added for Arduinos based on ATMEGA32U4)
  SPI.begin();      // Init SPI bus
  mfrc522.PCD_Init();   // Init MFRC522
  Serial.println(F("Scan PICC to see UID, type, and data blocks..."));
}

void loop() {
  // Reset the loop if no new card present on the sensor/reader. This saves the entire process when idle.
  if ( ! mfrc522.PICC_IsNewCardPresent()) {
    return;
  }

  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial()) {
    return;
  }

  byte PSWBuff[] = {0xFF, 0xFF, 0xFF, 0xFF}; //32 bit PassWord default FFFFFFFF
  byte pACK[] = {0, 0}; //16 bit PassWord ACK returned by the NFCtag

  Serial.print("Auth: ");
  Serial.println(mfrc522.PCD_NTAG216_AUTH(&PSWBuff[0], pACK)); //Request Authentification if return STATUS_OK we are good

  //Print PassWordACK
  Serial.print(pACK[0], HEX);
  Serial.println(pACK[1], HEX);

  byte WBuff[] = {0x00, 0x00, 0x00, 0x04};
  byte RBuff[18];

  //mfrc522.PICC_DumpMifareUltralightToSerial(); //This is a modifier dunp just cghange the for cicle to < 232 instead of < 16 in order to see all the pages on NTAG216
  MFRC522::StatusCode status;
  byte byteCount;
  byte buffer[18];
  byte nfc_data[256];
  byte index = 0;
  byte i;
  // Try the mpages of the original Ultralight. Ultralight C has more pages.
  for (byte page = 0; page < 16; page +=4) { // Read returns data for 4 pages at a time.
    // Read pages
    byteCount = sizeof(buffer);
    status = mfrc522.MIFARE_Read(page, buffer, &byteCount);
    if (status != mfrc522.STATUS_OK) {
      Serial.print(F("MIFARE_Read() failed: "));
      Serial.println(mfrc522.GetStatusCodeName(status));
      break;
    }

    //Put results in a common array
    for (i=0; i<16; i++) {
        nfc_data[index] = buffer[i];
        index++;
    }
  }

  Serial.println("-- HO LETTO I DATI NEL TAG RFID NTAG213 --");
  //Print URL type
  switch (nfc_data[27]) {
    case 1:
      Serial.print("http://www.");
      break;
    case 2:
      Serial.print("https://www.");
      break;
    case 3:
      Serial.print("http://");
      break;
    case 4:
      Serial.print("https://www.");
      break;
    case 5:
      Serial.print("tel:");
      break;
    case 6:
      Serial.print("mailto:");
      break;
  }
  
  for (i=28; i<255; i++) {
    if (nfc_data[i] == 0xFE) // End of string
      break;
    
    // Serial.print(nfc_data[i]);
    // Serial.print(F(" ")); // Pad with spaces
    Serial.print((char)nfc_data[i]);
  }

  Serial.println();
  delay(3000);
}
