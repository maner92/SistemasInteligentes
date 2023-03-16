#include <iostream>

using namespace std;

struct mochila
{
    string name;
    float value;
    float weight;
    float index;
};

int main()
{
    int n, i, j, max;
    float max_m, vmax = 0, wfin = 0;

    cout << "<---- PROBLEMA DE LA MOCHILA ----> \n";
    // Se pide el peso maximo a cargar en la mochila
    cout << "\n /// Ingresa la cantidad maxima que soporta la mochila/// \n";
    cout << "Cantidad maxima a soportar: ";
    cin >> max_m;

    // Aqui se pide la cantidad de objetos para meter en la mochila
    cout << "\n Ingresa el numero de elementos: ";
    cin >> n;
    mochila element[n], aux;

    // Se pide el ingresar los elements de la mochila
    cout
        << "\n /// Objetos para llenar la mochila /// \n";

    for (i = 0; i < n; i++)
    {
        cout << "\n ---- Objeto " << i + 1 << "---- \n";
        cout << "Ingresa el nombre:";
        cin >> element[i].name;
        cout << "Ingresa valor: ";
        cin >> element[i].value;
        cout << "Ingrese el peso: ";
        cin >> element[i].weight;
        element[i].index = element[i].value / element[i].weight;
    }

    // Se ordenan los elementos de mayor a menor
    for (i = 0; i < n; i++)
    {
        max = i;
        for (j = i + 1; j < n; j++)
        {
            if (element[j].index > element[i].index)
            {
                max = j;
            }
        }
        aux = element[i];
        element[i] = element[max];
        element[max] = aux;
    }

    // Objetos ya ordenados
    cout << "\n /// Objetos ya ordenados de mayor a menor ///  \n";
    for (i = 0; i < n; i++)
    {
        cout << i + 1 << " : ";
        cout << element[i].name << " ,";
        cout << element[i].index << " , ";
        cout << element[i].value << " , ";
        cout << element[i].weight << endl;
    }

    cout << endl;

    // Se busca la mejor solucion para ingresar a la mochila

    cout << "/// Mejor solucion para llevar en la mochila /// \n";
    i = 0;

    while (max_m > 0)
    {
        if (max_m > element[i].weight)
        {
            cout << element[i].name << " entra en la mochila \n";
            max_m = max_m - element[i].weight;
            vmax = vmax + element[i].value;
            wfin = wfin + element[i].weight;
        }
        else
        {
            cout << "\n Ya no hay espacio en la mochila \n";
            max_m = 0;
        }
        i++;
    }
    cout << "\n El valor maximo que llevamos en la mochila es " << vmax << endl;
    cout << "\n El peso maximo que llevamos en la mochila es " << wfin << endl;
}
