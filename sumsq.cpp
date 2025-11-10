#include <boost/python.hpp>

int sumsq(int n)
{
    int total = 0;
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            total += i * i + j * j;
        }
    }
    return total;
}

BOOST_PYTHON_MODULE(sumsq)
{
    using namespace boost::python;
    def("sumsq", &sumsq);
}