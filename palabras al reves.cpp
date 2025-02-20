#include <iostream>
#include <string>
#include <algorithm>

int main() {
  std::string texto;

  std::cout << "ingrese la palabra que desee cambiar: ";
  std::getline(std::cin, texto);

  std::cout << "La palabra original es: " << texto << std::endl;

  std::reverse(texto.begin(), texto.end());

  std::cout << "La palabra invertida es: " << texto << std::endl;

  return 0;
}