from rich.console import Console
from rich.progress import ProgressBar

values = {
    "A": 2.16,
    "B": 4.33,
    "C": 6.57,
    "D": 8.71,
}

console = Console()
maximum = max(values.values())

def render_bar_chart(values):
    for label, value in values.items():
        bar = ProgressBar(total=maximum, completed=value, width=40)
        
        console.print(f"{label}: ", bar, f" {value}")

render_bar_chart(values)