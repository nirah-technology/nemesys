from pathlib import Path
from libs.html2png.html2png import HtmlSnapshot

identifiers: list[str] = [
    "masculine",
    "masculine-hover",
    "masculine-pressed",
    "masculine-disabled",
    "feminine",
    "feminine-hover",
    "feminine-pressed",
    "feminine-disabled",
    "trans",
    "trans-hover",
    "trans-pressed",
    "trans-disabled",
    "button",
    "button-hover",
    "button-pressed",
    "button-disabled",
]

for id in identifiers:
    HtmlSnapshot.snapshot(
        url="tools/html/styling/styling.html",
        html_balise_id=id,
        picture_destination_folder=Path("resources/assets/pictures"),
        picture_name=id
    )