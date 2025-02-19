#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
    int cantidad, rango_min, rango_max;

    cout << "Ingrese la cantidad de números aleatorios a generar: ";
    cin >> cantidad;

    cout << "Ingrese el rango mínimo: ";
    cin >> rango_min;
    cout << "Ingrese el rango máximo: ";
    cin >> rango_max;

    srand(time(0));

    cout << "Números aleatorios generados:" << endl;
    for (int i = 0; i < cantidad; i++) {
        int numero_aleatorio = rand() % (rango_max - rango_min + 1) + rango_min;
        cout << numero_aleatorio << " ";
    }
    cout << endl;

    return 0;
}