import click
from clickshot.recorder import start_recording


@click.group()
def cli():
    """ClickShot — Annotated Screenshot Recorder"""
    pass

@cli.command()
@click.option("--output-dir", default="output", help="Where to save screenshots")
@click.option('--screenshot', default='grim', type=click.Choice(['grim', 'maim', 'scrot']), help='Screenshot backend')
@click.option('--cursor', default='hyprctl', type=click.Choice(['hyprctl', 'xdotool']), help='Cursor provider')
@click.option('--display', default='eDP-1',help='Specific Display/Monitor to capture')
def record(output_dir, screenshot, cursor, display):
    """Start recording mouse/touch clicks, 'q' to Quit recording and 'p' to Pause/Resume recording"""
    from clickshot.backends.grim_backend import GrimScreenshot
    from clickshot.backends.maim_backend import MaimScreenshot
    from clickshot.backends.scrot_backend import ScrotScreenshot
    from clickshot.backends.hyprctl_cursor import HyprctlCursor
    from clickshot.backends.xdotool_cursor import XdotoolCursor
    screenshot_backend = {
        "grim": GrimScreenshot(display),
        "maim": MaimScreenshot(),
        "scrot": ScrotScreenshot()
    }[screenshot]

    cursor_provider = {
        "hyprctl": HyprctlCursor(),
        "xdotool": XdotoolCursor()
    }[cursor]

    start_recording(output_dir, screenshot_backend, cursor_provider)

if __name__ == "__main__":
    cli()