"""Generate star triangles."""


def star_triangle(rows: int) -> list[str]:
    """Return the lines of a left-aligned star triangle."""
    return ["*" * row for row in range(1, rows + 1)]


if __name__ == "__main__":
    rows = int(input("Enter the number of rows for the star triangle: "))
    print("\n".join(star_triangle(rows)))