def nb_year(p0, percent, aug, p):
    days = 0
    population = p0
    while population < p:
        population += int(population * (percent / 100) + aug)
        days += 1
    return days