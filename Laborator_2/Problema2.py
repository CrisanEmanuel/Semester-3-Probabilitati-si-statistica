# from matplotlib import pyplot as plt
# from random import random
# from math import dist
#
#
# def problema2():
#     print("a)")
#     # Valorile N
#     N_values = [500, 1000, 2000]
#
#     # Define latura pătratului
#     side_length = 1.0
#
#     # Initialize the counts for each condition
#     count_inside_circle = [0, 0, 0]
#     count_inside_center = [0, 0, 0]
#     count_triangles = [0, 0, 0]
#
#     # Loop through each N value
#     for N in N_values:
#         # Generate random points within the square
#         points = [(random(), random()) for _ in range(N)]
#
#         # Calculate distances from the center and corners
#         center = (0.5, 0.5)
#         distances_to_center = [dist(center, point) for point in points]
#         distances_to_corners = [min(point[0], 1 - point[0], point[1], 1 - point[1]) for point in points]
#
#         # Condition i: Points inside the circle tangent to the sides of the square
#         count_inside_circle[N_values.index(N)] = sum(1 for distance in distances_to_center if distance < 0.5)
#
#         # Condition ii: Points closer to the center than to the corners
#         count_inside_center[N_values.index(N)] = sum(
#             1 for i in range(N) if distances_to_center[i] < distances_to_corners[i])
#
#         # Condition iii: Points forming two acute and two obtuse triangles
#         # For this condition, we will use a geometrical approach
#         for i in range(N):
#             x, y = points[i]
#             if (x < 0.5 and y < 0.5) or (x > 0.5 and y > 0.5):
#                 count_triangles[N_values.index(N)] += 1
#
#     # Calculate relative frequencies
#     relative_freq_circle = [count / N for count in count_inside_circle]
#     relative_freq_center = [count / N for count in count_inside_center]
#     relative_freq_triangles = [count / N for count in count_triangles]
#
#     # Print the results
#     for i, N in enumerate(N_values):
#         print(f'N = {N}:')
#         print(f'i) Frecventa relativa este {relative_freq_circle[i]:.4f}')
#         print(f'ii) Frecventa relativa este {relative_freq_center[i]:.4f}')
#         print(f'iii) Frecventa relativa este {relative_freq_triangles[i]:.4f}')
#         print()
#
#     # Valori ale lui N
#     N_values = [500, 1000, 2000]
#
#     # Initializează subploturile
#     fig, axes = plt.subplots(len(N_values), 4, figsize=(15, 10))
#
#     for i, N in enumerate(N_values):
#         # Generează punctele uniform aleatorii în pătrat
#         points = [(random(), random()) for _ in range(N)]
#
#         # Subplot 1: Pătratul și punctele
#         axes[i, 0].plot(*zip(*points), 'ro', markersize=1)
#         axes[i, 0].set_xlim(0, 1)
#         axes[i, 0].set_ylim(0, 1)
#         axes[i, 0].set_aspect('equal')
#         axes[i, 0].set_title(f'N = {N}')
#         axes[i, 0].add_patch(plt.Rectangle((0, 0), 1, 1, fill=False))
#
#         # Subplot 2: Pătratul și cercul pentru condiția (i)
#         axes[i, 1].plot(*zip(*points), 'ro', markersize=1)
#         axes[i, 1].add_patch(plt.Circle((0.5, 0.5), 0.5, color='b', fill=False))
#         axes[i, 1].set_xlim(0, 1)
#         axes[i, 1].set_ylim(0, 1)
#         axes[i, 1].set_aspect('equal')
#         axes[i, 1].set_title(f'Condition (i) - N = {N}')
#
#         # Subplot 3: Pătratul și punctele pentru condiția (ii)
#         center = (0.5, 0.5)
#         distances_to_center = [((x - center[0]) ** 2 + (y - center[1]) ** 2) ** 0.5 for x, y in points]
#         distances_to_corners = [min(x, 1 - x, y, 1 - y) for x, y in points]
#         condition_ii_points = [point for j, point in enumerate(points) if
#                                distances_to_center[j] < distances_to_corners[j]]
#         axes[i, 2].plot(*zip(*condition_ii_points), 'ro', markersize=1)
#         axes[i, 2].set_xlim(0, 1)
#         axes[i, 2].set_ylim(0, 1)
#         axes[i, 2].set_aspect('equal')
#         axes[i, 2].set_title(f'Condition (ii) - N = {N}')
#
#         # Subplot 4: Pătratul și punctele pentru condiția (iii)
#         v1 = [0.5, 0.5]
#         v2 = [0.5, 0.5]
#         v3 = [0.5, 0.5]
#         v4 = [0.5, 0.5]
#         triangle1_points = []
#         triangle2_points = []
#         for point in points:
#             if point[0] < 0.5 and point[1] < 0.5:
#                 v1 = point
#                 triangle1_points.append(point)
#             elif point[0] > 0.5 > point[1]:
#                 v2 = point
#                 triangle1_points.append(point)
#             elif point[0] < 0.5 < point[1]:
#                 v3 = point
#                 triangle2_points.append(point)
#             else:
#                 v4 = point
#                 triangle2_points.append(point)
#
#         axes[i, 3].plot(*zip(*triangle1_points), 'ro', markersize=1)
#         axes[i, 3].plot(*zip(*triangle2_points), 'ro', markersize=1)
#         axes[i, 3].set_xlim(0, 1)
#         axes[i, 3].set_ylim(0, 1)
#         axes[i, 3].set_aspect('equal')
#         axes[i, 3].set_title(f'Condition (iii) - N = {N}')
#         axes[i, 3].plot([v1[0], v2[0], v3[0], v4[0], v1[0]], [v1[1], v2[1], v3[1], v4[1], v1[1]], 'b-')
#
#     plt.tight_layout()
#     plt.show()
from matplotlib.pyplot import axis, plot
from random import random
from math import dist

def problema2():
    # Definirea laturii pătratului
    latura = 1.0

    # Definirea centrului pătratului
    centru = latura / 2

    # Definirea razei cercului tangent laturilor pătratului
    raza_cerc = latura / 2

    # Numărul total de puncte generate
    numar_puncte = [500, 1000, 2000]

    for n in numar_puncte:
        # Inițializarea contoarelor pentru fiecare cerință
        puncte_in_cerc = 0
        puncte_mai_aproape_de_centru = 0
        triunghiuri_ascutite = 0
        triunghiuri_obtuz = 0

        # Listele pentru stocarea coordonatelor x și y ale punctelor generate
        x_coord = []
        y_coord = []

        for _ in range(n):
            # Generare punct aleator în pătrat
            x = random() * latura
            y = random() * latura

            # Adăugarea coordonatelor punctului la listele de coordonate
            x_coord.append(x)
            y_coord.append(y)

            # Cerința i) - Contorizarea punctelor în interiorul cercului
            if dist((x, y), (0.5, 0.5)) <= 0.5:
                puncte_in_cerc += 1

            # Cerința ii) - Contorizarea punctelor mai aproape de centrul pătratului
            # decât de vârfurile pătratului
            distanta_centru = dist((x, y), (centru, centru))
            distanta_margine = min(x, y, latura - x, latura - y)
            if distanta_centru < distanta_margine:
                puncte_mai_aproape_de_centru += 1

            # Cerința iii) - Identificarea triunghiurilor formate cu vârfurile pătratului
            if (x < centru and y < centru) or (x > centru and y > centru):
                triunghiuri_ascutite += 1
            else:
                triunghiuri_obtuz += 1

        # Calcularea frecvenței relative pentru fiecare cerință
        frecventa_i = puncte_in_cerc / n
        frecventa_ii = puncte_mai_aproape_de_centru / n
        frecventa_iii_ascutite = triunghiuri_ascutite / n
        frecventa_iii_obtuz = triunghiuri_obtuz / n

        # Afișarea rezultatelor
        print(f'Pentru {n} puncte generate:')
        print(f'i) Frecventa punctelor in cerc: {frecventa_i}')
        print(f'ii) Frecventa punctelor mai aproape de centrul patratului: {frecventa_ii}')
        print(f'iii) Frecventa triunghiurilor ascutite: {frecventa_iii_ascutite}')
        print(f'iii) Frecventa triunghiurilor obtuze: {frecventa_iii_obtuz}')
        print()

        # Afișarea pătratului și punctelor generate
        plot(x_coord, y_coord, 'ro')
        axis('equal')
