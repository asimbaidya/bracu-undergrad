from rich.console import Console
from rich.table import Table
from rich.table import box


def vi_as_str(array):
    indx = [str(i) for i in range(len(array))]
    vals = [str(i) for i in array]
    return (indx, vals)


def show_la(array, ttl="Linear array"):
    ind, val = vi_as_str(array)

    # init table
    tab = Table(title=ttl, show_lines=True, box=box.HEAVY)

    # console init
    console = Console()

    # addign values to the table
    tab.add_column("value")
    for v in val:
        tab.add_column(v)

    # addign indexes to the table
    tab.add_row("index", *ind)

    # showing the outpu
    console.print(tab)


def show_ca(array, start, size, ttl="Circulry Array"):
    ind, val = vi_as_str(array)

    # init table
    tab = Table(title=ttl, show_lines=True, box=box.HEAVY)

    # console init
    console = Console()

    # addign values to the table
    tab.add_column("value")
    for v in val:
        tab.add_column(v)

    # addign ca indexex to the tables
    f = ind[len(array) - start :]
    l = ind[: len(array) - start]
    caind = f + l
    tab.add_row("CA index", *caind)

    # addign la indexes to the table
    tab.add_row("LA index", *ind)

    # showing the outpu
    console.print(tab)


if __name__ == "__main__":
    cai = [0, 0, 1, 2, 3, 4, 0, 0]
    show_la(cai)
