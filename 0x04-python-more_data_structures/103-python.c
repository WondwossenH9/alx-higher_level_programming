#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
/**
 * print_python_bytes - prints python bytes
 * @p: pointer to python object
 * Return: nothing
 */

void print_python_bytes(PyObject *p)
{
	long int size;
	int i;
	char *test_str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &test_str, &size);

	printf("  size: %li\n", size);
	printf("  test string: %s\n", test_str);
	if (size < 10)
		printf("  first %li bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	for (i = 0; i <= size && i < 10; i++)
		printf(" %02hhx", test_str[i]);
	printf("\n");
}

/**
 * print_python_list - prints python list
 * @p: pointer to python object
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	long int size = PyList_Size(p);
	int j;
	PyListObject *list = (PyListObject *)p;
	const char *type;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", list->allocated);
	for (j = 0; j < size; j++)
	{
		type = (list->ob_item[j])->ob_type->tp_name;
		printf("Element %i: %s\n", j, type);
		if (!strcmp(type, "bytes"))
			print_python_bytes(list->ob_item[j]);
	}
}
