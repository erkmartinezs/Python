from bbdd_project import DATA


def run():

    # Using List Comprenhentions

    allPythonDevs = [
        worker["name"] for worker in DATA if worker["language"] == 'python'
    ]

    allPlatziWorkers = [
        worker["name"] for worker in DATA if worker["organization"] == 'Platzi'
    ]

    for worker in allPythonDevs:
        print(worker)

    for worker in allPlatziWorkers:
        print(worker)

    # Using High Order Funtions (Exercise)

    allPythonDevs = list(
        filter(lambda worker: worker["language"] == 'python', DATA))
    allPythonDevs = list(map(lambda worker: worker["name"], allPythonDevs))

    allPlatziWorkers = list(
        filter(lambda worker: worker["organization"] == 'Platzi', DATA))
    allPlatziWorkers = list(
        map(lambda worker: worker["name"], allPlatziWorkers))

    for worker in allPythonDevs:
        print(worker)

    for worker in allPlatziWorkers:
        print(worker)

    #--------------------------------------------------
    # Using High Order Funtions
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    oldPeople = list(
        map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
    # Alternative in python between 3.5 and 3.9
    #oldPeople = list(map(lambda worker: {**worker, **{"old": worker["age"] > 70}}, DATA))

    for worker in adults:
        print(worker)

    for worker in oldPeople:
        print(worker)

    # Using List Comprenhentions  (Exercise)

    adults = [worker["name"] for worker in DATA if worker["age"] > 18]

    for worker in adults:
        print(worker)


if __name__ == '__main__':
    run()