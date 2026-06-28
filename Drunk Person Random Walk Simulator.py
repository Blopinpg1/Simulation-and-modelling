import random
import matplotlib.pyplot as plt
import math

# simulation function
def drunk_walk(n):
    x, y = 0, 0
    xs, ys = [0], [0]
    counts = {'L': 0, 'R': 0, 'F': 0}

    for step in range(n):
        r = random.random()          # generate uniform random number

        if r < 0.30:                 # inversion method (cumulative probability)
            x -= 1  
            counts['L'] += 1
        elif r < 0.50:               # 0.30 + 0.20
            x += 1
            counts['R'] += 1
        else:                        # 0.50 + 0.50
            y += 1
            counts['F'] += 1

        xs.append(x)
        ys.append(y)

    return xs, ys, counts

#  Run for n = 10, 100, 1000
for n in [10, 100, 1000]:
    xs, ys, counts = drunk_walk(n)
    final_x, final_y = xs[-1], ys[-1]
    distance = math.sqrt(final_x**2 + final_y**2)

    print(f"\n{'='*40}")
    print(f"  n = {n} steps")
    print(f"  Final position : ({final_x}, {final_y})")
    print(f"  Net distance   : {distance:.4f}")
    print(f"  Left  : {counts['L']} ({counts['L']/n*100:.1f}%) — expected 30%")
    print(f"  Right : {counts['R']} ({counts['R']/n*100:.1f}%) — expected 20%")
    print(f"  Fwd   : {counts['F']} ({counts['F']/n*100:.1f}%) — expected 50%")

#  Plot all three
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
for ax, n in zip(axes, [10, 100, 1000]):
    xs, ys, _ = drunk_walk(n)
    ax.plot(xs, ys, linewidth=0.8, alpha=0.7)
    ax.plot(xs[0], ys[0], 'go', markersize=8, label='Start')   # green = start
    ax.plot(xs[-1], ys[-1], 'ro', markersize=8, label='End')   # red = end
    ax.set_title(f'n = {n} steps')
    ax.set_xlabel('X (Left / Right)')
    ax.set_ylabel('Y (Forward)')
    ax.legend()
    ax.grid(True, alpha=0.3)

plt.suptitle('Drunk Person Random Walk Simulation', fontsize=14)
plt.tight_layout()
plt.savefig('drunk_walk.png', dpi=150)
plt.show()