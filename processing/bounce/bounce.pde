float x; // horizonal position of puck
float y; // vertical position of puck
float dx = 2; // horizontal velocity of puck
float dy = 3; // vertical velocity of puck
float w = 10; // width (and height) of puck rectangle
float g = 0.1; // gravity (change in dy per unit time)

// paddle
float px = 100; // horizontal position of paddle
float py = 25; // vertical position of paddle
float pw = 100; // width of paddle
float ph = 10; // height of paddle

Color pColor = new Color(255, 0, 0); // puck color
Color bgColor = new Color(0, 0, 50); // background color; navy
Color fgColor = new Color(255, 255, 0); // foreground color; yellow


void setup() {
  size(480, 360);
  x = 0;
  y = height * 0.5;
  frameRate(30);
  background(bgColor.red, bgColor.green, bgColor.blue);
  noStroke();
}

void plot(Color c) {
  fill(c.red, c.green, c.blue);
  rect((int) x, height - (int) y, w, w);
}

void plotp(Color c) {
  noStroke();
  fill(c.red, c.green, c.blue);
  rect(px, height - py, pw, ph);
}

void draw() {
  // remove the previous
  plot(bgColor);

  // draw the paddle
  plotp(pColor);
  
  x = x + dx;
  if (x < w) {
    x = w;
    dx = -dx;
  }
  if (x + w >= width - w) {
    dx = -dx; // reverse horizontal direction
  }
  y = y + dy;
  if (y < w) {
    dy = -dy;
  }
  if (y < py + ph
      && x >= px
      && x + w < px + pw
      && dy < 0) {
    dy = -dy;
    pw = pw - 5;// make the paddle shorter
  }
  
  if (y + w >= height - w) {
    dy = -dy;
  }
  dy -= g;

  // paint the new rectangle
  plot(fgColor);
}

void keyPressed() {
  if (keyCode == RIGHT) {
    plotp(bgColor);
    px = px + 50;
    if (px+pw > width - w) px = width - w - pw;
  }
  if (keyCode == LEFT) {
    plotp(bgColor);
    px = px - 50;
    if (px < w ) px = w;
  }
}


class Color {
  final int red;
  final int green;
  final int blue;

  Color(int red, int green, int blue) {
    this.red = red;
    this.green = green;
    this.blue = blue;
  }
}
