#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "dicelib.hpp"

namespace py = pybind11;
using namespace dicelib;

PYBIND11_MODULE(dicelib, m)
{
    py::enum_<Result>(m, "Result")
        .value("DRAW", Result::DRAW)
        .value("P1_WINS", Result::P1_WINS)
        .value("P2_WINS", Result::P2_WINS)
        .export_values();

    m.def("roll", &roll, py::arg("n"));
    m.def("compare", &compare, py::arg("p1"), py::arg("p2"));
}