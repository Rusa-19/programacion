#include <iostream>

using namespace std;

int main() {
    float num1, num2, num3, num4, num5;
    float promedio;

    cout << "Ingrese el primer número: ";
    cin >> num1;
    cout << "Ingrese el segundo número: ";
    cin >> num2;
    cout << "Ingrese el tercer número: ";
    cin >> num3;
    cout << "Ingrese el cuarto número: ";
    cin >> num4;
    cout << "Ingrese el quinto número: ";
    cin >> num5;

    promedio = (num1 + num2 + num3 + num4 + num5) / 5;

    cout << "El promedio de los cinco números es: " << promedio << endl;

    return 0;
}