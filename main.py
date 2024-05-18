import click

from custom_types import SettingsType
from view.CursesView import CursesView
from model.Model import Model
from controller.CursesMouseController import CursesMouseController


@click.command()
@click.option(
    "--difficulty",
    "-d",
    type=click.Choice(["easy", "medium", "hard", "custom"], case_sensitive=False),
    default="medium",
    help="",
)
@click.option("--settings", "-s", nargs=3, type=(int, int, int), help="")
def start_app(**args):
    model = Model(**args)
    view = CursesView()
    controller = CursesMouseController(model, view)
    controller.main_loop()


if __name__ == "__main__":
    start_app()
