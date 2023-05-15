#include <Python.h>
/**
 *  * print_python_list_info - Prints information about python objects
 * @p: PyObject pointer 
 *by Lorna
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, x;
	PyObject *item;

	size = PyList_Size(p);
	printf("[*] Size of Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (x = 0; x < size; x++)
	{
	item = PyList_GetItem(p, x);
	printf("Element %zd: %s\n", x, Py_TYPE(item)->tp_name);
	}
}
