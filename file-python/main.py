import time

import psutil
from rich.live import Live
from rich.table import Table


def make_bar(percent: float, width: int = 30) -> str:
    filled = int(width * percent / 100)
    return "[green]" + "█" * filled + "[/green]" + "[grey35]" + "░" * (width - filled) + "[/grey35]"


def make_table() -> Table:
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent

    table = Table(title="System Monitor")
    table.add_column("Metric", style="cyan")
    table.add_column("Usage", justify="right")
    table.add_column("Bar")

    table.add_row("CPU", f"{cpu:.1f}%", make_bar(cpu))
    table.add_row("Memory", f"{memory:.1f}%", make_bar(memory))
    return table


def main() -> None:
    with Live(make_table(), refresh_per_second=2, screen=True) as live:
        while True:
            live.update(make_table())
            time.sleep(0.5)


if __name__ == "__main__":
    main()
