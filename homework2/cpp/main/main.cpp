#include <simulation.hpp>
#include <plot.hpp>

#include <string>

int main()
{
    std::string file_base = std::string(OUTPUT_DIRECTORY) + "Plot";

    full_simulation_results full_results = full_simulate(50);

    plot(full_results.B, full_results.avg_B, file_base + "B.png", "First collision");
    plot(full_results.U, full_results.avg_U, file_base + "U.png", "Empty bins after n balls");
    plot(full_results.C, full_results.avg_C, file_base + "C.png", "All bins have at least one ball");
    plot(full_results.D, full_results.avg_D, file_base + "D.png", "All bins have at least two balls");

    return 0;
}
