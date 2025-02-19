#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdlib> 

using namespace std;

string elegirPalabraSecreta(const vector<string>& palabras) {
   
    srand(time(0)); 
    int indiceAleatorio = rand() % palabras.size();
    return palabras[indiceAleatorio];
}

int main() {
    const vector<string> palabras = {"perro", "gato", "casa", "arbol", "libro", "computadora", "telefono", "escuela"};

    string palabraSecreta = elegirPalabraSecreta(palabras);
    int longitudPalabra = palabraSecreta.length();

    string letrasAdivinadas(longitudPalabra, '_');

    int intentosRestantes = 6;
    vector<char> letrasIngresadas;

    cout << "¡Bienvenido al juego del ahorcado!" << endl;

    while (intentosRestantes > 0 && letrasAdivinadas.find('_') != string::npos) {
        cout << "\nPalabra: " << letrasAdivinadas << endl;
        cout << "Intentos restantes: " << intentosRestantes << endl;
        cout << "Letras ingresadas: ";
        for (char letra : letrasIngresadas) {
            cout << letra << " ";
        }
        cout << endl;

        char letra;
        cout << "Ingresa una letra: ";
        cin >> letra;

        letra = tolower(letra);

        if (find(letrasIngresadas.begin(), letrasIngresadas.end(), letra) != letrasIngresadas.end()) {
            cout << "Ya ingresaste esa letra. Intenta con otra." << endl;
            continue; 
        }

        letrasIngresadas.push_back(letra);

        bool letraEncontrada = false;
        for (int i = 0; i < longitudPalabra; ++i) {
            if (palabraSecreta[i] == letra) {
                letrasAdivinadas[i] = letra;
                letraEncontrada = true;
            }
        }

        if (!letraEncontrada) {
            intentosRestantes--;
            cout << "Letra incorrecta." << endl;
        }
    }

    if (letrasAdivinadas.find('_') == string::npos) {
        cout << "\n¡Ganaste! Adivinaste la palabra: " << palabraSecreta << endl;
    } else {
        cout << "\n¡Perdiste! La palabra era: " << palabraSecreta << endl;
    }

    return 0;
}
