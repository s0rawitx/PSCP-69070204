def main():
    data = {}
    years = set()

    while True:
        line = input().strip()
        if line == "END":
            break

        year = line[:2]
        faculty = int(line[2:4])

        years.add(year)

        if year not in data:
            data[year] = {}

        if faculty not in data[year]:
            data[year][faculty] = 0

        data[year][faculty] += 1

    sorted_years = sorted(list(years))

    for year in sorted_years:
        faculties = sorted(list(data[year].keys()))
        first_fac = True
        for faculty in faculties:
            count = data[year][faculty]
            if first_fac:
                print(f"{year} {faculty} {count}")
                first_fac = False
            else:
                print(f"-- {faculty} {count}")


main()