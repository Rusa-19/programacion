#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string elegirpalabrasecreta(const vector <string>& palabras){
    int indicealeatorio = rand () %
    palabras.size();
    return palabras[indicealeatorio]
}

int main() {
    const vector <string> palabras = {"perro","gato","loro","fresa","mora","piña","cambur","libro","lapiz","cuaderno","borrador"}
    
string palabrasecreta =
  elegirpalabrasecreta(palabras);
  int longitudpalabra =
  palabrasecreta.length();
    
string letrasadivinadas =
letrasadivinadas (longitudpalabra,"_");

int intentosrestantes = 6;
vector <char> letrasingresadas;

while (intentosrestantes > 0 && letrasadivinadas.find ("_") != string::npos) {
    cout << "palabra:" <<
letrasadivinadas << endl;
    cout << "intentos restantes:" <<
intentosrestantes << endl;
   cout << "letras ingresadas:" <<
for (char letra:
letrasingresadas) {
    cout <<letra<< "",
}
cout<<endl;
char letra;

}
