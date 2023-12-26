#include <stdio.h>
#include<conio.h>
#include<windows.h>
#define C3  130
#define Db3 138
#define D3  146
#define Eb3 155
#define E3  164
#define F3  174
#define Gb3 185
#define G3  196
#define Ab3 207
#define A3  220
#define Bb3 233
#define B3  246

#define C4  261
#define Db4 277
#define D4  293
#define Eb4 311
#define E4  329
#define F4  349
#define Gb4 369
#define G4  392
#define Ab4 415
#define A4  440
#define Bb4 466
#define B4  493

#define C5  523
#define Db5 544
#define D5  587
#define Eb5 622
#define E5  659
#define F5  698
#define Gb5 739
#define G5  783
#define Ab5 830
#define A5  880
#define Bb5 932
#define B5  987

#define C6  1046
#define Db6 1108
#define D6  1174
#define Eb6 1244
#define E6  1318
#define F6  1396
#define Gb6 1479
#define G6  1567
#define Ab6 1661
#define A6  1760
#define Bb6 1864
#define B6  1975

#define C7  2093
#define Db7 2217
#define D7  2349
#define Eb7 2489
#define E7  2637
#define F7  2794
#define Gb7 2960
#define G7  3136
#define Ab7 3322
#define A7  3520
#define Bb7 3729
#define B7  3951

#define full 600
#define half full / 2

void Harry_porter();
void SA_RI_GA_MA__();
void pink_panther();
void Doremon();
void jingle();
int main(){

    printf("WELCOME...!!!!!!!!!");

    puts("\nChoose a melody: \n(1) Doremon\n(2) SA RI GA MA ...\n(3) Harry porter\n(4) Pink panther\n(5) Jingle bells"); 

    int n;
    scanf("%d",&n);

switch(n){
    case 1 : Doremon();
             break;
    case 2 : SA_RI_GA_MA__();
             break;
    case 3 : Harry_porter();
             break;
    case 4 : pink_panther();
             break;
    case 5 : jingle();
             break;
    default : printf("not a valid song");
}
    return 0;
}
void Harry_porter(){
    Beep(B5,half);
    Beep(E6,half);
    Sleep(half);
    Beep(G6,half);
    Beep(Gb6,half);
    Beep(E6,half);
    Sleep(half);
    Beep(B6,half);
    Beep(A6,half);
    Beep(Gb6,half);
    Beep(E6,half);
    Beep(G6,half);
    Beep(Gb6,half);
    Beep(Eb6,half);
    Beep(F6,half);
    Beep(B5,full);
    Beep(B5,half);
    Beep(E6,half);
    Beep(G6,half);
    Beep(Gb6,half);
    Beep(E6,half);
    Beep(B6,half);
    Beep(D7,half);
    Beep(Db7,half);
    Beep(C7,half);
    Beep(Ab6,half);
    Beep(C7,half);
    Beep(B6,half);
    Beep(Bb6,half);
    Beep(Bb5,half);
    Beep(G6,half);
    Beep(E6,half);
    Beep(G6,half);
    Beep(B6,half);
    Beep(G6,half);
    Beep(B6,half);
    Beep(G6,half);
    Beep(C7,half);
    Beep(B6,half);
    Beep(Bb6,half);
    Beep(Gb6,half);
    Beep(G6,half);
    Beep(B6,half);
    Beep(Bb6,half);
    Beep(Bb5,half);
    Beep(B5,half);
    Beep(B6,half);
    Beep(G6,half);
    Beep(B6,half);
    Beep(G6,half);
    Beep(B6,half);
    Beep(G6,half);
    Beep(D7,half);
    Beep(Db7,half);
    Beep(C7,half);
    Beep(Ab6,half);
    Beep(C7,half);
    Beep(B6,half);
    Beep(Bb6,half);
    Beep(Bb5,half);
    Beep(G6,half);
    Beep(E6,half);
}
void pink_panther(){
    Beep(Db4,half);
    Beep(D4,half);
    Beep(Eb4,half);
    Beep(E4,full);
    Beep(Db4,half);
    Beep(D4,half);
    Beep(Eb4,half);  
    Beep(E4,full);
    Beep(Db4,half);
    Beep(D4,half);
    Beep(Eb4,half);
    Beep(E4,full);
    Beep(Gb4,half);
    Beep(G4,half);
    Beep(Eb4,half);
    Beep(E4,half);
    Beep(Gb4,half);
    Beep(G4,half);
    Beep(C5,half);
    Beep(B4,half);
    Beep(E4,half);
    Beep(G4,half);
    Beep(B4,half);
    Beep(Bb4,full);
    Beep(A4,half);
    Beep(G4,half);
    Beep(E4,half);
    Beep(D4,half);
    Beep(E4,full);
    Beep(Eb4,half);
    Beep(E4,full);
    Beep(Gb4,half);
    Beep(G4,full);
}
void jingle(){
Beep(E5, half);
	Beep(E5, half);
	Beep(E5, half);
 
	Sleep(half);
 
	Beep(E5, half);
	Beep(E5, half);
	Beep(E5, half);
 
	Sleep(half);
 
	Beep(E5, half);
	Beep(G5, half);
	Beep(C5, half);
	Beep(D5, half);
	Beep(E5, half);
 
	Beep(C4, half);
	Beep(D4, half);
	Beep(E4, half);
 
	Beep(F5, half);
	Beep(F5, half);
	Beep(F5, half);
 
	Sleep(half);
 
	Beep(F5, half);
	Beep(E5, half);
	Beep(E5, half);
 
	Sleep(half);
 
	Beep(E5, half);
	Beep(D5, half);
	Beep(D5, half);
	Beep(E5, half);
	Beep(D5, half);
 
	Sleep(half);
 
	Beep(G5, half);
 
	Sleep(half);
 
	Beep(E5, half);
	Beep(E5, half);
	Beep(E5, half);
 
	Sleep(half);
 
	Beep(E5, half);
	Beep(E5, half);
	Beep(E5, half);
 
	Sleep(half);
    Beep(E5, half);
	Beep(G5, half);
	Beep(C5, half);
	Beep(D5, half);
	Beep(E5, half);
 
	Beep(C4, half);
	Beep(D4, half);
	Beep(E4, half);
 
	Beep(F5, half);
	Beep(F5, half);
	Beep(F5, half);
 
	Sleep(half);
 
	Beep(F5, half);
	Beep(E5, half);
	Beep(E5, half);
 
	Sleep(half);
 
	Beep(G5, half);
	Beep(G5, half);
	Beep(F5, half);
	Beep(D5, half);
	Beep(C5, full);
 
	Sleep(full);
    
}
 
void Doremon(){
	Beep(220,300);

  Beep(294,300);

  Beep(294,300);

  Beep(370,300);

  Beep(494,300);

  Beep(370,300);

  Beep(440,800);

  

  Beep(440,300);

  Beep(494,300);

  Beep(440,300);

  Beep(370,300);

  Beep(392,300);

  Beep(370,300);

  Beep(330,800);

  

  Beep(247,300);

  Beep(330,300);

  Beep(330,300);

  Beep(370,300);

  Beep(555,300);

  Beep(555,300);

  Beep(494,300);

  Beep(440,300);

  Beep(392,800);

  Beep(392,300);

  Beep(370,300);

  Beep(247,800);

  Beep(278,300);

  Beep(294,300);

  Beep(330,2600);

  

  Beep(220,300);

  Beep(294,300);

  Beep(294,300);

  Beep(370,300);

  Beep(494,300);

  Beep(370,300);

  Beep(440,800);

  

  Beep(440,300);

  Beep(494,300);

  Beep(440,300);

  Beep(370,300);

  Beep(392,300);

  Beep(370,300);

  Beep(330,800);

  

  Beep(247,300);

  Beep(330,300);

  Beep(330,300);

  Beep(370,300);

  Beep(555,300);

  Beep(555,300);

  Beep(494,300);

  Beep(440,300);

  Beep(392,800);

  Beep(392,300);

  Beep(370,300);

  Beep(278,600);

  Beep(330,600);

  Beep(294,2600);

  

  Beep(494,300);

  Beep(494,300);

  Beep(494,300);

  Beep(440,300);

  Beep(392,200);

  Beep(440,200);

  Beep(494,200);

  Beep(440,800);

  Beep(330,300);

  Beep(370,300);

  Beep(416,300);

  Beep(330,300);

  Beep(440,900);
  

  Beep(494,800);

  Beep(440,800);

  Beep(392,900);

  

  Beep(555,300);

  Beep(555,300);

  Beep(555,300);

  Beep(494,300);

  Beep(440,300);

  Beep(494,300);

  Beep(440,300);

  Beep(392,900);

  

  Beep(440,300);

  Beep(494,300);

  Beep(370,900);

  Beep(330,300);

  Beep(294,900);

  

  Beep(494,800);

  Beep(440,800);

  Beep(392,900);

  

  Beep(555,300);

  Beep(555,300);

  Beep(555,300);

  Beep(494,300);

  Beep(440,300);

  Beep(494,300);

  Beep(440,300);

  Beep(392,900);

  

  Beep(440,300);

  Beep(494,300);

  Beep(370,900);

  Beep(330,300);

  Beep(294,1000);




}
void krishna(){
    
    Beep(A5,half);
    Beep(A5,half);
    Beep(D6,half);
    Beep(D6,half);

        Sleep(200);

    Beep(D6,half);

    Sleep(200);

    Beep(C6,half);
    Beep(B5,half);
    
    Sleep(200);

    Beep(A5,half);
    Beep(C6,half);
    Beep(B5,half);

    Sleep(100);

    Beep(A5,half);
    Sleep(200);
    Beep(G5,half);
    Beep(A5,half);
    Beep(A5,half);
  /*  Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
    Beep(,half);
*/

}
void SA_RI_GA_MA__(){
  Beep(Db5,half);
  Sleep(200);
  Beep(Eb5,half);
  Sleep(200);
  Beep(F5,half);
  Sleep(200);
  Beep(Gb5,half);
  Sleep(200);
  Beep(Ab5,half);
  Sleep(200);
  Beep(Bb5,half);
  Sleep(200);
  Beep(C6,half);
  Sleep(200);
  Beep(Db6,half);
  Sleep(200);
  Beep(Db6,half);
  Sleep(200);
  Beep(C6,half);
  Sleep(200);
  Beep(Bb5,half);
  Sleep(200);
  Beep(Ab5,half);
  Sleep(200);
  Beep(Gb5,half);
  Sleep(200);
  Beep(F5,half);
  Sleep(200);
  Beep(Eb5,half);
  Sleep(200);
  Beep(Db5,half);
  Sleep(200);
  

}
