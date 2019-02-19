#include "audio.h"
#include <Python.h>

static PyObject *audio_playNext(PyObject *self, PyObject *args)
{

}

static PyObject *audio_isReady(PyObject *self, PyObject *args)
{
    int is_ready;
    if (!PyArg_ParseTuple(args, ""))
        return NULL;
    is_ready = isReady();
    return Py_BuildValue("i", is_ready);
}




static PyObject *audio_setRootDir(PyObject *self, PyObject *args)
{
    char *dir_name;
    if (!PyArg_ParseTuple(args, "s", &dir_name))
        return NULL;
    setRootDir(dir_name);
    return Py_None;
}

static PyObject *audio_setAlphabetDir(PyObject *self, PyObject *args)
{
    char *dir_name;
    if (!PyArg_ParseTuple(args, "s", &dir_name))
        return NULL;
    setAlphabetDir(dir_name);
    return Py_None;
}

static PyObject *audio_setConfigDir(PyObject *self, PyObject *args)
{
    char *dir_name;
    if (!PyArg_ParseTuple(args, "s", &dir_name))
        return NULL;
    setConfigDir(dir_name);
    return Py_None;
}

static PyObject *audio_getCurLetterTimes(PyObject *self, PyObject *args)
{
    int size, n, ok;
    PyObject *o_list;
    const int *letter_times;
    if (!PyArg_ParseTuple(args, ""))
        return NULL;
    size = 0;
    ok = 0;
    n = 0;
    letter_times = getCurLetterTimes(&size);
    o_list = PyList_New(0);
    for (; n < size; ++n)
    {
        ok = PyList_Append(o_list, Py_BuildValue("i", *letter_times++));
    }
    return o_list;
}

static PyMethodDef audio_methods[] = {

    {"isReady", audio_isReady, METH_VARARGS, "Is ready for next sound"},
    {"setRootDir", audio_setRootDir, METH_VARARGS,
     "Set the root directory of audio command files ."},
    {"setAlphabetDir", audio_setAlphabetDir, METH_VARARGS,
     "Set the alphabet sound-file directory."},
    {"setConfigDir", audio_setConfigDir, METH_VARARGS,
     "Set the config sound-file directory."},

    {"getCurLetterTimes", audio_getCurLetterTimes, METH_VARARGS,

    {NULL, NULL, 0, NULL}};

PyMODINIT_FUNC initaudio(void)
{
    PyObject *m;

    m = Py_InitModule("audio", audio_methods);
    if (m == NULL)
        return;
}
