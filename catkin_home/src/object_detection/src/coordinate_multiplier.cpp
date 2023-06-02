#include <iostream>

extern "C" {
    /**
     * Multiplica las coordenadas cx y cy por 100.
     *
     * @param[in,out] cx Coordenada x a multiplicar por 100.
     * @param[in,out] cy Coordenada y a multiplicar por 100.
     *
     */
    void multiply_coordinates(int& cx, int& cy) {
        cx *= 100;
        cy *= 100;
    }
}
