#include <iostream>

using namespace std;

int main() {
  srand(time(0)); 

  cout << "¡Bienvenido a la aventura en el bosque!" << endl;

  cout << "Te encuentras en un claro y debes elegir un camino:" << endl;
  cout << "1. El sendero de la izquierda" << endl;
  cout << "2. El sendero de la derecha" << endl;
  cout << "3. El camino recto" << endl;

  int opcion1;
  cin >> opcion1;

  switch (opcion1) {
    case 1:
      cout << "¡Oh no! Has caído en un agujero y la aventura termina aquí." << endl;
      return 0; 
    case 2:
      cout << "¡Has encontrado un puente colgante!" << endl;
      break; 
    case 3:
      cout << "El camino es largo y aburrido. ¡Mejor suerte la próxima vez!" << endl;
      return 0; 
    default:
      cout << "¡Opción inválida! Elige un camino válido." << endl;
      return 0; 
  }

  cout << "El puente cruje, ¿qué haces?" << endl;
  cout << "1. Cruzar corriendo" << endl;
  cout << "2. Cruzar con cuidado" << endl;
  cout << "3. Regresar" << endl;

  int opcion2;
  cin >> opcion2;

  switch (opcion2) {
    case 1:
      cout << "¡El puente se rompe! Caes al vacío y la aventura termina aquí." << endl;
      return 0;
    case 2:
      cout << "¡Logras cruzar el puente! Llegas a una bifurcación." << endl;
      break;
    case 3:
      cout << "¡Cobarde! Regresas al claro inicial." << endl;
      return 0;
    default:
      cout << "¡Opción inválida! Elige una acción válida." << endl;
      return 0;
  }

  cout << "En la bifurcación, ¿qué camino tomas?" << endl;
  cout << "1. El camino de la montaña" << endl;
  cout << "2. El camino del río" << endl;
  cout << "3. El camino del bosque oscuro" << endl;

  int opcion3;
  cin >> opcion3;

  switch (opcion3) {
    case 1:
      cout << "¡Escalas la montaña y encuentras un tesoro! ¡Has ganado!" << endl;
      break;
    case 2:
      cout << "¡Te encuentras con un oso y sales corriendo! La aventura termina aquí." << endl;
      return 0;
    case 3:
      cout << "¡Te pierdes en el bosque oscuro y nunca encuentras la salida! Fin del juego." << endl;
      return 0;
    default:
      cout << "¡Opción inválida! Elige un camino válido." << endl;
      return 0;
      }
      return 0;
}