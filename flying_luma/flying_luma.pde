import processing.pdf.*;

PFont font1; PFont font2; PFont bold;
PImage bg; PImage bgR; PImage luma; PImage luma2; PImage meteor; PImage openingBg; PImage costume; 
int x; int cVy; int cx; int cy; int y; 
PImage pokeball; int px; int py;
PImage weapon; int wx; int wy; 
int numMeteor = 7;
int gameState;
int []mx = new int[numMeteor]; int []my = new int[numMeteor];
int count; int score; int highScore;
int weaponCount; int pokeballCount;
boolean isFiring; boolean poke;


void setup(){
  isFiring = true;
  poke = false;
  gameState = -1;
  font2 = createFont("OCR A EXTENDED", 18);
  font1 = createFont("Courier New", 38);
  bold = createFont("OCR A EXTENDED", 25);

  size(600,600);
  bg = loadImage("./img/bg2.png");
  bgR = loadImage("./img/bgR2.png");
  luma = loadImage("./img/luma.png");
  luma2 = loadImage("./img/luma2.png");
  meteor = loadImage("./img/meteor.png");
  pokeball = loadImage("./img/pokeball.png");
  weapon = loadImage("./img/weapon.png");
  openingBg = loadImage("./img/bg2.png");
  costume = luma;
  
  cVy = 2;
  cx = 50;
  cy = 100;
  
  wx = width + 10000;
  px = width + 200;
  py = (int)random(200,600);
  for(int i = 0; i < numMeteor; i++){
    mx[i] = width + (int)random(50,200) + 200*i;
    my[i] = height/2 + (int)random(-200,200);
  }
  
}

void draw(){
  count++;
  move();
  if(score > highScore){
    highScore = score;
  }
  
  if (gameState==0){
  image(bg, x, 0);
  image(bgR, x + bg.width-6,0);
  image(bg, x + 2 * bg.width-12,0);
  
  if(x < -(2*bg.width+12)){
    x = 0;
  }
  
 //Meteor
  for(int i=0; i < numMeteor; i++){
    mx[i] -= 2;
    if(mx[i] < -10){
      score++;
      mx[i] = width + (int)random(50,200);
      my[i] = height/2 + (int)random(-200,200);
    }
    if(abs((int)((wx+10) - (mx[i]+5))) < 10 && abs((int)((wy+10) - (my[i]+32))) < 56){
      mx[i] += 2000;
      wx = width + 20000;
      score++;
    }
    if(abs((int)((cx+35) - (mx[i]+7))) < 22 && abs((int)((cy+34) - (my[i]+41))) < 74){
      gameState = 1;
    }
    image(meteor, mx[i], my[i]);
    
//Pokeball
    if(score > 10){
      px -= 3;
    }
    if(px < -100){
      px = width + 2000;
      py = (int)random(200,600);
    }
    
    if(abs((int)((cx+35) - (px+75))) < 80 && abs((int)((cy+34) - (py+52))) < 86){
      gameState = 1;
    }
    image(pokeball, px, py);
  }
        
//Luma(Star)
  image(luma,cx,cy);
  cy = cy + cVy;
  if(count%2 == 0){
    cVy++;
  }
  x--;
  checkStar();
  
//Weapon(Shuriken)
  image(weapon, wx, wy);
  wx += 10;
  if(abs((int)((wx+10)-(px+75))) < 80 && abs((int)((wy+10) - (py+52))) < 86){
    px +=2000;
    wx = 20000;
    if(pokeballCount == 0){
      poke = true;
    }
    if(pokeballCount > 0){
      poke = false;
    }
    pokeballCount++;   
  }
  
    if(wx > width + 20){
      wx = 20000;
    }
}

//When player dies
if (gameState == 1){
  //button
  textSize(34);
  text("You Died...", 200, 230);
  fill(245); //text color
  rect(190,235,240,45,10); // button background
  fill(0);

//Restart Game
  if(mouseX > 190 && mouseY > 235 && mouseX < 430 && mouseY < 280){
    if(mousePressed){
      cy = 100;
      cVy = 2;
      cx = 50;
      score = 0;
      wx = width + 10000;
      px = width + 200;
      py = (int)random(200,600);
      for(int i=0; i < numMeteor; i++){
        mx[i] = width + (int)random(50, 200) + 200*i;
        my[i] = height/2 + (int)random(-200,200);
      }
      gameState = 0;
    }
    
//Hovering over button
    else{
      fill(173, 191, 255);
      rect(190,235, 240, 45, 10);
      fill(0);
      text("Play Again?", 200,270); //button text
     }
   }
    else{
      text("Click Me...", 200,270);  //button text
    } 
  }
  
  //Text on the Screen (Score/Warnings)
  fill(0);
  textSize(15);
  text("Score: " + score, width - 130,30);
  text("High Score: " + highScore, width - 130, 50);
  if(score > 8 && score <12){
    fill(255,0,0);
    textSize(20);
    text("Warning: Zooming Pokeballs!",30,110);
    fill(0);
    textSize(20);
  }
  if(weaponCount < 1 && score > 0){
    if(score < 5){
      text("Don't forget that Luma can throw Shurikens...", 20,30);
    }
    else{
      text("Press the Down Arrow to Throw....", 20,30);
    }
  }
  if(!isFiring && weaponCount > 0 && score > 3){
    text("Good Job! You learned how to throw :)", 20,30);
    if(weaponCount > 3){
      text("hmm...will there be more obstacles...?", 20,60);
    }
  }
  
  if(poke){
    text("huh...shurikens can destroy pokeballs too...", 20,60);
  }
  //Opening Background
  if(gameState == -1){
    image(openingBg,0,0);
    fill(0,0,0,151);
    textSize(24);
    textFont(font1);
    text("Click anywhere to play!",45,150);
    if(mousePressed && mouseX > 0){
      gameState = 0;
    }
    
    textFont(font2);
    text("Move: Left/Right Arrow",170,270);
    text("Throw Weapon: Down Arrow",170,295);
    text("Fly: click Mouse",170,320);
    fill(0,0,0,255);
    textFont(bold);
    text("Luma Controls",200,240);
    noFill();
    rect(160,250,280,80,5);
  }
}

//Moving Left/Right
void move(){
 if(keyPressed){
   if(cx>0 && keyCode == LEFT){
     cx -= 2;
   }
   else if(cx < width/2 && keyCode == RIGHT){
     cx += 2;
   }
 }
}

//Throwing Shurikens button
void keyReleased(){
  if(keyCode == DOWN){
  lumaThrow();
  }
}

//Costumes...
void mousePressed(){
  cVy = -10;
  costume = luma2;
}

void mouseReleased(){
  costume = luma;
}
//...Costumes


//Throwing Shurikens Code
void lumaThrow(){
  wx = cx + 20;
  wy = cy + 45;
  weaponCount++;

  if(weaponCount > 4){
    isFiring = true;
  }
  else{
    isFiring = false;
  }
}

//Checks if character hits the walls/edges = death
void checkStar(){
  if(cy > height || cy < -80){
    gameState = 1;
  }
}


    
