#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
  srand(time(0)); 
  
  int numeroAleatorio = rand() % 100 + 1; 

  int numeroUsuario;
  int intentos = 0;

  cout << "¡Adivina el número secreto entre 1 y 100!" << endl;

  do {
      
    cout << "Ingresa tu número: ";
    cin >> numeroUsuario;
    intentos++;

    if (numeroUsuario < numeroAleatorio) {
      cout << "¡Demasiado bajo! prueba de nuevo." << endl;
    } 
    else if (numeroUsuario > numeroAleatorio) {
      cout << "¡Demasiado alto! prueba otra vez." << endl;
    }
    else {
      cout << "¡Felicidades! ¡Adivinaste el número en " << intentos << " intentos!" << endl;
    }
  } while (numeroUsuario != numeroAleatorio);

  return 0;
}