#ifndef AXIS_HPP
#define AXIS_HPP

#include <vector>

template<typename T>
struct axis
{
    std::vector<T> x;
    std::vector<T> y;

    // conversion
    template<typename U>
    operator axis<U>()
    {
        return axis<U>
        {
            std::vector<U>(x.begin(), x.end()),
            std::vector<U>(y.begin(), y.end())
        };
    }
};

#endif 