#include <python.h>

/**
 *print_python_list_info - prints information about a python list
 *@p: A PyObject list
 *
 */
void print_python_list_info(PyObject *p)
{
	long int list_size = Pylist_Size(p);
	int index;
	PyListObject *list = (PyListObject *p;

	printf("[*] Size of the Python List = %li\n", list_size);
	printf("[*] Allocated = %li\n", list->allocated);

	for (index = 0; index < list_size; index++)
		printf("Element %i: %s\n", index, Py_TYPE(list->ob_item[index])->tp_name);
}
