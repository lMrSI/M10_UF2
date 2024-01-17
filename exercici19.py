areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]

print(areas_pis[1])
print(areas_pis[-1])
print(areas_pis[-7])
print(areas_pis[:3])
print(areas_pis[2:])
total_habitacions = areas_pis[5] + areas_pis[-1]
print(total_habitacions)

# Modificar l'àrea del lavabo i imprimir la nova llista 'areas_pis'
index_lavabo = areas_pis.index("Lavabo")
areas_pis[index_lavabo + 1] = 8.5
print(areas_pis)

# Afegir l'àrea de "pati interior" i 2.78 a les últimes posicions. Imprimir la nova llista 'areas_pis'.
areas_pis.extend(["Pati interior", 2.78])
print(areas_pis)

# Imprimir el total de l'àrea del pis.
total_area_pis = sum(areas_pis[1::2])
print(total_area_pis)