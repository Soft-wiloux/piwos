#include <iostream>
#include <Windows.h>
#include <python.h>
 
int main()
{
//Inicilizamos inteprete
Py_Initialize();
 
//Prueba de compilaciom
PyRun_SimpleString("print('Ya estas usando Python :D')");
 
//Terminamos inteprete
Py_Finalize();
 
system("Pause");
return 0;
}