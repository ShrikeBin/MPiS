import numpy as np
import matplotlib.pyplot as plt
import time


n_values = np.arange(1000, 100001, 1000)
repetitions = 1

# Mersenne Twister
rng = np.random.default_rng()

def stat_gen(n, rng):
    
    urns = np.zeros(n, dtype=int)

    # Initialize statistics
    Bn, Un, Cn, Dn = 0, 0, 0, 0

    # First, we simulate the process of placing balls in urns
    first_collision_found = False
    all_urns_filled = False
    all_urns_double_filled = False
    throws = 0
    
    while not all_urns_double_filled:
        throws += 1
        urn = rng.integers(0, n)
        urns[urn] += 1

        # First collision (Bn)
        if urns[urn] == 2 and not first_collision_found:
            Bn = throws
            first_collision_found = True

        # All urns filled at least once (Cn)
        if np.all(urns >= 1) and not all_urns_filled:
            Cn = throws
            all_urns_filled = True

        # All urns filled at least twice (Dn)
        if np.all(urns >= 2):
            Dn = throws
            all_urns_double_filled = True

    # Number of empty urns after m throws (Un)
    Un = np.count_nonzero(urns == 0)

    return Bn, Un, Cn, Dn, Dn - Cn

start_time = time.time()

# Store results in an array for all statistics
results = {
    "Bn": np.zeros(len(n_values)),
    "Un": np.zeros(len(n_values)),
    "Cn": np.zeros(len(n_values)),
    "Dn": np.zeros(len(n_values)),
    "Dn_Cn_diff": np.zeros(len(n_values))
}

# Run simulations for each urn size
for i, n in enumerate(n_values):

    Bn_list = np.zeros(repetitions)
    Un_list = np.zeros(repetitions)
    Cn_list = np.zeros(repetitions)
    Dn_list = np.zeros(repetitions)
    Dn_Cn_diff_list = np.zeros(repetitions)

    for j in range(repetitions):
        Bn, Un, Cn, Dn, Dn_Cn_diff = stat_gen(n,rng)
        Bn_list[j] = Bn
        Un_list[j] = Un
        Cn_list[j] = Cn
        Dn_list[j] = Dn
        Dn_Cn_diff_list[j] = Dn_Cn_diff

    # Store mean of the statistics for this urn size
    results["Bn"][i] = np.mean(Bn_list)
    results["Un"][i] = np.mean(Un_list)
    results["Cn"][i] = np.mean(Cn_list)
    results["Dn"][i] = np.mean(Dn_list)
    results["Dn_Cn_diff"][i] = np.mean(Dn_Cn_diff_list)

# Plotting the results and saving each to a file

# 1. Plot Bn vs n (log-log plot)
plt.figure(figsize=(10, 6))
plt.loglog(n_values, results["Bn"], label="Bn (First Collision)", color='blue')
plt.xlabel("Number of urns (n)")
plt.ylabel("Throws until first collision (Bn)")
plt.title("First Collision (Bn) vs Number of urns")
plt.grid(True)
plt.legend()
plt.savefig("Bn_vs_n.png")  # Save the plot to a PNG file
plt.close()  # Close the plot to avoid displaying it

# 2. Plot Un vs n (log-log plot)
plt.figure(figsize=(10, 6))
plt.loglog(n_values, results["Un"], label="Un (Empty urns)", color='red')
plt.xlabel("Number of urns (n)")
plt.ylabel("Average number of empty urns (Un)")
plt.title("Empty Urns (Un) vs Number of urns")
plt.grid(True)
plt.legend()
plt.savefig("Un_vs_n.png")  # Save the plot to a PNG file
plt.close()

# 3. Plot Cn vs n (log-log plot)
plt.figure(figsize=(10, 6))
plt.loglog(n_values, results["Cn"], label="Cn (All urns filled once)", color='green')
plt.xlabel("Number of urns (n)")
plt.ylabel("Throws until all urns filled once (Cn)")
plt.title("All Urns Filled Once (Cn) vs Number of urns")
plt.grid(True)
plt.legend()
plt.savefig("Cn_vs_n.png")  # Save the plot to a PNG file
plt.close()

# 4. Plot Dn vs n (log-log plot)
plt.figure(figsize=(10, 6))
plt.loglog(n_values, results["Dn"], label="Dn (All urns filled twice)", color='purple')
plt.xlabel("Number of urns (n)")
plt.ylabel("Throws until all urns filled twice (Dn)")
plt.title("All Urns Filled Twice (Dn) vs Number of urns")
plt.grid(True)
plt.legend()
plt.savefig("Dn_vs_n.png")  # Save the plot to a PNG file
plt.close()

# 5. Plot Dn - Cn vs n (log-log plot)
plt.figure(figsize=(10, 6))
plt.loglog(n_values, results["Dn_Cn_diff"], label="Dn - Cn (Difference)", color='orange')
plt.xlabel("Number of urns (n)")
plt.ylabel("Difference (Dn - Cn)")
plt.title("Difference Between Dn and Cn vs Number of urns")
plt.grid(True)
plt.legend()
plt.savefig("Dn_Cn_diff_vs_n.png")  # Save the plot to a PNG file
plt.close()

end_time = time.time()
print(f"Execution Time: {end_time - start_time:.2f} seconds")
