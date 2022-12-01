
extern "C" {
////////////////////////////////////////////////////////////////////////////////
// timer

static void timer_setup(void);
static void timer_setup(void) {
  // empty
}

static void timer_set_now(uint32_t *last_usp);
static void timer_set_now(uint32_t *last_usp) {
  *last_usp = micros();
}

static bool timer_elapsed(uint32_t *last_usp, uint32_t delay_us);
static bool timer_elapsed(uint32_t *last_usp, uint32_t delay_us) {
  uint32_t now_us;
  timer_set_now(&now_us);
  if((now_us - *last_usp) >= delay_us) {
    *last_usp = now_us;
    return true;
  }
  else {
    return false;
  }
}

////////////////////////////////////////////////////////////////////////////////
// serial

const uint32_t serial_baud = 38400UL;  // otherwise, maybe 9600UL;
const uint32_t serial_version = 123456UL;
static struct {
  char ch;
  char *python_command;
  char *responses;
  char *desc;
} serial_interface[] = {
#include "serial_interface.h"
};
const int serial_interface_count = sizeof(serial_interface) / sizeof(serial_interface[0]);

//const uint32_t serial_timeout_us = 100000UL;  // 100 ms
const uint32_t serial_timeout_us = 3000000UL;  // 3 s  // debug

static void serial_setup(void);
static void serial_setup(void) {
  Serial.begin(serial_baud);
  while(!Serial);
}

static uint8_t serial_interface_lookup(char ch);
static uint8_t serial_interface_lookup(char ch) {
  uint8_t idx;
  for(idx = 0; idx < serial_interface_count; idx++) {
    if(serial_interface[idx].ch == ch) {
      return idx;
    }
  }
  while(1);  // handle lookup failed error by halting
}

static void serial_command(char ch);
static void serial_command(char ch) {
//  return; // debug
  uint32_t last_us;
  
  uint8_t idx = serial_interface_lookup(ch);
  
  while(1) {  // infinite attempts to send
    Serial.print(F("<"));
    Serial.print(ch);
    Serial.println(F(">"));
    
    timer_set_now(&last_us);
    while(!Serial.available()) {
      if(timer_elapsed(&last_us, serial_timeout_us)) {
        break;
      }
    }
    
    if(Serial.available()) {
      char response = Serial.read();
      if(strchr(serial_interface[idx].responses, response)) {
        if(response == 'K') {
          return;  // command was sent
        }
        // else response == '?': treat as bad response
      }
      // handle bad response by resending
    }
  }
}

////////////////////////////////////////////////////////////////////////////////
// blink

static uint8_t blink_pin = 13;  // on board LED, may interfere with SPI
static bool blink_state;

const uint32_t blink_period_us = 1000000UL;
const uint32_t blink_toggle_delay_us = blink_period_us / 2;

static uint32_t blink_last_us;

static void blink_setup(void);
static void blink_setup(void) {
  pinMode(blink_pin, OUTPUT);
  blink_state = HIGH;
  digitalWrite(blink_pin, blink_state);
  
  timer_set_now(&blink_last_us);
}

static void blink_toggle(void);
static void blink_toggle(void) {
  blink_state = !blink_state;
  digitalWrite(blink_pin, blink_state);
  
  if(blink_state == HIGH) {
    serial_command('H');
  }
  else {
    serial_command('L');
  }
}

////////////////////////////////////////////////////////////////////////////////
// setup and loop

void setup(void) {
  timer_setup();
  serial_setup();
  blink_setup();
  
  serial_command('R');
}

void loop() {
  if(timer_elapsed(&blink_last_us, blink_toggle_delay_us)) {
    blink_toggle();
  }
}

////////////////////////////////////////////////////////////////////////////////
// end of code
}
  
