from rich.console import Console
from rich.table import Table


def vi_as_str(array):
    indx = [str(i) for i in range(len(array))]
    vals = [str(i) for i in array]
    return (indx, vals)


if __name__ == "__main__":
    data = [i for i in range(1, 11)]
    data.reverse()

    #tab = Table(title='Circular Array')
    tab = Table(title='Circular Array', show_lines=True)

    ind, val = vi_as_str(data)
    tab.add_column('value')
    for v in val:
        tab.add_column(v)

    tab.add_row('index', *ind)
    tab.add_row('index', *ind)

    console = Console()
    console.print(tab)
