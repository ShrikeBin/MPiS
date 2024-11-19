#ifndef AXIS_HPP
#define AXIS_HPP

#include <vector>
#include <functional>

template<typename T>
struct axis
{
    std::vector<T> x;
    std::vector<T> y;

    // Conversion
    template<typename U>
    operator axis<U>()
    {
        return axis<U>
        {
            std::vector<U>(x.begin(), x.end()),
            std::vector<U>(y.begin(), y.end())
        };
    }

    void apply_to_x(const std::function<T(T)>& func)
    {
        for (auto& val : x)
        {
            val = func(val);
        }
    }

    void apply_to_y(const std::function<T(T)>& func)
    {
        for (auto& val : y)
        {
            val = func(val);
        }
    }
};

#endif
