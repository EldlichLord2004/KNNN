#include <iostream>
#include <windows.h>
#include <cstdlib>
#include <conio.h>
#include <stdlib.h>
#include <vector>
#include <string.h>
using namespace std;
struct Point {
  int x, y;
};

void gotoxy(int column, int line) {
  COORD coord;
  coord.X = column;
  coord.Y = line;
  SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}

class Snake {
private:
  vector<Point> A;
  int DoDai;
  enum snakesDirection { STOP = 0, LEFT, RIGHT, UP, DOWN };
  bool isGameOver;


public:
  Snake() {
    DoDai = 1;
    Point p;
    for (int i = 0;i < DoDai;i++)
    {
      p.x = 1;
      p.y = 1;
      A.push_back(p);
    }
  }

  Point getHead() {
    return A[DoDai - 1];
  }

  void draw() {
    for (int i = 0; i < DoDai; i++) {
      gotoxy(A[i].x, A[i].y);
      cout << "X";
    }
  }

  void move(int huong) {
    for (int i = 1; i < DoDai; i++)
      A[i - 1] = A[i];
    if (huong == 0) A[DoDai - 1].x++; //d
    if (huong == 1) A[DoDai - 1].y++; //s
    if (huong == 2) A[DoDai - 1].x--; //a
    if (huong == 3) A[DoDai - 1].y--; //w

  }

  void growup() {
    DoDai++;
    A.insert(A.begin(), A[DoDai - 2]);

  }

};

class food {
private:
  struct Point A;

public:
  food() {
    A.x = rand() % 30+1;
    A.y = rand() % 30+1;
  }
  void draw() {
    gotoxy(A.x, A.y);
    cout << "O";
  }


  void newfood()
  {
    A.x = rand() % 30+1;
    A.y = rand() % 30+1;
  }

  Point getPoint() {
    return A;
  }
};

class Board {
private:
  int width, height;
public:
  int row = 0, col = 0;
  string str;
  Board() {
    width = 40;
    height = 40;
  }

  void draw() {
  string str;
    for (int i = 0; i < width; i++) {
      for (int j = 0; j < height; j++) {
        if (i == 0 or i == width - 1 or j == 0 or j == height - 1) {
          str.append("# ");
        }

        else str.append("  ");
      }
      str.append("\n");
    }
    cout << str;
}

  pair<int, int> get_size() {
    return make_pair(width, height);
  }

};

class game{
  private:
    int score=0;
    Snake r;
    food f;
    string str;
    Board bf;
  public:
    bool check(){
      if (r.getHead().x == 0 or r.getHead().x == 2*bf.get_size().first-1 or r.getHead().y == 0 or r.getHead().y == bf.get_size().second-1) {
        return false;
      }
      return true;
    }

    void input_name(){
      cout << "Enter your name: ";
      cin >> str;
    }

    void show_score()
  {
    gotoxy(2*bf.get_size().first+1,0);
    cout << "Score: " << score << endl;
  }


    void play() {
      bf.draw();
      f.draw(); // Hiển thị thức ăn (O)
      r.draw();
      show_score();
      int huong = 0;
      char t = 'd', prev = 'd';
      while (1) {
        if (kbhit()) {
          prev = t;
          t = getch();
          if (t == 'a' and prev != 'd') huong = 2;
          if (t == 'w' and prev != 's') huong = 3;
          if (t == 'd' and prev != 'a') huong = 0;
          if (t == 's' and prev != 'w') huong = 1;
        }
        system("cls");
        r.move(huong);
        if (r.getHead().x == f.getPoint().x and r.getHead().y == f.getPoint().y) {
          // system("cls");
          score++;
          f.newfood();
          r.growup();
        }
        if (check() == false) {
          system("cls");
          cout << "Game Over\n";
          break;
        }
        bf.draw();
        r.draw();
        f.draw();
        show_score();
        Sleep(100);
      }
  }
};



int main() {
  game play;
  system("cls");
  play.play();
  play.show_score();
  system("pause");
  return 0;
}
