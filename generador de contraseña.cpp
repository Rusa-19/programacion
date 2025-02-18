#include <iostream>
#include <random>
#include <string>

std::string generarContraseña(int longitud) {
    const std::string caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-`~[]\{}|;':\",./<>?";
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> distrib(0, caracteres.size() - 1);
    std::string contraseña = "";
    for (int i = 0; i < longitud; ++i) {
        contraseña += caracteres[distrib(gen)];
    }
    return contraseña;
}

int main() {
    int longitud;
    std::cout << "Ingrese la longitud de la contraseña: ";
    std::cin>> longitud;
    std::string contraseña = generarContraseña(longitud);
    std::cout << "Contraseña generada: " << contraseña << std::endl;
    return 0;
}